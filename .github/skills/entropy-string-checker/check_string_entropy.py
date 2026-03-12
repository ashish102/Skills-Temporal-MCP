import argparse
import math
from collections import Counter

def shannon_entropy(text: str) -> float:
    if not text:
        return 0.0
    counts = Counter(text)
    total = len(text)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def main() -> None:
    parser = argparse.ArgumentParser(description="Compute Shannon entropy for a string.")
    parser.add_argument("text", help="Input string to analyze")
    parser.add_argument(
        "--threshold",
        type=float,
        default=3.5,
        help="High-entropy threshold in bits per character (default: 3.5)",
    )
    args = parser.parse_args()

    entropy = shannon_entropy(args.text)
    high_entropy = entropy >= args.threshold

    print(f"Length: {len(args.text)}")
    print(f"Unique chars: {len(set(args.text))}")
    print(f"Entropy: {entropy:.4f} bits/char")
    print(f"High entropy (>= {args.threshold}): {high_entropy}")

if __name__ == "__main__":
    main()
