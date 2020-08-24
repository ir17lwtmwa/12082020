from tkinter import *
var = " "


def entry(num):
    global var
    var = var + str(num)
    equ.set(var)


def answer():
    try:
        global var
        result = str(eval(var))
        equ.set(result)
        var = " "
    except:
        equ.set("Error")
        var = " "


def delete():
    global var
    var = " "
    equ.set(" ")


if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light blue")
    root.title("GUI Calculator")
    root.geometry("235x150")
    equ = StringVar()
    free_box = Entry(root, textvariable=equ)
    free_box.grid(columnspan=5, ipadx=50)
    equ.set('0')
    b1 = Button(root, text=' 1 ', fg='white', bg='black', command=lambda: entry(1), height=1, width=7)
    b1.grid(row=2, column=0)
    b2 = Button(root, text=' 2 ', fg='white', bg='black', command=lambda: entry(2), height=1, width=7)
    b2.grid(row=2, column=1)
    b3 = Button(root, text=' 3 ', fg='white', bg='black', command=lambda: entry(3), height=1, width=7)
    b3.grid(row=2, column=2)
    b4 = Button(root, text=' 4 ', fg='white', bg='black', command=lambda: entry(4), height=1, width=7)
    b4.grid(row=3, column=0)
    b5 = Button(root, text=' 5 ', fg='white', bg='black', command=lambda: entry(5), height=1, width=7)
    b5.grid(row=3, column=1)
    b6 = Button(root, text=' 6 ', fg='white', bg='black', command=lambda: entry(6), height=1, width=7)
    b6.grid(row=3, column=2)
    b7 = Button(root, text=' 7 ', fg='white', bg='black', command=lambda: entry(7), height=1, width=7)
    b7.grid(row=4, column=0)
    b8 = Button(root, text=' 8 ', fg='white', bg='black', command=lambda: entry(8), height=1, width=7)
    b8.grid(row=4, column=1)
    b9 = Button(root, text=' 9 ', fg='white', bg='black', command=lambda: entry(9), height=1, width=7)
    b9.grid(row=4, column=2)
    b0 = Button(root, text=' 0 ', fg='white', bg='black', command=lambda: entry(0), height=1, width=7)
    b0.grid(row=5, column=1)
    add = Button(root, text=' + ', fg='white', bg='black', command=lambda: entry("+"), height=1, width=7)
    add.grid(row=2, column=3)
    subtract = Button(root, text=' - ', fg='white', bg='black', command=lambda: entry("-"), height=1, width=7)
    subtract.grid(row=3, column=3)
    prod = Button(root, text=' * ', fg='white', bg='black', command=lambda: entry("*"), height=1, width=7)
    prod.grid(row=4, column=3)
    div = Button(root, text=' / ', fg='white', bg='black', command=lambda: entry("/"), height=1, width=7)
    div.grid(row=5, column=3)
    ans = Button(root, text=' = ', fg='white', bg='black', command=answer, height=1, width=7)
    ans.grid(row=5, column=2)
    ac = Button(root, text=' AC ', fg='white', bg='red', command=delete, height=1, width=7)
    ac.grid(row=6, column=0)
    point = Button(root, text=' . ', fg='white', bg='black', command=lambda: entry("."), height=1, width=7)
    point.grid(row=5, column=0)
    root.mainloop()
