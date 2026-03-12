---
name: entropy-string-checker
description: Use this skill to calculate Shannon entropy for a string and classify it as high or low entropy.
---

# Entropy String Checker Instructions
When the user asks about string entropy or whether a string is high-entropy, follow these steps:
1. Always run the provided Python script `check_string_entropy.py` in this folder to compute the entropy.
2. Do not treat results as static; recompute every time, especially when a threshold is provided.
3. If the user gives multiple strings, check each string one by one.
4. If the user provides a threshold, pass it to the script; otherwise use the default threshold.

Additional references:
- Overview: see OVERVIEW.md
- Usage details: see USAGE.md
- Examples: see EXAMPLES.md
