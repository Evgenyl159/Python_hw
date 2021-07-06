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
print('success')