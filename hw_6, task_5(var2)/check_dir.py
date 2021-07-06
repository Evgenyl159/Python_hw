import os
import sys


def check_dir():
    print(f'{os.getcwd()}\n{os.listdir()}')


check_dir()
