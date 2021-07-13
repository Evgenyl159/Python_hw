import re


def email_parse(email):
    valid_data = {'username': None, 'domain': None}
    result = re.findall(r'^(\w+[._\w+]\w+)@\w+\.\D{2,3}$', email)
    if result:
        valid_data['username'] = re.findall(r'^(\w+.\w+)@', email)
        valid_data['domain'] = re.findall(r'(\w+\.\D{2,3})', email)
        print(valid_data)
    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


email_parse('somon_4224e@geekbrains.ru')