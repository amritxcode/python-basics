class Student:  #we define class's name as Student
    def __init__(self, name, roll_no, section):   #when someone creates a student, pythin automatically runs this method
        self.name = name    #Store the value passed in name inside this object's name attribute.
        self.roll_no = roll_no
        self.section = section
    def display_info(self):
        print(self.name)
        print(self.roll_no)
        print(self.section)
    




amrit = Student("Amrit", 12, "A")
alice = Student("Alice", 18, "B")

amrit.display_info()
alice.display_info()
