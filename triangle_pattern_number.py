num = int(input("Enter a number: "))

for i in range(1,num):
    for j in range(i):
        print(i, end="")
    print()