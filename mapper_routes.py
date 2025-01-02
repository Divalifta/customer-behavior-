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
        # Extract the route fields
        route = f"{data[4]}-{data[5]}"  # 'from-to'
        print(f"{route}\t1")
    except Exception as e:
        print(f"DEBUG: Skipping line due to Exception: {e} -> {line.strip()}")
