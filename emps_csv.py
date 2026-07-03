import csv

def emps():
    with open("Basics/emp.csv", "r") as infile:
        reader = csv.DictReader(infile)

        with open("Basics/ai_emp.csv", "w", newline="") as outfile:

            fieldnames = ["Name", "Department", "Salary"]

            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                if row["Department"] == "AI":
                    writer.writerow(row)

    print("AI employees saved successfully.")


emps()