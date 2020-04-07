from tkinter import *
from tkinter import ttk
import time
import _thread
import math

c: Canvas
drawing = False


def draw_line():
    c.delete(ALL)
    for i in range(0, 100, 2):
        time.sleep(0.2)
        xn = i
        yn = i
        c.create_line(0, xn, 100, yn)
        print('Draw line xn=%d, yn=%d' % (xn, yn))
    global drawing
    drawing = False


def do_draw_line():
    global drawing
    if drawing:
        return
    drawing = True
    _thread.start_new_thread(draw_line, ())


def draw_circle():
    c.delete(ALL)
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
    global drawing
    drawing = False


def do_draw_circle():
    global drawing
    if drawing:
        return
    drawing = True
    _thread.start_new_thread(draw_circle, ())


def draw():
    root = Tk()
    root.title('My Canvas')
    f1 = Frame(root, bd=1, bg='grey', relief='raised')
    f1.pack(side=LEFT)
    ttk.Button(f1, text='Draw Line', command=do_draw_line).pack()
    ttk.Button(f1, text='Draw Circle', command=do_draw_circle).pack()
    f2 = Frame(root, bd=1, relief='raised')
    f2.pack(side=RIGHT)
    global c
    c = Canvas(f2, width=400, height=300)
    c.pack()
    root.mainloop()


if __name__ == '__main__':
    draw()
