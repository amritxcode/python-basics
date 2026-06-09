num = int(input("Enter a number: "))

if(num==1 or num==0):
    print("Not Prime")
else:
    isPrime=True

    for i in range(2, num):
        if num % i == 0:
            isPrime=False
            break
    if isPrime ==True:
        print("Is Prime")
    else:
        print("Not Prime")