import requests
import collections
import time

start_time = time.time()
url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
r_get = requests.get(url=url, headers={'User-Agent': user_agent_val})
data = r_get.text
z = open('random_name', 'w')
z.write(data), z.close()
list_ip = []
with open('random_name', 'r') as f:
    for line in f:
        check = line.split(' ')
        list_ip.append((check[0], check[5].replace('"', ''), check[6]))
collect = collections.Counter()
for ip in list_ip:
    collect[ip[0]] += 1
search_value = max(collect.values())
for k, v in collect.items():
    if v == search_value:
        print(f'ip спамера: {k}\nколичество запросов: {v}')
print(f'Время обработки с запросом на файл: {(time.time() - start_time)}')
print ('\nВыведены не все значения из списка, чтобы не засорять консоль:')
for i in range(0, 10):
    print(list_ip[i])
# print(list_ip) # Чтобы вывести весь список
