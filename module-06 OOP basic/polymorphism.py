# polymorphism
# poly --> many
# morph --> shape


class Device:
    def __init__(self, brand):
        self.brand = brand

    def get_device(self):
        print("Get Device")


class Phone(Device):
    def __init__(self, brand):
        super().__init__(brand)

    def get_device(self):
        print("This is Phone")


class Laptop(Device):
    def __init__(self, brand):
        super().__init__(brand)

    def get_device(self):
        print("This is Laptop")


class Watch(Device):
    def __init__(self, brand):
        super().__init__(brand)

    def get_device(self):
        print("This is Watch")


samsung_phone = Phone("samsung")
samsung_phone.get_device()

hp_laptop = Laptop("HP Laptop")
hp_laptop.get_device()

apple_watch = Watch("Apple Watch")
apple_watch.get_device()
