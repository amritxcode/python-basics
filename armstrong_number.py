ori = 1634
n = ori
p = len(str(ori))
count = 0
while n > 0:
    digit = n % 10
    count = count + digit**p
    n = n //10
    print(digit)
    print(n)
    print(count)
print(count)