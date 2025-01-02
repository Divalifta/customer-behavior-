#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Skip the header row
    if line.startswith("from"):
        continue

    data = line.strip().split(",")
    if len(data) < 20:  # Ensure the row has enough columns
        continue

    try:
        travel_date = data[19]  # Adjust column index based on dataset
        print(f"{travel_date}\t1")
    except Exception as e:
        continue
