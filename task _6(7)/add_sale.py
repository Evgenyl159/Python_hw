import os
import sys


def add_sale():
    price = sys.argv[1]
    if price.isdigit():
        with open('bakery.csv', 'a', encoding='utf-8') as f:
            f.write(price + '\n')
    else:
        print('недопустимый формат')
        sys.exit()


add_sale()
