class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for i in self.cart:
            total += i["price"] * i["quantity"]

        if amount < total:
            return f"please provide {total - amount} more money"

        return f"Here is your items and extra money: {amount-total}"


suck = Shopping("alan suck")

suck.add_to_cart("alu", 30, 5)
suck.add_to_cart("dim", 40, 4)
suck.add_to_cart("rice", 50, 3)

print(suck.cart)
total = suck.checkout(600)
print(total)
