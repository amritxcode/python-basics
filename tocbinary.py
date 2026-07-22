def is_binary(text):
    if not text:
        return False
    
    for char in text:
        if char != "0" and char != "1":
            return False
    return True

user_input = input("Enter string: ")

if is_binary(user_input):
    print("String is binary")
else:
    print("String is not binary")