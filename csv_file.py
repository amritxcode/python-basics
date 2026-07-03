import csv

with open("Basics/students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row["Name"])