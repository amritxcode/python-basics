salaries = [
    "85000",
    "72000",
    "invalid",
    "91000",
    "N/A",
    "",
    "65000"
]

invalid_salaries = []
total = 0
valid_counter = 0
for salary in salaries:
    try:
        # Convert salary to int
        salary_int= int(salary)
        total += salary_int
        valid_counter += 1
    except ValueError:
        # Store the invalid salary
        invalid_salaries.append(salary)

print(f"Total Salary: {total}")
print(f"Average Salary: {total/valid_counter}")
print(invalid_salaries)