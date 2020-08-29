from tkinter import *


def add():
    num = int(e1.get()) + int(e2.get())
    cal.set(num)
    Entry(root, text="%s" % cal).grid(row=2, column=1)


root = Tk()
root.title('Mark PLC 2')
cal = StringVar()
Label(root, text='First: ').grid(row=0, sticky=W)
Label(root, text='Second: ').grid(row=1, sticky=W)
Label(root, text='Result: ').grid(row=2, sticky=W)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

b = Button(root, text='Calculate', bg='blue', fg='white', activebackground='black', activeforeground='blue',
           command=add)
b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)
c = Button(root, text='Quit', bg='red', fg='white', activebackground='white', activeforeground='red', command=root.quit)
c.grid(row=2, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

mainloop()
