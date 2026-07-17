cubes = (x**3 for x in range(1,6))

for num in cubes:
    print(num)
print()
odd_num = (x for x in range(1,11) if x % 2 != 0)
for num in odd_num:
    print(num)