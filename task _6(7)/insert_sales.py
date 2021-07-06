import sys


def insert_sales():
    if len(sys.argv) == 3:
        with open('help_log.txt', 'w', encoding='utf-8') as ts:
            ts.write('')
        with open('bakery.csv', 'r', encoding='utf-8') as f, open('help_log.txt', 'r+', encoding='utf-8') as ts:
            for line in f:
                ts.write(line)
        with open('bakery.csv', 'w', encoding='utf-8') as f, open('help_log.txt', 'r+', encoding='utf-8') as ts:
            need_index = sys.argv[1]
            new_value = sys.argv[2]
            for index_line, value in enumerate(ts, start=1):
                if index_line == int(need_index):
                    f.write(new_value + '\n')
                else:
                    f.write(value)
        with open('help_log.txt', 'w', encoding='utf-8') as ts:
            print('success')

    else:
        print('Недопустимое значение')


insert_sales()
