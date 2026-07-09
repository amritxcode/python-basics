import csv

clean_employees = []

# Read the source file
with open("raw_employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if (
            row["department"] == "AI"
            and row["status"] == "active"
            and row["name"].strip() != ""
            and row["salary"] != "invalid"
        ):
            clean_employees.append(row)

fieldnames = [
    "employee_id",
    "name",
    "department",
    "salary",
    "email",
    "status"
]

# Write to a NEW file
with open("clean_employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(clean_employees)