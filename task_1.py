import os

folders = {'--my_project': ['--settings', '--mainapp', '--adminapp', '--authapp']}


def create_folders(path_):
    if not os.path.exists(path_):
        os.mkdir(path_)
    else:
        print(f'{path_} уже существует')


def build(data):
    if data:
        for d in data:
            create_folders(d)
            os.chdir(d)
            for item_list in dict(data).values():
                for item in item_list:
                    if not os.path.exists(item):
                        os.mkdir(item)
                    else:
                        print(f'{item} уже существует')


build(folders)