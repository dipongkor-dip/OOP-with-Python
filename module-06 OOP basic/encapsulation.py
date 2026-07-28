# encapsulation -> hide details
class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name  # public attribute
        self._branch = "rangpur"  # developer sign = single underscore _ = protected attribute
        

        self.__balance = initial_deposit  # double underscore __ = private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return "Influence Balance"


sunny = Bank("sunny", 12000)

print(sunny.holder_name)

sunny.deposit(56000)

print(dir(sunny))

print(sunny._Bank__balance)
