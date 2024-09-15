import os
import shutil

main_folder = (os.getcwd())

def create_folders(path_):
    if not os.path.exists(path_):
        os.mkdir(path_)
    else:
        print(f'{path_} уже существует')


def get_templates_task3():
    folder_html = '--templates'
    create_folders(folder_html)
    os.chdir(folder_html)
    tepmplates_geo = (os.getcwd())
    os.chdir(main_folder)
    for dirpath, dirnames, filenames in os.walk(main_folder):
        for filename in filenames:
            check_file = str(filename).split('.')
            if check_file[1] == 'html':
                test = os.path.join(dirpath, filename)
                try:
                    shutil.copy(test, tepmplates_geo)
                except shutil.SameFileError:
                    pass
    print('success')