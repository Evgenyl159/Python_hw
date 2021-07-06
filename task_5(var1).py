from bs4 import BeautifulSoup
import requests
from random import randint

user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/91.0.4472.124 Safari/537.36 '


def generator_ip_100():
    for n in range(100):
        a = randint(0, 255)
        b = randint(0, 255)
        c = randint(0, 255)
        d = randint(0, 255)
        f = open('test_ip.txt', 'a', encoding='utf-8')
        f.write(str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d) + '\n')
        f.close()


def get_names():
    url = 'https://randomus.ru/name?type=0&sex=10&count=100'  # count - количество полученных ФИО
    r_get = requests.get(url=url, headers={'User-Agent': user_agent_val})
    full_text = r_get.text
    soupe = BeautifulSoup(full_text)
    search_info = soupe.findAll('div', {'class': 'tags copy_button'})
    for item in search_info:
        check_name = item.text
        test = str(check_name).replace("\n", "")
        x = open('test_name.txt', 'a', encoding='utf-8')
        x.write(test + '\n')
        x.close()


generator_ip_100()
get_names()


def slipper():
    while True:
        try:
            first = input('Введи первый файл')
            check = open(first, 'r')
            check.close()
            break
        except FileNotFoundError as e:
            print(f'Неправильное название файла')
    while True:
        try:
            second = input('Введи Второй файл')
            check1 = open(second, 'r')
            check1.close()
            break
        except FileNotFoundError as e:
            print(f'Неправильное название файла')
    while True:
        try:
            output_file = input('Введи выходной файл')
            check2 = open(output_file, 'w')
            check2.close()
            break
        except Exception:
            print('error')

    with open(f"{first}", 'r', encoding='utf-8') as f, open(f"{second}", 'r', encoding='utf-8') as h, open(
            f"{output_file}", 'a', encoding='utf-8') as lines:
        for name in f:
            ip = h.readline()
            stat = name.replace('\n', '')
            lines.write(f'{stat} : {ip}')


# slipper()

def print_menu():
    print('---------меню---------')
    print('Пример:\ntest_ip.txt\ntest_name.txt\nlist_ip.txt')


if __name__ == '__main__':
    print_menu()
    generator_ip_100()
    get_names()
    slipper()