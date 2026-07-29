# readonly --> can not set the value or changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private attribute.

class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    # getter without any setter is readonly attribute
    @property  # method to attribute convert
    def age(self):
        return self._age

    # getter
    @property
    def salary(self):
        return self.__money

    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return "Salary is negative"
        else:
            self.__money += value


sunny = User("Sunny", 21, 12000)

# print(sunny.__money) # it's private

# print(sunny.age())  # not callable - it's attribute
print(sunny.age)  # attribute call

print(sunny.salary)

# sunny.salary = 28000 #  property 'salary' of 'User' object has no setter

sunny.salary = 28000  # now it's setter

print(sunny.salary)
