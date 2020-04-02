from tkinter import *


def timetable():
    root = Tk()
    root.title('Timetable')
    root.geometry('400x300+400+200')
    root.maxsize(640, 480)
    root.minsize(400, 300)
    ld1 = ['AM1', 'AM2', 'AM3']
    ld2 = ['PM1', 'PM2', 'PM3']
    l1 = Listbox(root)
    l2 = Listbox(root)
    for d in ld1:
        l1.insert(0, d)
    for d in ld2:
        l2.insert(0, d)
    l1.pack()
    l2.pack()
    root.mainloop()


if __name__ == '__main__':
    timetable()
