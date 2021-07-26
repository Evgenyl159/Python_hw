import re


class My_error(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if type(self.value) == str:
            return 'недопустимый эллемент списка'
        else:
            pass


def check_list():
    control_list = []
    print('для выхода из программы : stop')
    while True:
        try:
            user_input = input('Введите число')
            if re.compile(r'^-\d+$').match(user_input):
                control_list.append(user_input)
            elif re.compile(r'^\d+$').match(user_input):
                control_list.append(user_input)
            elif user_input == 'stop':
                break
            else:
                raise My_error(user_input)
        except My_error as e:
            print(e)
        except ValueError as v:
            print(v)
    print(control_list)


check_list()