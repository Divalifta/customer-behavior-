#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Skip the header row
    if line.startswith("from"):
        continue

    data = line.strip().split(",")
    if len(data) < 6:  # Ensure the row has enough columns
        continue

    try:
        # Extract customer and revenue
        user = data[1]              # 'user_name'
        revenue = float(data[15])   # 'total'
        print(f"{user}\t{revenue}")
    except ValueError:
        continue
