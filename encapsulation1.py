class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance=balance

    def deposit(self, amount):
        self.__balance+= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount("Alice", 10000)
acc.deposit(5000)
print(acc.get_balance())