import random
from functools import wraps


def generate_check_code():
    value1 = random.randint(1000, 2000)
    value2 = random.randint(2000, 9999)
    value3 = random.randint(value1, value2)
    return value3


def decorator_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in args:
            print(f'{func.__name__}({i}: {type(i)})')
        for k, v in kwargs.items():
            print(f'{func.__name__}({k} = {v}: {type(k)} {type(v)})')
        result = func(*args, **kwargs)
        print(type(result))
        return result

    return wrapper


@decorator_function
def luna(one, two, three, random_digits):
    control_sum = 0
    string_card = str(one) + str(two) + str(three) + str(random_digits)
    if len(string_card) != 16:
        return False, 'Не верный формат'
    card_nums = list(map(int, string_card))
    for count, num in enumerate(card_nums):
        if count % 2 == 0:
            check = num * 2
            if check > 9:
                check -= 9
            control_sum += check
        else:
            control_sum += num
    return control_sum % 10 == 0, string_card


a = luna(4276, '0800', 2534, generate_check_code())
if a[0]:
    print(f'{a[1]}  - карта существует')
else:
    print(f'{a[1]}  - карта не существует')
print(luna.__name__)