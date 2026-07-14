class Employee:
    def work(self):
        print("Employee is working")

class AIEngineer(Employee):
    def work(self):
        print("Building AI models")

class BackendEngineer(Employee):
    def work(self):
        print("Building REST APIs")

amrit = AIEngineer()
alice = BackendEngineer()

amrit.work()
alice.work()