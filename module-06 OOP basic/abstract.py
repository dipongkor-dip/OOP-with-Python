# abstract base class ~ abc

import abc

from abc import abstractmethod


class Animal(abc.ABC):
    @abc.abstractmethod  # enforce all derived class to have a eat method
    def eat(self):
        print("Animal Eating")

    # alternative import system
    @abstractmethod
    def move(self):
        print("Animal Moving")


class Monkey(Animal):
    def __init__(self, name):
        self.category = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        return super().eat()

    def move(self):
        return super().move()


lucky = Monkey("lucky")

lucky.eat()


# interview question: comparison interfaces and abstract classes
