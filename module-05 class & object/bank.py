class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f"min withdraw amount: {self.min_withdraw}"
        elif amount > self.max_withdraw:
            return f"you can not withdraw more then: {self.max_withdraw}"
        else:
            if self.balance < amount:
                return "Influence Balance"
            self.balance -= amount
            return f"here is your money: {amount}"


brk = Bank(15000)

res = brk.withdraw(5000)
print(res)

balance = brk.get_balance()
print(balance)

