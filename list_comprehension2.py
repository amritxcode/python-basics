odd = [x for x in range(1,21) if x % 2 != 0]
print(odd,"\n")

names = ["Amrit", "Alice", "Bob", "Charlie", "Eva"]

four_letters = [x for x in names if len(x) > 4]
print(four_letters,"\n")

numbers = [2, 5, 8, 11, 14]

even_squares = [x*x for x in numbers if x%2 == 0]
print(even_squares)