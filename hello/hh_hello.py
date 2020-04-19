def add(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    c = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    return c


def sub(a, b):
    c = a - b
    return c


def sub1(a, b):
    if a == 1:
        return 10
    elif a == 2:
        return 20
    elif a == 3:
        return 30
    else:
        return 100


def div(a, b):
    c = 0
    if b != 0:
        c = a / b
    return c


def hello(name):
    if name == "hanson":
        print("hello " + name)
    else:
        print("hi " + name)


def add1(a, b, c):
    return a + b + c


if __name__ == '__main__':
    hello("james")
