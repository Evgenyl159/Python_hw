import requests
import re
import time

start_time = time.time()
url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
r_get = requests.get(url=url, headers={'User-Agent': user_agent_val})
data = r_get.text
z = open('random_name.txt', 'w')
z.write(data), z.close()
q = open('parsed_raw.txt', 'w')
q.close()
with open('parsed_raw.txt', 'a', encoding='utf-8') as n, open('random_name.txt', 'r') as f:
    for line in f:
        ip = re.findall(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}|(?:\w+:+){4,8}\w+', line) # 2001:4801:7824:102:8bee:6e66:ff10:6aa2
        data = re.findall(r'(?:\d{1,2}/\w+/\d{4}:\d{2}:\d{2}:\d{2}.\+\d{4})', line)
        path = re.findall(r'(?:\w{2,4})(?:\s/\w+/\w+)', line)
        digit = re.findall(r"(?:\s(\d{2,4})\s(\d{1,9})\s)", line)
        for item in digit:
            digit1 = item[0]
            digit2 = item[1]
        split_path = path[0].split(' ')
        final = (ip[0], data[0], split_path[0], split_path[1], digit1, digit2)
        n.write(f'{final}\n')
    print('success')