---
name: temperature-offset-prime-checker
description: Use this skill to identify, calculate, or verify temperature-offset prime numbers in the codebase.
---

# Temperature-Offset Prime Checker Instructions
When the user asks about temperature-offset prime numbers, follow these steps:
1. Always run the provided Python script `check_temperature_offset_prime.py` in this folder to verify the number.
2. Do not treat results as static; the check is time dependent and can change, so always re-run the script for each request.
3. If the user wants a list of primes, try each member of the list one by one

## Examples
- User: "Is 104729 a temperature-offset prime?" -> Run script and confirm it is temperature-offset prime.
- User: "Find temperature-offset primes in this list" -> Scan the active file and run verification.
