from tkinter import *
import time
import _thread
import math


def draw_line(c: Canvas):
    time.sleep(2)
    for i in range(0, 100, 2):
        time.sleep(0.2)
        xn = i
        yn = i
        c.create_line(0, xn, 100, yn)
        print('Draw line xn=%d, yn=%d' % (xn, yn))


def draw_circle(c: Canvas):
    if c is not None:
        time.sleep(2)
    r = 50
    rr = math.pow(r, 2)
    x0 = 100
    y0 = 100
    for i in range(-r, r + 1):
        time.sleep(0.1)
        xn = i
        yn = math.sqrt(rr - math.pow(xn, 2))
        c.create_line(x0, y0, xn + x0, yn + y0)
        c.create_line(x0, y0, xn + x0, -yn + y0)
        print('Draw circle xn=%d, yn=%d' % (xn, yn))


def draw():
    root = Tk()
    c = Canvas(root, width=400, height=300)
    c.pack()
    # _thread.start_new_thread(draw_line, (c,))
    _thread.start_new_thread(draw_circle, (c,))
    root.mainloop()


if __name__ == '__main__':
    draw()
    # draw_circle(None)
