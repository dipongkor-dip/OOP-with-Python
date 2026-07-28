class Book:
    def __init__(self, name):
        self.name = name

    def read(self):
        raise NotImplementedError


class Physics(Book):
    def __init__(self, name):
        super().__init__(name)

    def read(self):
        print("Reading Physics Book")


# print(issubclass(Physics, Book))  # True

topon = Physics("Topon")

# print(isinstance(topon, Physics))  # True
# print(isinstance(topon, Book))  # True

topon.read()
