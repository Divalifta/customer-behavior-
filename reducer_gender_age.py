#!/usr/bin/env python3
import sys
from collections import defaultdict

gender_age_counts = defaultdict(int)

for line in sys.stdin:
    key, count = line.strip().split("\t")
    gender_age_counts[key] += int(count)

print("Booking Counts by Gender and Age Group:")
for key, count in sorted(gender_age_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{key}\t{count}")
