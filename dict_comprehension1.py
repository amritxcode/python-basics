squares = {x: x*x for x in range(1,6)}
print(squares,"\n")

names = ["Amrit", "Alice", "Bob"]
len_name= {x: len(x) for x in names}
print(len_name,"\n")

numbers = [1, 2, 3, 4, 5, 6]
even_squares = {x: x*x for x in numbers if x % 2 == 0}
print(even_squares)