n = int(input("Enter a number: "))
if n < 1:
    print("Enter a positive number greater than 1")
elif n == 2:
    print("2 is Prime")
else:    
    for i in range(2,(round(n / 2)+1)):
        if n % i == 0:
            print(f"{n} is Not Prime.")
            break
        else:
            print(f"{n} is Prime.")
            break