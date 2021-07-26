class My_error(Exception):

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def __str__(self):
        if self.val2 == 0:
            return 'на ноль делить нельзя'
        else:
            return repr(self.val1 / self.val2)


try:
    val_1 = int(input('первое число'))
    val_2 = int(input('второе число'))
    if val_2 == 0:
        raise My_error(val_1, val_2)
    else:
        print(val_1 / val_2)
except My_error as e:
    print(e)
except ValueError as v:
    print(v)