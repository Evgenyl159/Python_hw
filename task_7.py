class Complex_digit:
    def __init__(self, digit):
        try:
            self.digit = int(digit)
        except ValueError:
            print('недопустимый формат')

    def __add__(self, other):
        return self.digit + other.digit

    def __sub__(self, other):
        return self.digit * other.digit


first = Complex_digit(100)
second = Complex_digit(200)
print(first.__add__(second))
print(first.__sub__(second))