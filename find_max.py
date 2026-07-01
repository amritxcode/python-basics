def find_max(*numbers):
    if not numbers:
        return None
    
    largest = float('-inf')
    for num in numbers:
        if num > largest:
            largest = num
    return largest