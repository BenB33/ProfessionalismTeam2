from tkinter import *

form = Tk()
form.title("Calculator")

entry = Entry(form, width=35, borderwidth=3)
entry.grid(row=0, columnspan=3, padx=10, pady=10)

def buttonAdd(number):
    entry.delete(0, END)
    entry.insert(0, number)

# Define number buttons
btn1 = Button(form, text="1", padx=30, pady=15, command=lambda: buttonAdd(1))
btn2 = Button(form, text="2", padx=30, pady=15, command=lambda: buttonAdd(2))
btn3 = Button(form, text="3", padx=30, pady=15, command=lambda: buttonAdd(3))
btn4 = Button(form, text="4", padx=30, pady=15, command=lambda: buttonAdd(4))
btn5 = Button(form, text="5", padx=30, pady=15, command=lambda: buttonAdd(5))
btn6 = Button(form, text="6", padx=30, pady=15, command=lambda: buttonAdd(6))
btn7 = Button(form, text="7", padx=30, pady=15, command=lambda: buttonAdd(7))
btn8 = Button(form, text="8", padx=30, pady=15, command=lambda: buttonAdd(8))
btn9 = Button(form, text="9", padx=30, pady=15, command=lambda: buttonAdd(9))
btn0 = Button(form, text="0", padx=30, pady=15, command=lambda: buttonAdd(0))

btnDecimal = Button(form, text=".", padx=30, pady=15, command=buttonAdd)
btnAdd = Button(form, text="+", padx=30, pady=15, command=buttonAdd)
btnEquals = Button(form, text="=", padx=30, pady=15, command=buttonAdd)
btnClear = Button(form, text="Clear", padx=30, pady=15, command=buttonAdd)

# Display Buttons on screen
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=1)
btnDecimal.grid(row=4, column=2)

btnAdd.grid(row=5, column=0)
btnEquals.grid(row=5, column=1)
btnClear.grid(row=5, column=2)


form.mainloop()