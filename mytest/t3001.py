import os
import sys

from t3002 import *
from mytest import root
from hello.hello import *


def load():
    os.getcwd()
    print(os.path.realpath('com/hh/ft'))
    # with open('resources/data_001.txt') as file:
    #     data = file.read()
    #     print(data)


if __name__ == '__main__':
    # load()
    print(maxz(1, 3))
    print(root)
    print(add(1, 4))
