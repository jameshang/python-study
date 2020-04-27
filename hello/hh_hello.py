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
    k = add2(a, b)
    p = add2(k, c)
    return p


def add2(a, b):
    c = a + b
    return c


def fun1(a, b, c, d):
    x = a + b
    if x > c:
        y = x * d
    elif x < c:
        y = x / d
    else:
        y = d
    return y


def add3(a):
    c = 0
    for i in range(2, 11):
        c = c + a
        if i < 9:
            print(a + a + a + a + a + a + a)
        print(i)
    return c


def loop1(a):
    for i in range(12, 23):
        if 2 + 11 < i < 6 + 22:
            print(i)


if __name__ == '__main__':
    loop1(1)

