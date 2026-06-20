def add_student():
    name = (input("Enter student's name: "))
    students.append(name)

def view_students():
    for student in students:
        print(student)

students=[]

while True:
    print("Enter 1 to add student\nEnter 2 to view students\nEnter 3 to exit")
    num= (input("Enter a number: "))
    if num == '1':
        add_student()
    elif num == '2':
        view_students()
    elif num == '3':
        break
    else:
        print("Invalid input")
        break