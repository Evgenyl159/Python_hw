import requests
from bs4 import BeautifulSoup

user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/91.0.4472.124 Safari/537.36 '


def get_names():
    url = 'https://randomus.ru/name?type=0&sex=10&count=100'  # count - количество полученных ФИО
    list_name = []
    r_get = requests.get(url=url, headers={'User-Agent': user_agent_val})
    full_text = r_get.text
    soupe = BeautifulSoup(full_text)
    search_info = soupe.findAll('div', {'class': 'tags copy_button'})
    for item in search_info:
        check_name = item.text
        test = str(check_name).replace(' ', ',')
        list_name.append(test.replace("\n", ''))
    return list_name


def get_hooby():
    url_hobby = 'https://habr.com/ru/post/404969/'
    list_hobby = []
    r_get_hobby = requests.get(url=url_hobby)
    full_text = r_get_hobby.text
    soupe = BeautifulSoup(full_text)
    table_hobby = soupe.find('div', {'id': 'post-content-body'}).findAll('h2')
    for i in table_hobby:
        list_hobby.append(i.text)
    return list_hobby


hobbys = (get_hooby())
names = (get_names())
with open('check_names.csv', 'w') as f_names:
    for name in names:
        f_names.write(name + '\n')
with open('check_hobby.csv', 'w') as f_hobby:
    for hobby in hobbys:
        f_hobby.write(hobby + '\n')

with open('check_names.csv', 'r') as f, open('check_hobby.csv', 'r') as h:
    count_f = f.readlines()
    count_h = h.readlines()
    f.seek(0), h.seek(0)
    if len(count_f) > len(count_h):
        dict_test = {k.replace('\n', ''): None for k in f}
        for i in dict_test:
            dict_test[i] = h.readline().replace('\n', '')
        print('success')

        with open('dict_names+hobby.txt', 'w', encoding='cp1251') as d:
            for k, v in dict_test.items():
                if v == '':
                    d.write(f'{k}: {None}\n')
                else:
                    d.write(f'{k}:  {v}\n')
    else:
        print('Не подходящее значение\nCode: 1')

with open('check_names.csv', 'r') as f, open('check_hobby.csv', 'r') as h, open('task4_test.txt', 'w') as check:
    for item in f:
        hb = h.readline()
        if hb == '':
            check.write(item.replace("\n", " : ") + 'None\n')
        else:
            check.write(item.replace("\n", " : ") + hb.replace("n", ""))