import sys


def show_price():
    if len(sys.argv) == 2:
        with open('bakery.csv', 'r', encoding='utf-8') as z:
            try:
                for line_s, lines_text in enumerate(z, start=1):
                    rep_text = str(lines_text).replace('\n', '')
                    if rep_text == sys.argv[1]:
                        search_index = line_s
                        break
                    else:
                        continue
                z.seek(0)
                for line_n, line in enumerate(z, start=1):
                    if line_n >= search_index:
                        print(line.replace('\n', ''))
            except UnboundLocalError as e:
                print(f'значение: {sys.argv[1]} не найдено\n')
    elif len(sys.argv) == 3:
        with open('bakery.csv', 'r', encoding='utf-8') as n:
            start = 0
            stop = 0
            for line_n, line in enumerate(n, start=1):
                check_index = str(line).replace('\n', '')
                if check_index == sys.argv[1]:
                    start = line_n
                if check_index == sys.argv[2]:
                    stop = line_n
            n.seek(0)
            for lns_num, line_txt in enumerate(n, start=1):
                if start <= lns_num <= stop:
                    print(str(line_txt).replace('\n', ''))
                else:
                    continue

    elif len(sys.argv) == 1:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                print(line.replace('\n', ''))

    else:
        print('некорректный ввод параметров')


show_price()
