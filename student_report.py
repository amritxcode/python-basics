def student_report(name, *marks):
    if not marks:
        return None
        
    def find_max():
        if not marks:
            return None
        
        largest = marks[0]
        for num in marks[1:]:
            if num > largest:
                largest = num
        return largest
        

    def average():
        total = 0
        for num in marks:
            total += num
        return total/len(marks)

    def low():  
        lowest = marks[0]
        for mark in marks[1:]:
            if mark < lowest:
                lowest = mark
        return lowest   
    
    return {
        "name" : name,
        "highest" : find_max(),
        "lowest" : low(),
        "avg" : average(),
        "marks" : marks
    }

results = student_report("Amrit", 85,89,90,77,89,91)

print(f"Student : {results['name']}")
print(f"Marks : {results['marks']}")
print(f"Average : {round(results['avg'],2)}")
print(f"Highest : {results['highest']}")
print(f"Lowest : {results['lowest']}")
