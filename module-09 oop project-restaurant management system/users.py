import abc
from orders import Order


class User(abc.ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()  # cart = order class instance

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("✔ Item added")
        else:
            print("Item not found")

    def view_cart(self):
        print("\n=====view cart=====")
        print("Name\tPrice\tQuantity")

        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")

        print(f"Total Price: {self.cart.total_price}")  # using property

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.employees.append(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def delete_item(self, restaurant, item):
        restaurant.menu.remove_item(item)
