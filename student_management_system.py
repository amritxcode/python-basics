students = []

#taking student inputs
def add_student():
    student_id = int(input("Enter id: "))
    if id <= 0:
        print("Error: ID must be greater than 0.")
        return
    
    #checking duplicates
    for student in students:
        if student_id == student["id"]:
            print("Student id already exists.")
            return
        
    #validating name  
    name = input("Enter name: ")
    if len(name.strip())==0:
        print("Error: Name cannot be blank.")
        return

    # Check age    
    age = int(input("Enter age: "))
    if age < 16 and age >= 60:
        print("Error: Age must be between 16 to 60.")
        return
    
    cgpa = float(input("Enter CGPA: "))
    if cgpa <=0.0 and cgpa >= 10.0:
        print("Error: CGPA must be between 0.0 to 10.0.")
        return
    
    # create the student dict
    student_dict = {
        "id" : student_id, 
        "name" : name.strip(),
        "age" : age,
        "cgpa" : cgpa
    }

    #adding student dict to the list
    students.append(student_dict)
    print("Student added successfully!")


def search_student():
    search_id = int(input("Enter student id: "))
    for student in students:
        if search_id == student["id"]:
            print(f"ID: {student["id"]}, Name: {student["name"]}, Age: {student["age"]}, CGPA: {student["cgpa"]}")
            return
    print("Student not found")