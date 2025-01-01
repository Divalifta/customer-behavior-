import sys

# Read each line from input
for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) < 8:  # Ensure valid data
        continue

    # Extract relevant fields
    route = f"{data[4]}-{data[5]}"  # from-to
    user = data[1]                  # user_name
    revenue = float(data[7])        # total revenue
    distance = float(data[10])      # distance
    flight_price = float(data[8])   # flight price

    # Emit key-value pairs
    print(f"{route}\t1")              # Most popular routes
    print(f"{user}\t{revenue}")       # Revenue per customer
    print(f"{distance}\t{flight_price}")  # Distance vs flight price
