num = int(input("Enter a number: "))

isPrime = False
if num > 1:
    isPrime= True
    for i in range (2,num):
        if num % i == 0:
            isPrime = False
            break

if isPrime:
    print("Is a Prime Number")
else:
    print("Not a Prime Number")