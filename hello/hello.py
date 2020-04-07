from tkinter import *


def hello1(name):
    print('Hello %s!' % name)


def hello2():
    name = input('Who are you?\n')
    print('Hello %s!' % name)


def hello3(name):
    root = Tk()
    lb = Label(root, text='Hello %s!' % name)
    lb.pack()
    root.mainloop()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def plus(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == '__main__':
    x = add(1, 2)
    print(x)
