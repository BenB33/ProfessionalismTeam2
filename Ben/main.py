from tkinter import *

form = Tk()

def printMessage():
    printLabel = Label(form, text="Button has been pressed")
    printLabel.pack()

def printEntry():
    thirdLabel = Label(form, text=entry.get())
    thirdLabel.pack()

# Displaying Text
firstLabel = Label(form, text="Hello World")
secondLabel = Label(form, text="Tkinter Research")
firstLabel.pack()
secondLabel.pack()

# Displaying Buttons
firstButton = Button(form, text="Click", state=DISABLED, padx=10, pady=5, bg="red", fg="white")
secondButton = Button(form, text="Print", command=printMessage)
firstButton.pack()
secondButton.pack()

# Input Fields
entry = Entry(form, width=50, borderwidth=5)
entry.pack()
thirdButton = Button(form, text="Submit", command=printEntry)
thirdButton.pack()

form.mainloop()