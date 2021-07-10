import os
import yaml
import random


def create_folders(path_):
    if not os.path.exists(path_):
        os.mkdir(path_)
    else:
        print(f'{path_} уже существует')


def check_value(value_):
    if type(value_) == str:
        check_val = str(value_).split('.')
        if check_val[1] != '':
            with open(f'{check_val[0]}.{check_val[1]}', 'w+') as a:
                for i in range(10, random.randint(5, 500)):
                    line = str(random.randint(111, 777))
                    a.write(line)
    elif type(value_) == dict:
        for folder in value_:
            create_folders(folder)
            search_info_dict(value_)
    else:
        print('не верный формат')


def search_info(dict_direct):
    for key in dict_direct:
        create_folders(key)
        os.chdir(key)
    values = dict_direct.values()
    for val_list in values:
        for val in val_list:
            check_value(val)
    os.chdir(main_folder)


def search_info_dict(dict_direct):
    for key in dict_direct:
        os.chdir(key)
    values = dict_direct.values()
    for val_list in values:
        for val in val_list:
            check_value(val)
    os.chdir(main_folder)


with open('config.yaml', 'r') as f:
    full_text = yaml.safe_load(f)
    for item in full_text:
        for need_folder in item:
            create_folders(need_folder)
            os.chdir(need_folder)
            main_folder = (os.getcwd())
            for folders in item.values():
                for folder in folders:
                    search_info(folder)