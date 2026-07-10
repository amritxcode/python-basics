import csv

valid_students = []
invalid_students = []

with open("students_raw.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reason = ""

        try:
            # Rule 1: Status check
            if row["status"].strip() != "active":
                reason = "Inactive student"

            # Rule 2: Name check
            elif row["name"].strip() == "":
                reason = "Missing name"

            # Rule 3: Email check
            elif row["email"].strip() == "":
                reason = "Missing email"

            # Rule 4: CGPA conversion
            else:
                cgpa = float(row["cgpa"])

                # Rule 5: CGPA range
                if not (0 <= cgpa <= 10):
                    raise ValueError("CGPA out of range")

        except ValueError as error:
            reason = str(error)

        if reason == "":
            valid_students.append(row)

        else:
            invalid_students.append({
                "student_id": row["student_id"],
                "reason": reason
            })


print("Valid Students:")
print(valid_students)

print("\nInvalid Students:")
print(invalid_students)