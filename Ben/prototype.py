import tkinter as tk
from tkinter import *


listData = []

# Login Functionality
def verifyLogin(username, password):
    print(username, password)
    if username == "admin" and password == "admin":
        MainPage().__init__(username)
    else:
        LoginPage().__init__()

class MainPage:


    def __init__(self, name=None):
        self.n = name;
        self.main_page = Tk()
        self.main_page.title("Main page")
        self.main_page.geometry("500x500")

        # Buttons
        self.newEmployee = Button(self.main_page, text="Add Employees", command=lambda: self.addEmployee())
        self.newEmployee.grid(row=1, column=1, pady=30)
        self.seeEmployee = Button(self.main_page, text="View Employees", command=lambda: self.viewEmployee())
        self.seeEmployee.grid(row=2, column=1, pady=30)
        self.removeEmployee = Button(self.main_page, text="Delete Employees", command=lambda: self.deleteEmployee())
        self.removeEmployee.grid(row=3, column=1, pady=30)

        # List Box
        self.employeeListBox = Listbox(self.main_page, width=30, height=20)
        self.employeeListBox.grid(rowspan=3,row=1, column=2)

        # Search
        self.search = Entry(self.main_page, textvariable="  Search  ")
        self.search.grid(row=1, column=3)
        self.searchButton = Button(self.main_page, text="  Search  ", command=lambda: self.searchEmployees())
        self.searchButton.grid(row=2, column=3)

        # Temporary Employee Entry Boxes
        self.employeeName = Entry(self.main_page, textvariable="  Name  ")
        self.employeeName.grid(row=5, column=1)
        self.employeeNum = Entry(self.main_page, textvariable="Emp Num")
        self.employeeNum.grid(row=5, column=2)
        self.employeeRole = Entry(self.main_page, textvariable="Emp Role")
        self.employeeRole.grid(row=5, column=3)

        self.databaseInsert()

        self.main_page.mainloop()

        
    
    
    def databaseInsert(self):
        print("Add items from database to this")
    def viewEmployee(self):
        print("View Employee")

    # Add Employee To Listbox
    def addEmployee(self):
        global listData
        print("Add Employee")
        self.employeeListBox.insert(END, self.employeeName.get())
        listData.append(self.employeeName.get())

    # Delete Selected Employee from Listbox
    def deleteEmployee(self):
        global listData
        print("Delete Employee")
        selected = self.employeeListBox.get(self.employeeListBox.curselection())
        self.employeeListBox.delete(tk.ANCHOR)
        listData.pop(listData.index(selected))

    def searchEmployees(self):
        print("Searching")

class LoginPage():

    def Quit(self):
        uName = self.username.get()
        uPass = self.password.get()
        self.login_screen.destroy()
        verifyLogin(uName, uPass)


    def __init__(self):
        self.login_screen = Tk()
        self.login_screen.title("Login")
        self.login_screen.geometry("300x250")
        Label(self.login_screen, text="Please Enter User Credentials").pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Username").pack()
        self.username = Entry(self.login_screen, textvariable="username")
        self.username.pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password").pack()
        self.password = Entry(self.login_screen, textvariable="password", show= '*')
        self.password.pack()
        Label(self.login_screen, text="").pack()
        self.SubmitButton = Button(self.login_screen, text="Submit", command=lambda: self.Quit())
        self.SubmitButton.pack()
        self.login_screen.mainloop()



if __name__ == "__main__":
    LoginPage()
