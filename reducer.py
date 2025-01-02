import sys
from collections import defaultdict

# Dictionaries to store aggregated results
route_counts = defaultdict(int)
customer_revenue = defaultdict(float)
distance_price = defaultdict(list)

for line in sys.stdin:
    key, value = line.strip().split("\t")

    try:
        value = float(value)
    except ValueError:
        continue

    # Aggregate results based on key
    if "-" in key and len(key.split("-")) == 2:  # Routes
        route_counts[key] += int(value)
    elif key.replace(".", "", 1).isdigit():  # Distance vs Flight Price
        distance_price[float(key)].append(value)
    else:  # Customer Revenue
        customer_revenue[key] += value

# Output Most Popular Routes
print("Most Popular Routes:")
for route, count in sorted(route_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{route}\t{count}")

# Output Highest Revenue Customers
print("\nHighest Revenue-Generating Customers:")
for customer, revenue in sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)[:5]:  # Top 5
    print(f"{customer}\t{revenue}")

# Output Distance vs Flight Price (Average)
print("\nDistance vs Flight Price (Average):")
for distance, prices in distance_price.items():
    avg_price = sum(prices) / len(prices)
    print(f"{distance}\t{avg_price}")
