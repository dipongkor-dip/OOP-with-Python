# base class , common attribute + functionality class
class Gadget:
    def __init__(self, brand, price, origin):
        self.brand = brand
        self.price = price
        self.origin = origin

    def run(self):
        return f"Running Gadget: {self.brand}"


class Laptop:
    def __init__(self, ram, ssd):
        self.ram = ram
        self.ssd = ssd

    def add_laptop(self, ram, ssd):
        self.ram = ram
        self.ssd = ssd


class Phone(Gadget):
    def __init__(self, brand, price, origin, battery, memory):
        self.battery = battery
        self.memory = memory
        super().__init__(brand, price, origin)

    def __repr__(self):
        return f"Phone Specification- brand: {self.brand}, price: {self.price}, origin : {self.origin}, battery: {self.battery}, memory: {self.memory}"

    def add_phone(self, battery, memory):
        self.battery = battery
        self.memory = memory


# inheritance

my_phone = Phone("APPLE", 59000, "USA", "6000mh", "128GB")


print(my_phone)
