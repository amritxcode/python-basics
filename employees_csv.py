import csv

def emp_data():
    with open("Basics/employees.csv", "r") as file:
        reader = csv.DictReader(file)
        employees = {}
        for row in reader:
            employees[row["Name"]] = row["Department"]
    
    return employees

print(emp_data())