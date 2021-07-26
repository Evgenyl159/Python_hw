class Cell:

    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        check = self.count - other.count
        if check > 0:
            return check
        else:
            return 'Недопустимое значение'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        try:
            check = self.count // other.count
            return check
        except ZeroDivisionError:
            print('недопустимое значение')

    def make_order(self, rows):
        return '\n'.join(['*' * rows for i in range(self.count // rows)]) + '\n' + '*' * (self.count % rows)


a = Cell(50)
b = Cell(35)
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(a.__truediv__(b))

print(a.make_order(7))
