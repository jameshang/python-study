def add(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    c = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    return c


def sub(a, b):
    c = a - b
    return c


def div(a, b):
    c = 0
    if b != 0:
        c = a / b
    return c


if __name__ == '__main__':
    c1 = add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    c2 = sub(89, 77)
    print(c1 * c2)
    c3 = div(1, 2)
    print(c3)