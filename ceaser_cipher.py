alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

small_alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

choice = input("Enter E for Encryption or D for Decryption: ")

if choice == "E" or choice == "e":

    pt = input("Enter your text: ")
    sep_pt = list(pt)
    key = int(input("Enter number to shift: "))

    cipher_list = []

    for letter in sep_pt:
        if letter in alphabets:
            letter_index = alphabets.index(letter)
            new_index = (letter_index + key) % 26
            cipher_list.append(alphabets[new_index])

        elif letter in small_alphabets:
            letter_index = small_alphabets.index(letter)
            new_index = (letter_index + key) % 26
            cipher_list.append(small_alphabets[new_index])

        else:
            cipher_list.append(letter)

    ct = "".join(cipher_list)

    print(f"Cipher Text: {ct}")

elif choice == "D" or choice == "d":

    ct = input("Enter cipher text: ")
    sep_ct = list(ct)
    key = int(input("Enter number to shift: "))

    plain_list = []

    for letter in sep_ct:
        if letter in alphabets:
            letter_index = alphabets.index(letter)
            new_index = (letter_index - key) % 26
            plain_list.append(alphabets[new_index])

        elif letter in small_alphabets:
            letter_index = small_alphabets.index(letter)
            new_index = (letter_index - key) % 26
            plain_list.append(small_alphabets[new_index])

        else:
            plain_list.append(letter)

    pt = "".join(plain_list)

    print(f"Plain Text: {pt}")

else:
    print("Invalid Choice!")