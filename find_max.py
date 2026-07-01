def find_max(*numbers):
    largest = float('-inf')
    for num in numbers:
        if num >= largest:
            largest = num
    return largest