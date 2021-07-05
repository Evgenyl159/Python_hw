import sys


def check_input():
    print('{1 файл на чтение} {2 файл на чтение} {3 куда записываем}')
    user_args = sys.argv[1:]
    first, second, output = user_args
    try:
        check = open(first, 'r')
        check.close()
    except FileNotFoundError as e:
        print(f'Неправильное название файла\nвыход из программы')
        sys.exit()
    try:
        check1 = open(second, 'r')
        check1.close()
    except FileNotFoundError as e:
        print(f'Неправильное название файла\nвыход из программы')
        sys.exit()
    try:
        check2 = open(output, 'w')
        check2.close()
    except Exception:
        print('не правильный формат', Exception)
        sys.exit()
    return first, second, output


def slipper(fir, sec, out):
    with open(f"{fir}", 'r', encoding='utf-8') as f, open(f"{sec}", 'r', encoding='utf-8') as h, open(
            f"{out}", 'a', encoding='utf-8') as wr:
        for name in f:
            ip = h.readline()
            stat = name.replace('\n', '')
            wr.write(f'{stat} : {ip}')
        return 'success'


f, s, o = check_input()
print(slipper(f, s, o))
