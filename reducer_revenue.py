#!/usr/bin/env python3
import sys
from collections import defaultdict

customer_revenue = defaultdict(float)

for line in sys.stdin:
    user, revenue = line.strip().split("\t")
    customer_revenue[user] += float(revenue)

print("Highest Revenue-Generating Customers:")
for user, revenue in sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)[:5]:  # Top 5
    print(f"{user}\t{revenue}")
