import tkinter as tk
from tkinter import *
from tkinter import Text

listData = []


# Login Functionality
def verify_login(username, password):
    print(username, password)
    if username == "admin" and password == "admin":
        MainPage(username)
    else:
        LoginPage()


def search_employees():
    print("Searching")


class MainPage:

    def __init__(self, name=None):
        self.n = name
        self.main_page = Tk()
        self.main_page.title("Employee List")
        self.main_page.geometry("592x411+572+345")
        self.main_page.minsize(120, 1)
        self.main_page.maxsize(1924, 1061)
        self.main_page.resizable(1, 1)

        # Buttons
        self.newEmployee = tk.Button()
        self.newEmployee.place(relx=0.59, rely=0.258, height=34, width=197)
        self.newEmployee.configure(command=self.add_employee)
        self.newEmployee.configure(pady="0")
        self.newEmployee.configure(text='''Add Employees''')

        self.viewEmployee = tk.Button()
        self.viewEmployee.place(relx=0.6, rely=0.866, height=34, width=107)
        self.viewEmployee.configure(pady="0")
        self.viewEmployee.configure(text='''View Employees''')

        self.removeEmployee = tk.Button()
        self.removeEmployee.place(relx=0.4, rely=0.866, height=34, width=107)
        self.removeEmployee.configure(command=self.delete_employee)
        self.removeEmployee.configure(pady="0")
        self.removeEmployee.configure(text='''Delete Employees''')

        self.clearEmployee = tk.Button()
        self.clearEmployee.place(relx=0.801, rely=0.866, height=34, width=107)
        self.clearEmployee.configure(command=self.clear_listbox)
        self.clearEmployee.configure(pady="0")
        self.clearEmployee.configure(text='''Clear Employees''')

        self.searchList = tk.Button()
        self.searchList.place(relx=0.524, rely=0.706, height=34, width=197)
        self.searchList.configure(pady="0")
        self.searchList.configure(text='''Search''')

        # List Box
        self.employeeListBox = tk.Listbox()
        self.employeeListBox.place(relx=0.017, rely=0.022, relheight=0.939, relwidth=0.356)

        # Text Boxes
        self.empIdTxt = tk.Text()
        self.empIdTxt.place(relx=0.583, rely=0.044, relheight=0.054, relwidth=0.34)
        self.empIdTxt.configure(wrap="word")

        self.empNameTxt = tk.Text()
        self.empNameTxt.place(relx=0.583, rely=0.112, relheight=0.051, relwidth=0.34)
        self.empNameTxt.configure(wrap="word")

        self.empContactNumTxt = tk.Text()
        self.empContactNumTxt.place(relx=0.583, rely=0.178, relheight=0.054, relwidth=0.34)
        self.empContactNumTxt.configure(wrap="word")

        self.searchListTxt = tk.Text()
        self.searchListTxt.place(relx=0.541, rely=0.633, relheight=0.054, relwidth=0.306)
        self.searchListTxt.configure(wrap="word")

        # Labels
        self.empIdLbl = tk.Label()
        self.empIdLbl.place(relx=0.427, rely=0.044, height=19, width=83)
        self.empIdLbl.configure(text='''Employee ID:''')

        self.empNameLbl = tk.Label()
        self.empNameLbl.place(relx=0.394, rely=0.112, height=19, width=102)
        self.empNameLbl.configure(text='''Employee Name:''')

        self.empContactLbl = tk.Label()
        self.empContactLbl.place(relx=0.39, rely=0.178, height=19, width=102)
        self.empContactLbl.configure(text='''Contact Number:''')

        self.database_insert()

        self.main_page.mainloop()

    def database_insert(self):
        print("Add items from database to this")

    def view_employee(self):
        print("View Employee")

    # Add Employee To Listbox
    def add_employee(self):
        global listData
        print("Add Employee")
        self.employeeListBox.insert(END, self.empIdTxt.get("1.0", END))
        listData.append(self.empIdTxt.get("1.0", END))
        
        self.empIdTxt.delete("1.0", END)

    # Delete Selected Employee from Listbox
    def delete_employee(self):
        global listData
        print("Delete Employee")
        selected = self.employeeListBox.get(self.employeeListBox.curselection())
        self.employeeListBox.delete(tk.ANCHOR)
        listData.pop(listData.index(selected))

    # Clear All Employee Records From ListBox
    def clear_listbox(self):
        global listData
        print("Clear Employee Data")
        self.employeeListBox.delete(0, tk.END)
        listData.clear()


class LoginPage:

    def quit(self):
        uName = self.username.get()
        uPass = self.password.get()
        self.login_screen.destroy()
        verify_login(uName, uPass)

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
        self.password = Entry(self.login_screen, textvariable="password", show='*')
        self.password.pack()
        Label(self.login_screen, text="").pack()
        self.SubmitButton = Button(self.login_screen, text="Submit", command=lambda: self.quit())
        self.SubmitButton.pack()
        self.login_screen.mainloop()


if __name__ == "__main__":
    LoginPage()
