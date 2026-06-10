num = int(input("Enter a number: "))

reversed_number = 0

while num > 0:
    last_digit = num%10
    reversed_number = reversed_number*10 + last_digit
    num= num//10
print(reversed_number)