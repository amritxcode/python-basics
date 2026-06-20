def add_student():
    name = (input("Enter student's name: "))
    students.append(name.lower())

def view_students():
    for student in students:
        print(student)

def search_student():
    search = input("Enter a name to search: ").lower()
    if search in students:
        print(f"Found at No.{students.index(search) + 1}")
    else:
        print("Not Found")

students=[]

while True:
    print("\nEnter 1 to add student\nEnter 2 to view students\nEnter 3 to search a student\nEnter 4 to exit\n")
    num= (input("Enter a number: "))
    if num == '1':
        add_student()
    elif num == '2':
        view_students()
    elif num =='3':
        search_student()

    elif num == '4':
        break
    else:
        print("Invalid input")