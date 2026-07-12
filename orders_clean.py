import csv

valid_orders = []
invalid_orders = []

with open("orders_raw.csv", "r") as file:
    reader = csv.DictReader(file)


    for row in reader:
        reason = ""

        try:
            customer = row["customer"].strip()
            quantity = int(row["quantity"])
            price = int(row["price"])
            status = row["status"].strip()
            row["status"] = status


            if customer == "":
                reason = "Customer cannot be empty"
            elif quantity <= 0:
                reason = "Invalid quantity"
            elif price <= 0:
                reason = "Invalid price"
            else:
                if status not in ["completed", "pending"]:
                    reason = "Invalid status"


        except ValueError as error:
            reason = str(error)

     
        if reason == "":
            row["total_price"] = quantity * price
            valid_orders.append(row)
        else:
            invalid_orders.append({
                "order_id": row["order_id"],
                "reason": reason
                })
        

print("Valid Orders:")
print(valid_orders)
print("Invalid Orders:")
print(invalid_orders)


fieldnames = [
    "order_id",
    "customer",
    "item",
    "quantity",
    "price",
    "status",
    "total_price"
]

with open("clean_orders.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames= fieldnames)

    writer.writeheader()
    writer.writerows(valid_orders)

    invalid_fieldnames = [
    "order_id",
    "reason"
]

with open("rejected_orders.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=invalid_fieldnames)

    writer.writeheader()
    writer.writerows(invalid_orders)


# ---------------- Statistics ----------------

revenue = 0

for order in valid_orders:
    revenue += order["total_price"]

print("\nStatistics")
print(f"Total Orders: {len(valid_orders) + len(invalid_orders)}")
print(f"Valid Orders: {len(valid_orders)}")
print(f"Rejected Orders: {len(invalid_orders)}")
print(f"Revenue: ₹{revenue}")
print(f"Average Order Value: ₹{revenue / len(valid_orders):.2f}")