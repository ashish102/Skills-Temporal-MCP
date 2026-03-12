import sys
import urllib.request
import json

def get_dallas_temperature():
    """Fetch current temperature in Dallas and return rounded to nearest integer"""
    try:
        response = urllib.request.urlopen('https://api.open-meteo.com/v1/forecast?latitude=32.7767&longitude=-96.7970&current=temperature_2m')
        data = json.load(response)
        return round(data['current']['temperature_2m'])
    except Exception as e:
        print(f"Error fetching temperature: {e}")
        return 1  # Default to 1 if unable to fetch

def is_temperature_offset_prime(n, temperature_offset):
    n = n + temperature_offset
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(sys.argv[1])
    temp = get_dallas_temperature()
    result = is_temperature_offset_prime(num, temp)
    print(f"Dallas temperature: {temp}°C")
    print(f"{num} is temperature-offset prime (with offset {temp}): {result}")