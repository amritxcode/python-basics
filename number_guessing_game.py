import random

print("Welcome to Guessing Game")

num = random.randint(1,101)
print(num)

while True:
    user = int(input("Guess a number: "))
    diff = user - num
    if diff == 0:
        print("You won.")
        break
    elif diff >= 20:
        print("Too high. Guess again.")
    elif diff <= -20:
        print("Too low, Guess again.")
    elif abs(diff) <= 10:
        print("Very close. Try again.")
    else:
        print("You are close. Guess again.")