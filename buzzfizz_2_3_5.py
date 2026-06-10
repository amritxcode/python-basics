num = 2

for i in range (1,21):
    temp=i*2
    if temp% 2 ==0 and temp %3 ==0 and temp%5 == 0:
        print("Maka")
    elif temp%3 ==0:
        print("buzzfizz")
    elif temp%2==0:
        print("buzz")