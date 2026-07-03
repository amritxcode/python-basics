def add_student():
    """
    Add a student's name to the students file.

    Prompts:
        Student name.

    Returns:
        None.
    """
    name = input("Enter student's name: ").strip().title()
    if not name:
        print("Name cannot be empty.")
        return
    with open("Basics/students.txt", "a") as file:
        file.write(name + "\n")
        print("Student added successfully")

add_student()