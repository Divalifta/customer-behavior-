#!/usr/bin/env python3
import sys

for line in sys.stdin:
    if line.startswith("from"):
        continue

    data = line.strip().split(",")
    if len(data) < 6:
        continue

    try:
        gender = data[2]
        age = int(data[3])
        age_group = "Under 18" if age < 18 else "18-35" if age <= 35 else "35+"
        print(f"{gender}-{age_group}\t1")
    except ValueError:
        continue
