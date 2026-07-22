def count_all(text):
    digits = 0
    alphabets = 0
    special_chrs = 0

    for char in text:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alphabets += 1
        else:
            special_chrs += 1

    print(f"Digits: {digits}")
    print(f"Alphabets: {alphabets}")
    print(f"Special Characters: {special_chrs}")

user = input("Enter text: ")
count_all(user)