class BankAccount:
    def __init__(self, acc_holder, acc_num, bal):
        self.acc_holder = acc_holder
        self.acc_num= acc_num
        self.bal = bal
    
    def display_info(self):
        print(f"Account Holder: {self.acc_holder}")
        print(f"Account Number: {self.acc_num}")
        print(f"Balance: ₹{self.bal}")
    
    def deposit(self,amount):
        if amount <=0:
            print("Invalid amount")
        else:
            self.bal += amount
            print(f"Current Balance: {self.bal}")

    def withdraw(self,amount):
        if amount <=0:
            print("Invalid amount")
        elif self.bal < amount:
            print(f"Insufficient Balance\nCurrent Balance: {self.bal}")
        else:
            self.bal -= amount
            print(f"Balance remaining: {self.bal}")


amrit= BankAccount("Amrit",1001,5000)
alice= BankAccount("Alice", 1002,12000)

amrit.deposit(2000)
amrit.withdraw(1000)
alice.withdraw(15000)
print()
amrit.display_info()
print()
alice.display_info()