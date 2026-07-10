import csv

valid = []
invalid = []

with open("model_training_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reason = ""
        
        try:
            email = row["email"].strip()
            row["email"] = email
            skill = row["skill_level"]
            experience = int(row["experience_years"])
            age = int(row["age"])
            if age < 18:
                reason = "Minor, less than 18"
            elif age > 60:
                reason = "Age greater than 60"
            elif 0 > experience or experience > age:
                reason = "Invalid experience"
            elif skill not in ["beginner", "intermediate", "advanced", "expert"]:
                reason = "Invalid skill level"
            elif email == "":
                reason = "Empty email"
            else:
                label = int(row["label"])
                if 0 > label or label > 1:
                    reason = "Invalid label"

        except ValueError as error:
            reason = str(error)
        
        if reason == "":
            valid.append(row)
        else:
            invalid.append({
                "id": row["id"],
                "reason": reason
            })


print("Valid Employees:")
print(valid)

print("\nInvalid Employees:")
print(invalid)

fieldnames = [
    "id", "age","experience_years","skill_level","email","label"
    ]

with open("clean_training_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames= fieldnames)

    writer.writeheader()
    writer.writerows(valid)

invalid_fieldnames = [
    "id", "reason",
]

with open("rejected_training_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=invalid_fieldnames)

    writer.writeheader()
    writer.writerows(invalid)