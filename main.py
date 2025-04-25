from tkinter import *

window = Tk()
window.geometry("500x500")

e = Entry(window, width=54, borderwidth=5)
e.place(x=0, y=0)

def bckspc():
    curnt = e.get()
    e.delete(0, END)
    e.insert(0, curnt[:-1])

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

def add():
    try:
        n1 = e.get()
        global math
        math = "addition"
        global i
        i = float(n1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid input")

def subtract():
    try:
        n1 = e.get()
        global math
        math = "subtraction"
        global i
        i = float(n1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid input")

def divide():
    try:
        n1 = e.get()
        global math
        math = "division"
        global i
        i = float(n1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid input")

def multiply():
    try:
        n1 = e.get()
        global math
        math = "multiplication"
        global i
        i = float(n1)
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid input")

def eql():
    try:
        n2 = float(e.get())
        e.delete(0, END)
        if math == "addition":
            result = i + n2
        elif math == "subtraction":
            result = i - n2
        elif math == "division":
            if n2 == 0:
                e.insert(0, "Cannot divide by 0")
                return
            result = i / n2
        elif math == "multiplication":
            result = i * n2
        r_r = round(result, 4)
        if r_r == int(r_r):
            e.insert(0, int(r_r))
        else:
            e.insert(0, r_r)

    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid input")


def clr():
    e.delete(0, END)

b = Button(window, text="1", width=5, command=lambda: click(1))
b.place(x=10, y=60)
b = Button(window, text="2", width=5, command=lambda: click(2))
b.place(x=170, y=60)
b = Button(window, text="3", width=5, command=lambda: click(3))
b.place(x=330, y=60)
b = Button(window, text="4", width=5, command=lambda: click(4))
b.place(x=10, y=120)
b = Button(window, text="5", width=5, command=lambda: click(5))
b.place(x=170, y=120)
b = Button(window, text="6", width=5, command=lambda: click(6))
b.place(x=330, y=120)
b = Button(window, text="7", width=5, command=lambda: click(7))
b.place(x=10, y=180)
b = Button(window, text="8", width=5, command=lambda: click(8))
b.place(x=170, y=180)
b = Button(window, text="9", width=5, command=lambda: click(9))
b.place(x=330, y=180)
b = Button(window, text="0", width=5, command=lambda: click(0))
b.place(x=170, y=240)
b = Button(window, text="×", width=5, command=multiply)
b.place(x=90, y=300)
b = Button(window, text="÷", width=5, command=divide)
b.place(x=250, y=300)
b = Button(window, text="+", width=5, command=add)
b.place(x=90, y=360)
b = Button(window, text="-", width=5, command=subtract)
b.place(x=250, y=360)
b = Button(window, text="clear", width=5, command=clr)
b.place(x=10, y=420)
b = Button(window, text="=", width=5, command=eql)
b.place(x=330, y=420)
b = Button(window, text=".", width=5, command=lambda: click("."))
b.place(x=10, y=240)
b = Button(window, text="⌫", width=5, command=bckspc)
b.place(x=330, y=240)

mainloop()