#!/usr/bin/env python3
import sys
from collections import defaultdict

distance_price = defaultdict(list)

for line in sys.stdin:
    distance, flight_price = line.strip().split("\t")
    distance_price[float(distance)].append(float(flight_price))

print("Distance vs Flight Price (Average):")
for distance, prices in sorted(distance_price.items()):
    avg_price = sum(prices) / len(prices)
    print(f"{distance}\t{avg_price}")
