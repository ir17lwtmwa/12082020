from tkinter import *


def printName():
    let = e.get()
    print(let)


root = Tk()
root.title('Mark PLC 1')
Label(root, text='Welcome!').grid(row=0, sticky=W)
Label(root, text='Please enter name below to create account.').grid(row=1, sticky=W)
Label(root, text='Account Holder Name: ').grid(row=2, sticky=W)
result = Label(root, text='', textvariable="txt.txt").grid(row=4)

e = Entry(root)

e.grid(row=2, column=1)

b = Button(root, text='Done', fg='white', bg='blue', activebackground='black', activeforeground='blue',
           command=printName)
b.grid(row=3, column=1, sticky=E)


mainloop()
