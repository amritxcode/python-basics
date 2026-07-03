def average(*marks):
    if not marks:
        return None
    total = 0
    for num in marks:
        total += num
    return total/len(marks)