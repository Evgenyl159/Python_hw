import os
import json
import yaml
import shutil
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
        for need in item:
            create_folders(need)
            os.chdir(need)
            main_folder = (os.getcwd())
            for folders in item.values():
                for folder in folders:
                    search_info(folder)


def get_templates_task3():
    folder_html = '--templates'
    create_folders(folder_html)
    os.chdir(folder_html)
    tepmplates_dir = (os.getcwd())
    os.chdir(main_folder)
    for dirpath, dirnames, filenames in os.walk(main_folder):
        for filename in filenames:
            check_file = str(filename).split('.')
            if check_file[1] == 'html':
                test = os.path.join(dirpath, filename)
                try:
                    shutil.copy(test, tepmplates_dir)
                except shutil.SameFileError:
                    pass
    print('success')


def check_tuple(file, root):
    medium_dict = {}
    size = os.stat(os.path.join(root, file)).st_size
    check = str(file).split('.')
    medium_dict[size] = check[1]
    return medium_dict


def check_dict(dict_test, list100, list1000, list10000, list100000):
    dict_check = {}
    for key in dict(dict_test).items():
        if key[0] == 100:
            dict_check[key[0]] = (key[1], list100)
        elif key[0] == 1000:
            dict_check[key[0]] = (key[1], list1000)
        elif key[0] == 10000:
            dict_check[key[0]] = (key[1], list10000)
        else:
            dict_check[key[0]] = (key[1], list100000)
    return dict_check


def get_unique_val(list_val):
    list_of_unique_values = []
    unique_val = set(list_val)

    for number in unique_val:
        list_of_unique_values.append(number)

    return list_of_unique_values


def size_obj_task4_5(folder_name):
    if os.path.exists(folder_name) or folder_name == '--my_project':
        print(folder_name)
        if folder_name == '--my_project':
            search = '.'
        else:
            search = folder_name
        dir_sizes = {}
        main_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}
        count = 0
        size = 0
        list100 = []
        list1000 = []
        list10000 = []
        list100000 = []
        for root, dirs, files in os.walk(search, topdown=False):
            size = sum(os.path.getsize(os.path.join(root, f)) for f in files)
            for z in files:
                test_val = check_tuple(z, root)
                for key_size in test_val:
                    for i in main_dict:
                        if key_size < i:
                            main_dict[i] = main_dict[i] + 1
                            if i == 100:
                                list100.append(test_val[key_size])
                            elif i == 1000:
                                list1000.append(test_val[key_size])
                            elif i == 10000:
                                list10000.append(test_val[key_size])
                            else:
                                list100000.append(test_val[key_size])
                            break
                        else:
                            continue
            size += sum(dir_sizes[os.path.join(root, d)] for d in dirs)
            count = count + len(files)
            dir_sizes[root] = size
        uniq_list100 = get_unique_val(list100)
        uniq_list1000 = get_unique_val(list1000)
        uniq_list10000 = get_unique_val(list10000)
        uniq_list100000 = get_unique_val(list100000)
        data = (check_dict(main_dict, uniq_list100, uniq_list1000, uniq_list10000, uniq_list100000))
        print(dir_sizes)
        with open(f'{folder_name}_summary.json', 'w', encoding='utf-8') as q:
            q.write(json.dumps(data))
    else:
        print('папка не существует')


get_templates_task3()
size_obj_task4_5('--mainapp')
