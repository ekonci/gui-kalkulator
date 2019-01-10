import Tkinter
import tkMessageBox

window = Tkinter.Tk()

x_ask = Tkinter.Label(window, text="Vnesi x: ")
x_ask.pack()

x = Tkinter.Entry(window)
x.pack()

y_ask = Tkinter.Label(window, text="Vnesi y: ")
y_ask.pack()

y = Tkinter.Entry(window)
y.pack()

operacija_ask = Tkinter.Label(window, text="Vnesi operacijo (+, -, *, /): ")
operacija_ask.pack()

operacija = Tkinter.Entry(window)
operacija.pack()

def check_guess():
    if operacija.get() == "+":
        result_text = int(x.get()) + int(y.get())
    elif (operacija.get()) == "-":
        result_text = int(x.get()) - int(y.get())
    elif operacija.get() == "*":
        result_text = int(x.get()) * int(y.get())
    elif operacija.get() == "/":
        result_text = int(x.get()) / int(y.get())
    else:
        result_text = "PRISLO JE DO NAPAKE"

    tkMessageBox.showinfo("Result", result_text)

# submit button
submit = Tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()


window.mainloop()
