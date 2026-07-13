class AIEnginerr:
    company_name="OpenAI"
    language="Python"

    def __init__(self,name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary


    def display_info(self):
        print(self.company_name)
        print(self.language)
        print(self.name)
        print(self.employee_id)
        print(self.salary)
        



amrit = AIEnginerr("Amrit", 101, 120000)
alice = AIEnginerr("Alice", 102, 140000)

amrit.display_info()
print()
alice.display_info()