class Passenger:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.bus = None


class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login Successfully")
            return True
        else:
            return False
