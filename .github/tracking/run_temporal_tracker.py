import argparse
import importlib.util
import json
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
ENTROPY_SCRIPT = REPO_ROOT / '.github' / 'skills' / 'entropy-string-checker' / 'check_string_entropy.py'
PRIME_SCRIPT = REPO_ROOT / '.github' / 'skills' / 'temperature-offset-prime-checker' / 'check_temperature_offset_prime.py'
LOG_PATH = REPO_ROOT / '.github' / 'tracking' / 'temporal-analysis-log.jsonl'


def load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Unable to load module from {module_path}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


entropy_module = load_module(ENTROPY_SCRIPT, 'entropy_checker')
prime_module = load_module(PRIME_SCRIPT, 'temperature_prime_checker')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Track temporal analysis snapshots for a dataset.')
    parser.add_argument('numbers', nargs='*', type=int, help='Dataset values to analyze')
    parser.add_argument('--dataset', help='JSON array of integers, for example [10,20,30]')
    parser.add_argument(
        '--threshold',
        type=float,
        default=3.5,
        help='High-entropy threshold in bits per character (default: 3.5)',
    )
    return parser.parse_args()


def load_numbers(args: argparse.Namespace) -> list[int]:
    if args.dataset:
        parsed = json.loads(args.dataset)
        if not isinstance(parsed, list) or not all(isinstance(value, int) for value in parsed):
            raise ValueError('--dataset must be a JSON array of integers')
        return parsed
    if args.numbers:
        return args.numbers

    config_path = REPO_ROOT / 'config.json'
    if config_path.exists():
        data = json.loads(config_path.read_text(encoding='utf-8'))
        numbers = data.get('numbers')
        if isinstance(numbers, list) and all(isinstance(value, int) for value in numbers):
            return numbers

    raise ValueError('No dataset provided and config.json does not contain a valid numbers list')


def analyze(numbers: list[int], threshold: float) -> dict[str, Any]:
    temperature_c = prime_module.get_dallas_temperature()
    records = []
    for number in numbers:
        text = str(number)
        entropy = entropy_module.shannon_entropy(text)
        is_prime = prime_module.is_temperature_offset_prime(number, temperature_c)
        records.append(
            {
                'number': number,
                'text': text,
                'entropy': round(entropy, 4),
                'entropy_class': 'high' if entropy >= threshold else 'low',
                'temperature_c': temperature_c,
                'offset_value': number + temperature_c,
                'temperature_offset_prime': is_prime,
            }
        )

    snapshot = {
        'timestamp': datetime.now().astimezone().isoformat(timespec='seconds'),
        'dataset': numbers,
        'dataset_key': json.dumps(numbers, separators=(',', ':')),
        'temperature_c': temperature_c,
        'prime_count': sum(1 for item in records if item['temperature_offset_prime']),
        'entropy_summary': {
            'threshold': threshold,
            'average_entropy': round(sum(item['entropy'] for item in records) / len(records), 4),
            'high_entropy_count': sum(1 for item in records if item['entropy_class'] == 'high'),
            'low_entropy_count': sum(1 for item in records if item['entropy_class'] == 'low'),
        },
        'numbers': records,
    }
    return snapshot


def append_snapshot(snapshot: dict[str, Any]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(snapshot) + '\n')


def load_history(dataset_key: str) -> list[dict[str, Any]]:
    if not LOG_PATH.exists():
        return []

    history = []
    with LOG_PATH.open('r', encoding='utf-8') as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get('dataset_key') == dataset_key:
                history.append(row)
    return history


def status_map(snapshot: dict[str, Any]) -> dict[int, bool]:
    return {item['number']: item['temperature_offset_prime'] for item in snapshot['numbers']}


def detect_flips(previous: dict[str, Any] | None, current: dict[str, Any]) -> list[str]:
    if previous is None:
        return []

    previous_status = status_map(previous)
    current_status = status_map(current)
    flips = []
    for number in current['dataset']:
        old_value = previous_status.get(number)
        new_value = current_status.get(number)
        if old_value is None or new_value is None or old_value == new_value:
            continue
        direction = 'became prime' if new_value else 'stopped being prime'
        flips.append(f'{number}: {direction} ({previous["temperature_c"]}C -> {current["temperature_c"]}C)')
    return flips


def format_timeline(history: list[dict[str, Any]], limit: int = 5) -> str:
    rows = []
    for snapshot in history[-limit:]:
        statuses = ' '.join(
            f"{item['number']}:{'Y' if item['temperature_offset_prime'] else 'N'}"
            for item in snapshot['numbers']
        )
        rows.append(
            {
                'timestamp': snapshot['timestamp'],
                'temp': str(snapshot['temperature_c']),
                'prime_count': str(snapshot['prime_count']),
                'statuses': statuses,
            }
        )

    if not rows:
        return 'No snapshots found.'

    headers = {'timestamp': 'Timestamp', 'temp': 'TempC', 'prime_count': 'PrimeCount', 'statuses': 'PerNumber'}
    widths = {key: len(value) for key, value in headers.items()}
    for row in rows:
        for key, value in row.items():
            widths[key] = max(widths[key], len(value))

    line1 = ' | '.join(headers[key].ljust(widths[key]) for key in headers)
    line2 = '-+-'.join('-' * widths[key] for key in headers)
    line_rows = [' | '.join(row[key].ljust(widths[key]) for key in headers) for row in rows]
    return '\n'.join([line1, line2, *line_rows])


def next_check_recommendation(previous: dict[str, Any] | None, current: dict[str, Any], flips: list[str]) -> str:
    if flips:
        return '30-60m recommended because prime status changed.'
    if previous is None:
        return '2-3h recommended until a second snapshot establishes a trend.'
    temperature_delta = abs(current['temperature_c'] - previous['temperature_c'])
    if temperature_delta >= 2:
        return '30-60m recommended because temperature moved quickly.'
    return '2-3h recommended because conditions look stable.'


def main() -> None:
    args = parse_args()
    numbers = load_numbers(args)
    snapshot = analyze(numbers, args.threshold)
    append_snapshot(snapshot)
    history = load_history(snapshot['dataset_key'])
    previous = history[-2] if len(history) >= 2 else None
    flips = detect_flips(previous, snapshot)

    print(f'Dataset: {snapshot["dataset"]}')
    print(f'Current timestamp: {snapshot["timestamp"]}')
    print(f'Dallas temperature: {snapshot["temperature_c"]}C')
    print(f'Prime count: {snapshot["prime_count"]}')
    print('')
    print('Recent timeline')
    print(format_timeline(history))
    print('')
    print('Flip report')
    if flips:
        for flip in flips:
            print(f'- {flip}')
    elif previous is None:
        print('- No previous snapshot for this dataset yet.')
    else:
        print('- No prime flips since the previous snapshot.')
    print('')
    print('Trend summary')
    if previous is None:
        print('- Baseline snapshot recorded. More runs are needed before trends can be inferred.')
    else:
        temp_delta = snapshot['temperature_c'] - previous['temperature_c']
        direction = 'up' if temp_delta > 0 else 'down' if temp_delta < 0 else 'flat'
        print(f'- Temperature is {direction} versus the previous run ({previous["temperature_c"]}C -> {snapshot["temperature_c"]}C).')
        print(f'- Prime count changed from {previous["prime_count"]} to {snapshot["prime_count"]}.')
    print(f'- Next check: {next_check_recommendation(previous, snapshot, flips)}')


if __name__ == '__main__':
    main()
