import sys
from collections import defaultdict

# Dictionaries to store results
route_counts = defaultdict(int)
customer_revenue = defaultdict(float)
distance_price = defaultdict(list)

# Read each line from input
for line in sys.stdin:
    key, value = line.strip().split("\t")
    if "-" in key:  # Most popular routes
        route_counts[key] += int(value)
    elif key.replace(".", "", 1).isdigit():  # Distance vs Flight Price
        distance_price[float(key)].append(float(value))
    else:  # Revenue per customer
        customer_revenue[key] += float(value)

# Output Most Popular Routes
print("Most Popular Routes:")
for route, count in sorted(route_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{route}\t{count}")

# Output Highest Revenue Customers
print("\nHighest Revenue-Generating Customers:")
for customer, revenue in sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True):
    print(f"{customer}\t{revenue}")

# Output Distance vs Flight Price
print("\nDistance vs Flight Price:")
for distance, prices in distance_price.items():
    avg_price = sum(prices) / len(prices)
    print(f"{distance}\t{avg_price}")
