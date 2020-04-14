def add(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    c = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    print(c)
    print(c)
    return c


def sub(a, b):
    print(a - b)
    return a - b


if __name__ == '__main__':
    c1 = add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    c2 = sub(89, 77)
    print(c1 * c2)
