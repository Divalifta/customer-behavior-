import sys

for line in sys.stdin:
    # Skip the header row
    if line.startswith("from"):
        continue

    data = line.strip().split(",")
    if len(data) < 12:  # Ensure the row has enough columns
        continue

    try:
        # Extract relevant fields
        route = f"{data[4]}-{data[5]}"  # 'from-to'
        user = data[1]                  # 'user_name'
        revenue = float(data[10])       # 'total'
        distance = float(data[9])       # 'distance'
        flight_price = float(data[7])   # 'flight_price'

        # Emit key-value pairs
        print(f"{route}\t1")              # Popular routes
        print(f"{user}\t{revenue}")       # Revenue per customer
        print(f"{distance}\t{flight_price}")  # Distance vs flight price
    except ValueError:
        # Skip rows with invalid data
        continue
