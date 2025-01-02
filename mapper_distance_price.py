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
        # Extract distance and flight price
        distance = float(data[9])      # 'distance'
        flight_price = float(data[7])  # 'flight_price'
        print(f"{distance}\t{flight_price}")
    except ValueError:
        continue
