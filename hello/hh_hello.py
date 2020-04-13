def plus(a, b, c):
    return a * b * c


def add(a, b):
    res = 0
    for i in range(a, b + 1):
        res = res + i
    return res


def test1(p1,p2):
    a = 1
    a = 2
    a = 3
    b = 1
    b = 2
    a = b
    b = 3
    print(a)
    print(b)
    print(p1)
    print(p2)

if __name__ == '__main__':
    test1(3,5)

