from math import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *


h = 0.005
a = 0
b = 0.5
y0 = 0
x0=0.1
funcText = ''

mylist = None
functionLabelValue = None
errorLabel = None

def func(x, y):
    return eval(funcText)


def solv(a, b, h, y0, x0):
    x = np.arange(a + h, b + h, h)
    y = []
    y.append(y0)
    global mylist
    global functionLabelValue
    if (mylist):
        mylist.destroy()
    if (functionLabelValue):
        functionLabelValue.destroy()

    for xn, n in zip(x, range(len(x))):
        f1 = func(xn, y[n])
        f2 = func(xn + h / 2, y[n] + (h / 2) * f1)
        f3 = func(xn + h, y[n] - h * f1 + 2 * h * f2)
        y.append(y[n] + (h / 6) * (f1 + 4 * f2 + f3))

    x = x.tolist()
    x.insert(0, 0)
    plt.plot(x, y)
    plt.tick_params(length=4, width=2, labelsize=10)
    r = [i for i in np.arange(0, 1.5, 0.1)]
    plt.yticks(r)
    plt.xticks(r)
    plt.grid(True)
    plt.show(block= FALSE)
    mylist = Listbox(window, yscrollcommand = scrollbar.set )
    for i, j in zip(x, y):
        mylist.insert(END, f'x: {round(i, 5)}; y: {round(j, 5)}')
    mylist.pack()
    scrollbar.config( command = mylist.yview )

    funcValue = round(y[int((x0 - a) * (1 / h))], 5)
    functionLabelValue = Label(text=f'F(x)={funcValue}')
    functionLabelValue.pack()
    return round(y[int((x0 - a) * (1 / h))], 5)

window = Tk()
window.title('Runge–Kutta method')
window.geometry("300x500")
scrollbar = Scrollbar(window)
scrollbar.pack( side = 'right', fill = 'y')

functionLabel = Label(text='Enter function: ')
functionValue = Entry(window)

functionLabel.pack()
functionValue.pack()

startPointLabel = Label(text='Enter start point (a): ')
startPointValue = Entry(window)

startPointLabel.pack()
startPointValue.pack()

endPointLabel = Label(text='Enter end point (b): ')
endPointValue = Entry(window)

endPointLabel.pack()
endPointValue.pack()

startLabel = Label(text='Enter start value (y0): ')
startValue = Entry(window)

startLabel.pack()
startValue.pack()

def submitForm():
    global errorLabel
    if(errorLabel):
        errorLabel.destroy()
    if (mylist):
        mylist.destroy()
    if (functionLabelValue):
        functionLabelValue.destroy()
    global a
    global b
    global y0
    try:
        global funcText
        funcText = functionValue.get()
        try:
            a = float(startPointValue.get())
            b = float(endPointValue.get())
            y0 = float(startValue.get())
        except:
            errorLabel = Label(text='ValueError: could not convert string to float', fg='red')
            errorLabel.pack()
            return None
        global h
        global func
        if (a >= b):
            errorLabel = Label(text='BordersError: (a) has to be less than (b)', fg='red')
            errorLabel.pack()
            return None
        solv(a, b, h, y0, 0.1)
    except:
        errorLabel = Label(text='ValueFunction: invalid function ', fg='red')
        errorLabel.pack()



submitButton = Button(window, text='calculate',highlightbackground='#3E4149', command=submitForm)
submitButton.pack()

window.mainloop()
