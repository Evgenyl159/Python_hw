from abc import ABC, abstractmethod


class Gear(ABC):
    def __init__(self, count):
        self.count = count

    @property
    @abstractmethod
    def expenses(self):
        pass

    def __add__(self, other):
        return round(self.expenses + other.expenses, 2)


class Palt(Gear):

    @property
    def expenses(self):
        return (self.count / 6.5) + 0.5


class Costume(Gear):

    @property
    def expenses(self):
        return (2 * self.count + 0.3) / 100


a = Palt(200)
b = Costume(500)

print(a + b)