#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Skip the header row
    if line.startswith("from"):
        continue

    data = line.strip().split(",")
    if len(data) < 20:  # Ensure the row has sufficient columns
        continue

    try:
        travel_date = data[19].strip()  # Adjust column index based on dataset
        year_month = "-".join(travel_date.split("-")[:2])  # Extract year and month (YYYY-MM)
        revenue = float(data[15])       # Extract total revenue
        print(f"{year_month}\t{revenue}")
    except ValueError:
        continue
