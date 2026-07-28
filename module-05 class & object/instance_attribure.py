# class attribute
class Shop:
    cart = []  # this cart is a class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


himalaya = Shop(buyer="himalaya")
himalaya.add_to_cart("laptop")
himalaya.add_to_cart("phone")

print(himalaya.cart)  # ['laptop', 'phone']

asi = Shop("asi")
asi.add_to_cart("watch")
asi.add_to_cart("camera")

print(asi.cart)  # ['laptop', 'phone', 'watch', 'camera']


# instance attribute
class ShopI:
    shopping_mall = "Padhma"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # it's a instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


himalaya = ShopI(buyer="himalaya")
himalaya.add_to_cart("laptop")
himalaya.add_to_cart("phone")

print(himalaya.cart)  # ['laptop', 'phone']

asi = ShopI("asi")
asi.add_to_cart("watch")
asi.add_to_cart("camera")

print(asi.cart)  # ['watch', 'camera']
