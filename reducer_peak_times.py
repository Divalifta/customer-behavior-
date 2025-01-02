#!/usr/bin/env python3
import sys
from collections import defaultdict

date_counts = defaultdict(int)

for line in sys.stdin:
    date, count = line.strip().split("\t")
    date_counts[date] += int(count)

print("Most Popular Travel Dates:")
for date, count in sorted(date_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{date}\t{count}")
