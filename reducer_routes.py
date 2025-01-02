#!/usr/bin/env python3
import sys
from collections import defaultdict

route_counts = defaultdict(int)

for line in sys.stdin:
    route, count = line.strip().split("\t")
    route_counts[route] += int(count)

print("Most Popular Routes:")
for route, count in sorted(route_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{route}\t{count}")
