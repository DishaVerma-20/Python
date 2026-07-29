class Bank:
    def __init__(self, account_name:str, balance:int):
        self.account_name = account_name
        # private = double underscore lgakar
        self.__balance = balance

    # getter
    def get_balance(self):
        print(f"Current balance = {self.__balance}")

    # setter, doesn't make sense to change the balance but still
    def set_balance(self, new_amount):
        self.__balance = new_amount

    def deposit(self, amount):
        if self.__isServerLive() == True:
            self.__balance += amount
            print(f"Amount deposited, current balance is: {self.__balance}\n")
        else:
            print("Server is down")

    def __isServerLive(self):
        return True 
        # only for practice

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money in bank account")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn, current balance: {self.__balance}\n")

acc = Bank("Disha", 1000)
acc.deposit(1000)
# acc.balance = 10000000 no attribute 
# acc.__balance = 100000000 still AttributeError
# acc.balance = 1000000 lekin esa nahi hona chahiye 
acc.withdraw(500)
acc.get_balance()
# acc.__isServerLive() can't access it, pta he nahi hai usey 