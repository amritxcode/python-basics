n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

decision = input("Enter 'all' to get all operations, or enter 's' to do a specific operation: ").lower()
if decision == "all":
    print(n1 +n2)
    print(n1- n2)
    print(n1 *n2)
    if n2 != 0:
        print(n1 /n2)
    else:
        print("Cannot divide by zero")

elif decision == "s":
    spec= input("Enter any of '+','-',*','/' to do that specific operation: ")
    if spec == '+':
            print(n1 +n2)
        
    elif spec == '-':
             print(n1- n2)
    elif spec == '*':
              print(n1 *n2)
    elif spec == '/':
        if n2 != 0:
            print(n1 /n2)
        else:
             print("Cannot divide by zero")

    else:
        print("Invalid operation")a