# static attribute (class attribute)
# class method @classmethod
# static method @staticmethod
# differences between class and static method


class Shopping:
    cart = []
    origin = "china"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"buying: {item} for price: {price} and remaining: {remaining}")

    @classmethod  # it's decorator
    def get_product(self, item):
        print("Product fetching for looking", item)

    @staticmethod  # self -> not using
    def multiply(a, b):
        # print(self.name) # not available self
        print("Multiply :", a * b)


# Shopping.purchase() # Shopping.purchase() missing 4 required positional arguments: 'self', 'item', 'price', and 'amount'

bas = Shopping("Bas Market", "Dhaka")

# bas.purchase("Shirt", 3000, 5000)
# bas.get_product("Shirt")

Shopping.get_product("Trousers")  # it's class method for

Shopping.multiply(3, 2)  # static method
