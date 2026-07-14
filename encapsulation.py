class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(self.__balance)
        else:
            print("Invalid amount")
 
 
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(self.__balance)
        else:
            print("Insufficient balance")


    def show_balance(self):
        print(self.__balance)

amrit = BankAccount("Amrit", 5000)

amrit.deposit(2000)
amrit.withdraw(1000)
amrit.show_balance()