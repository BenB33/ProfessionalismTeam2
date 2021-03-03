import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import Text
from tkinter import messagebox
import webbrowser
import sqlite3
import csv
from pathlib import Path
from datetime import datetime

empIDData = []
empFirstNameData = []
empLastNameData = []
empHouseNoData = []
empCityData = []
empCountyData = []
empZipCodeData = []
empEmailData = []

# Import CSV File to data arrays
def import_csv_to_arrays(self):
    with open('employees.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        
        for data in csv_reader:
            empIDData.append(data[0])
            empFirstNameData.append(data[1])
            empLastNameData.append(data[2])
            empHouseNoData.append(data[3])
            empCityData.append(data[4])
            empCountyData.append(data[5])
            empZipCodeData.append(data[6])
            empEmailData.append(data[7])
        print(datetime.now(), "[LOG] Data successfully imported from employees.csv")


# Export data arrays to CSV File
def export_arrays_to_csv(self):
    with open('employees.csv', 'w+', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["ID", "first_name", "last_name", "House No", "city", "county", "zip", "email"])
        for data in range(0, len(empIDData)):
            csv_writer.writerow([empIDData[data], empFirstNameData[data], empLastNameData[data], empHouseNoData[data], empCityData[data], empCountyData[data], empZipCodeData[data], empEmailData[data]])
        print(datetime.now(), "[LOG] Exported all array data to employees.csv succesfully")


# Admin Page when user logs in as 'admin'

class AdminPage:
    def __init__(self, name=None):
        self.username = name
        self.admin_page = Tk()
        self.admin_page.title("Admin PIM System")
        self.admin_page.geometry("822x450+840+365")
        self.admin_page.minsize(822, 450)
        self.admin_page.maxsize(822, 450)

        # Listboxes
        self.listID = tk.Listbox()
        self.listID.place(relx=0.013, rely=0.089, relheight=0.827, relwidth=0.152)
        
        self.listFirstName = tk.Listbox()
        self.listFirstName.place(relx=0.17, rely=0.089, relheight=0.827, relwidth=0.151)
        
        self.listLastName = tk.Listbox()
        self.listLastName.place(relx=0.328, rely=0.089, relheight=0.827, relwidth=0.152)

        # For loop to populate the list boxes with array data
        for i in range(0, len(empIDData)):
            print(datetime.now(), "[LOG] Adding item #", i, " to list boxes from arrays")
            self.listID.insert(END, empIDData[i])
            self.listFirstName.insert(END, empFirstNameData[i])
            self.listLastName.insert(END, empLastNameData[i])


        # Entry Boxes
        self.entryID = tk.Entry()
        self.entryID.place(relx=0.706, rely=0.133, height=20, relwidth=0.2)

        self.entryFirstName = tk.Entry()
        self.entryFirstName.place(relx=0.706, rely=0.2, height=20, relwidth=0.2)

        self.entryLastName = tk.Entry()
        self.entryLastName.place(relx=0.706, rely=0.267, height=20, relwidth=0.2)

        self.entryHouseNo = tk.Entry()
        self.entryHouseNo.place(relx=0.706, rely=0.333, height=20, relwidth=0.2)

        self.entryCity = tk.Entry()
        self.entryCity.place(relx=0.706, rely=0.4, height=20, relwidth=0.2)

        self.entryCounty = tk.Entry()
        self.entryCounty.place(relx=0.706, rely=0.467, height=20, relwidth=0.2)

        self.entryZipCode = tk.Entry()
        self.entryZipCode.place(relx=0.706, rely=0.533, height=20, relwidth=0.2)

        self.entryEmail = tk.Entry()
        self.entryEmail.place(relx=0.706, rely=0.6, height=20, relwidth=0.2)


        # Labels

        self.lblSubmitEmpTitle = tk.Label()
        self.lblSubmitEmpTitle.place(relx=0.706, rely=0.044, height=21, width=158)
        self.lblSubmitEmpTitle.configure(text='''Submit New Employee''')
        
        self.lblEmpID = tk.Label()
        self.lblEmpID.place(relx=0.584, rely=0.133, height=21, width=92)
        self.lblEmpID.configure(text='''Employee ID:''')

        self.lblFirstName = tk.Label()
        self.lblFirstName.place(relx=0.596, rely=0.2, height=21, width=83)
        self.lblFirstName.configure(text='''First Name:''')

        self.lblLastName = tk.Label()
        self.lblLastName.place(relx=0.596, rely=0.267, height=21, width=83)
        self.lblLastName.configure(text='''Last Name:''')

        self.lblHouseNo = tk.Label()
        self.lblHouseNo.place(relx=0.596, rely=0.333, height=21, width=83)
        self.lblHouseNo.configure(text='''House No:''')

        self.lblCity = tk.Label()
        self.lblCity.place(relx=0.633, rely=0.4, height=21, width=50)
        self.lblCity.configure(text='''City:''')

        self.lblCounty = tk.Label()
        self.lblCounty.place(relx=0.608, rely=0.467, height=21, width=72)
        self.lblCounty.configure(text='''County:''')

        self.lblZipCode = tk.Label()
        self.lblZipCode.place(relx=0.596, rely=0.533, height=21, width=82)
        self.lblZipCode.configure(text='''ZIP Code:''')

        self.lblEmail = tk.Label()
        self.lblEmail.place(relx=0.62, rely=0.6, height=21, width=49)
        self.lblEmail.configure(text='''Email:''')

        self.lblEmpIDTitle = tk.Label()
        self.lblEmpIDTitle.place(relx=0.013, rely=0.022, height=21, width=127)
        self.lblEmpIDTitle.configure(text='''Employee ID''')

        self.lblFirstNameTitle = tk.Label()
        self.lblFirstNameTitle.place(relx=0.17, rely=0.022, height=21, width=127)
        self.lblFirstNameTitle.configure(text='''First Name''')

        self.lblLastNameTitle = tk.Label()
        self.lblLastNameTitle.place(relx=0.328, rely=0.022, height=21, width=128)
        self.lblLastNameTitle.configure(text='''Last Name''')

        self.lblLoggedInAs = tk.Label()
        self.lblLoggedInAs.place(relx=0.012, rely=0.933, height=21, width=94)
        self.lblLoggedInAs.configure(text='''Logged in as:''')

        self.lblLoggedInUser = tk.Label()
        self.lblLoggedInUser.place(relx=0.122, rely=0.933, height=21, width=73)
        self.lblLoggedInUser.configure(text=self.username)

        self.lblEmpListSize = tk.Label()
        self.lblEmpListSize.place(relx=0.28, rely=0.933, height=21, width=94)
        self.lblEmpListSize.configure(text='''Employee list size:''')

        self.lblEmpListSizeNum = tk.Label()
        self.lblEmpListSizeNum.place(relx=0.414, rely=0.933, height=21, width=55)
        self.lblEmpListSizeNum.configure(text= len(empIDData))


        # Buttons
        self.btnSubmitNewEmp = tk.Button()
        self.btnSubmitNewEmp.place(relx=0.706, rely=0.689, height=24, width=167)
        self.btnSubmitNewEmp.configure(command=self.add_employee)
        self.btnSubmitNewEmp.configure(text='''Submit Employee''')

        self.btnViewEmp = tk.Button()
        self.btnViewEmp.place(relx=0.499, rely=0.844, height=34, width=117)
        self.btnViewEmp.configure(command=self.employee_info_popup)
        self.btnViewEmp.configure(text='''View Employee''')

        self.btnDeleteEmp = tk.Button()
        self.btnDeleteEmp.place(relx=0.657, rely=0.844, height=34, width=117)
        self.btnDeleteEmp.configure(command=self.delete_employee)
        self.btnDeleteEmp.configure(text='''Delete Employee''')

        self.btnClearEmp = tk.Button()
        self.btnClearEmp.place(relx=0.815, rely=0.844, height=34, width=117)
        self.btnClearEmp.configure(command=self.clear_listbox)
        self.btnClearEmp.configure(text='''Clear Employees''')

        self.btnLogout = tk.Button()
        self.btnLogout.place(relx=0.815, rely=0.936, height=24, width=117)
        self.btnLogout.configure(command=self.logout)
        self.btnLogout.configure(text='''Logout''')


        # Separators
        self.TSeparator1 = ttk.Separator()
        self.TSeparator1.place(relx=0.575, rely=0.796,  relwidth=0.349)

        self.TSeparator1_1 = ttk.Separator()
        self.TSeparator1_1.place(relx=0.575, rely=0.038,  relwidth=0.349)

        self.TSeparator2 = ttk.Separator()
        self.TSeparator2.place(relx=0.575, rely=0.04,  relheight=0.756)
        self.TSeparator2.configure(orient="vertical")

        self.TSeparator2_1 = ttk.Separator()
        self.TSeparator2_1.place(relx=0.923, rely=0.04,  relheight=0.756)
        self.TSeparator2_1.configure(orient="vertical")


        # Functions



    # Employee Info Pop-up
    def employee_info_popup(self):

        # Grab the selected index of the employee
        selected = self.listID.curselection()
        print(datetime.now(), "[LOG] Selected Employee ", selected)

        if selected:
            index = selected[0]
            print(datetime.now(), "[LOG] Showing data for employee #", index)

            # Concatenate full employee info into a single string
            showinfo = "Employee ID: " + empIDData[index] + "\nFirst Name: " + empFirstNameData[index] + "\nLast Name: " + empLastNameData[index]+\
                                    "\nHouse No: "+ empHouseNoData[index]+ "\nCity: "+ empCityData[index]+ "\nCounty: "+ empCountyData[index]+ "\nZip Code: "+ empZipCodeData[index]+\
                                    "\nEmail: "+ empEmailData[index]
            
            tk.messagebox.showinfo(title="Employee Info", message=showinfo)
            
        else:
            selected = self.listFirstName.curselection()
            print(datetime.now(), "[LOG] Selected Employee ", selected)
            if selected:
                index = selected[0]
                print(datetime.now(), "[LOG] Showing data for employee #", index)

                # Concatenate full employee info into a single string
                showinfo = "Employee ID: " + empIDData[index] + "\nFirst Name: " + empFirstNameData[index] + "\nLast Name: " + empLastNameData[index]+\
                                "\nHouse No: "+ empHouseNoData[index]+ "\nCity: "+ empCityData[index]+ "\nCounty: "+ empCountyData[index]+ "\nZip Code: "+ empZipCodeData[index]+\
                                "\nEmail: "+ empEmailData[index]
                
                tk.messagebox.showinfo(title="Employee Info", message=showinfo)
                
            else:
                selected = self.listLastName.curselection()
                print(datetime.now(), "[LOG] Selected Employee ", selected)
                if selected:
                    index = selected[0]
                    print(datetime.now(), "[LOG] Showing data for employee #", index)

                    # Concatenate full employee info into a single string
                    showinfo = "Employee ID: " + empIDData[index] + "\nFirst Name: " + empFirstNameData[index] + "\nLast Name: " + empLastNameData[index]+\
                                "\nHouse No: "+ empHouseNoData[index]+ "\nCity: "+ empCityData[index]+ "\nCounty: "+ empCountyData[index]+ "\nZip Code: "+ empZipCodeData[index]+\
                                "\nEmail: "+ empEmailData[index]
                
                    tk.messagebox.showinfo(title="Employee Info", message=showinfo)
                    
                else:
                    print(datetime.now(), "[LOG] No record selected to delete")
                    tk.messagebox.showwarning(title="ERROR: Empty", message="Please select a record to delete!")

        

    # Update Labels
    def update_list_size_label(self):
        self.lblEmpListSizeNum['text'] = str(len(empIDData))


    # Logout
    def logout(self):
        print(datetime.now(), "[LOG] Logging out")
        self.admin_page.destroy()
        LoginPage()


    # Add Employee To Listbox
    def add_employee(self):
        global empIDData
        global empFirstNameData
        global empLastNameData
        

        if len(self.entryID.get()) == 0 or len(self.entryFirstName.get()) == 0 or len(self.entryLastName.get()) == 0 \
        or len(self.entryHouseNo.get()) == 0 or len(self.entryCity.get()) == 0 or len(self.entryCounty.get()) == 0 \
        or len(self.entryZipCode.get()) == 0 or len(self.entryEmail.get()) == 0:
            tk.messagebox.showwarning(title="ERROR: Empty", message="Please enter all the required information.")
            print(datetime.now(), "[LOG] Tried adding employee with empty fields")
        else:
            print(datetime.now(), "[LOG] Adding new employee")
            # Handle the listboxes
            self.listID.insert(END, self.entryID.get())
            self.listFirstName.insert(END, self.entryFirstName.get())
            self.listLastName.insert(END, self.entryLastName.get())

            # Handle the arrays
            empIDData.append(self.entryID.get())
            empFirstNameData.append(self.entryFirstName.get())
            empLastNameData.append(self.entryLastName.get())
            empHouseNoData.append(self.entryHouseNo.get())
            empCityData.append(self.entryCity.get())
            empCountyData.append(self.entryCounty.get())
            empZipCodeData.append(self.entryZipCode.get())
            empEmailData.append(self.entryEmail.get())

            export_arrays_to_csv(self)

            # Clears the text boxes
            self.entryID.delete(0, 'end')
            self.entryFirstName.delete(0, 'end')
            self.entryLastName.delete(0, 'end')
            self.entryHouseNo.delete(0, 'end')
            self.entryCity.delete(0, 'end')
            self.entryCounty.delete(0, 'end')
            self.entryZipCode.delete(0, 'end')
            self.entryEmail.delete(0, 'end')

            # Updating List Count Label
            self.update_list_size_label()
            
            print(datetime.now(), "[LOG] Array Contents: \n", empIDData, "\n", empFirstNameData, "\n", empLastNameData, "\n", empHouseNoData, "\n", empCityData, "\n", empCountyData, "\n", empZipCodeData, "\n", empEmailData, "\n")


    # Delete Selected Employee from Listbox
    def delete_employee(self):

        # Grab the selected index of item being deleted
        selected = self.listID.curselection()
        print(datetime.now(), "[LOG] Selected Employee ", selected)
        if selected:
            index = selected[0]
            print(datetime.now(), "[LOG] Deleting Employee ", index)
                
            # Handle the arrays
            empIDData.pop(index)
            empFirstNameData.pop(index)
            empLastNameData.pop(index)
            empHouseNoData.pop(index)
            empCityData.pop(index)
            empCountyData.pop(index)
            empZipCodeData.pop(index)
            empEmailData.pop(index)

            export_arrays_to_csv(self)

            #Handle the list boxes
            self.listID.delete(index)
            self.listFirstName.delete(index)
            self.listLastName.delete(index)

            # Updating List Count Label
            self.update_list_size_label()
            
        else:
            selected = self.listFirstName.curselection()
            print(datetime.now(), "[LOG] Selected Employee ", selected)
            if selected:
                index = selected[0]
                print(datetime.now(), "[LOG] Deleting Employee ", index)
                
                # Handle the arrays
                empIDData.pop(index)
                empFirstNameData.pop(index)
                empLastNameData.pop(index)
                empHouseNoData.pop(index)
                empCityData.pop(index)
                empCountyData.pop(index)
                empZipCodeData.pop(index)
                empEmailData.pop(index)

                export_arrays_to_csv(self)

                #Handle the list boxes
                self.listID.delete(index)
                self.listFirstName.delete(index)
                self.listLastName.delete(index)

                # Updating List Count Label
                self.update_list_size_label()
                
            else:
                selected = self.listLastName.curselection()
                print(datetime.now(), "[LOG] Selected Employee ", selected)
                if selected:
                    index = selected[0]
                    print(datetime.now(), "[LOG] Deleting Employee ", index)
                
                    # Handle the arrays
                    empIDData.pop(index)
                    empFirstNameData.pop(index)
                    empLastNameData.pop(index)
                    empHouseNoData.pop(index)
                    empCityData.pop(index)
                    empCountyData.pop(index)
                    empZipCodeData.pop(index)
                    empEmailData.pop(index)

                    export_arrays_to_csv(self)

                    #Handle the list boxes
                    self.listID.delete(index)
                    self.listFirstName.delete(index)
                    self.listLastName.delete(index)

                    # Updating List Count Label
                    self.update_list_size_label()
                    
                else:
                    print(datetime.now(), "[LOG] No record selected to delete")
                    tk.messagebox.showwarning(title="ERROR: Empty", message="Please select a record to delete!")
   

     # Clear All Employee Records From ListBox
    def clear_listbox(self):
        global empIDData
        global empFirstNameData
        global empLastNameData
        print(datetime.now(), "[LOG] Clearing Employee Data")
        
        # Clearing Listboxes
        self.listID.delete(0, tk.END)
        self.listFirstName.delete(0, tk.END)
        self.listLastName.delete(0, tk.END)

        # Clearing Arrays
        empIDData.clear()
        empFirstNameData.clear()
        empLastNameData.clear()
        empHouseNoData.clear()
        empCityData.clear()
        empCountyData.clear()
        empZipCodeData.clear()
        empEmailData.clear()

        # Updating List Count Label
        self.update_list_size_label()

        export_arrays_to_csv(self)


# User Page for when user logs in as 'user'

class UserPage:
    def __init__(self, name=None):
        self.username = name
        self.user_page = Tk()
        self.user_page.geometry("600x450+570+385")
        self.user_page.title("Employee List")
        self.user_page.minsize(600, 450)
        self.user_page.maxsize(600, 450)

        # Listboxes
        self.listID = tk.Listbox()
        self.listID.place(relx=0.013, rely=0.089, relheight=0.827, relwidth=0.218)

        self.listFirstName = tk.Listbox()
        self.listFirstName.place(relx=0.267, rely=0.089, relheight=0.827, relwidth=0.218)

        self.listLastName = tk.Listbox()
        self.listLastName.place(relx=0.517, rely=0.089, relheight=0.827, relwidth=0.22)

        # For loop to populate the list boxes with array data
        for i in range(0, len(empIDData)):
            print(datetime.now(), "[LOG] Adding item #", i, " to list boxes from arrays")
            self.listID.insert(END, empIDData[i])
            self.listFirstName.insert(END, empFirstNameData[i])
            self.listLastName.insert(END, empLastNameData[i])
        

        # Labels
        self.lblEmpIDTitle = tk.Label()
        self.lblEmpIDTitle.place(relx=0.033, rely=0.022, height=21, width=103)        
        self.lblEmpIDTitle.configure(text='''Employee ID''')

        self.lblFirstNameTitle = tk.Label()
        self.lblFirstNameTitle.place(relx=0.3, rely=0.022, height=21, width=93)
        self.lblFirstNameTitle.configure(text='''First Name''')
        
        self.lblLastNameTitle = tk.Label()
        self.lblLastNameTitle.place(relx=0.55, rely=0.022, height=21, width=94)
        self.lblLastNameTitle.configure(text='''Last Name''')

        self.lblLoggedInAs = tk.Label()
        self.lblLoggedInAs.place(relx=0.017, rely=0.933, height=21, width=94)
        self.lblLoggedInAs.configure(text='''Logged in as:''')

        self.lblLoggedInUser = tk.Label()
        self.lblLoggedInUser.place(relx=0.167, rely=0.933, height=21, width=64)
        self.lblLoggedInUser.configure(text=self.username)

        self.lblEmpListSize = tk.Label()
        self.lblEmpListSize.place(relx=0.5, rely=0.933, height=21, width=94)
        self.lblEmpListSize.configure(text='''Employee list size:''')

        self.lblEmpListSizeNum = tk.Label()
        self.lblEmpListSizeNum.place(relx=0.667, rely=0.933, height=21, width=44)
        self.lblEmpListSizeNum.configure(text=len(empIDData))
        

        # Buttons
        self.btnViewEmp = tk.Button()
        self.btnViewEmp.place(relx=0.767, rely=0.089, height=34, width=127)
        self.btnViewEmp.configure(command=self.employee_info_popup)
        self.btnViewEmp.configure(text='''View Employee''')

        self.btnLogOut = tk.Button()
        self.btnLogOut.place(relx=0.767, rely=0.222, height=34, width=127)
        self.btnLogOut.configure(command = lambda: self.logout())
        self.btnLogOut.configure(text='''Logout''')

    # Functions

    def logout(self):
        print(datetime.now(), "[LOG] Logging out")
        self.user_page.destroy()
        LoginPage()



        # Employee Info Pop-up
    def employee_info_popup(self):

        # Grab the selected index of the employee
        selected = self.listID.curselection()
        print(datetime.now(), "[LOG] Selected Employee ", selected)



        
        if selected:
            index = selected[0]
            print(datetime.now(), "[LOG] Showing data for employee #", index)

            # Concatenate full employee info into a single string
            showinfo = "Employee ID: " + empIDData[index] + "\nFirst Name: " + empFirstNameData[index] + "\nLast Name: " + empLastNameData[index]+\
                                    "\nHouse No: "+ empHouseNoData[index]+ "\nCity: "+ empCityData[index]+ "\nCounty: "+ empCountyData[index]+ "\nZip Code: "+ empZipCodeData[index]+\
                                    "\nEmail: "+ empEmailData[index]
            
            tk.messagebox.showinfo(title="Employee Info", message=showinfo)
            
        else:
            selected = self.listFirstName.curselection()
            print(datetime.now(), "[LOG] Selected Employee ", selected)
            if selected:
                index = selected[0]
                print(datetime.now(), "[LOG] Showing data for employee #", index)

                # Concatenate full employee info into a single string
                showinfo = "Employee ID: " + empIDData[index] + "\nFirst Name: " + empFirstNameData[index] + "\nLast Name: " + empLastNameData[index]+\
                                "\nHouse No: "+ empHouseNoData[index]+ "\nCity: "+ empCityData[index]+ "\nCounty: "+ empCountyData[index]+ "\nZip Code: "+ empZipCodeData[index]+\
                                "\nEmail: "+ empEmailData[index]
                
                tk.messagebox.showinfo(title="Employee Info", message=showinfo)
                
            else:
                selected = self.listLastName.curselection()
                print(datetime.now(), "[LOG] Selected Employee ", selected)
                if selected:
                    index = selected[0]
                    print(datetime.now(), "[LOG] Showing data for employee #", index)

                    # Concatenate full employee info into a single string
                    showinfo = "Employee ID: " + empIDData[index] + "\nFirst Name: " + empFirstNameData[index] + "\nLast Name: " + empLastNameData[index]+\
                                "\nHouse No: "+ empHouseNoData[index]+ "\nCity: "+ empCityData[index]+ "\nCounty: "+ empCountyData[index]+ "\nZip Code: "+ empZipCodeData[index]+\
                                "\nEmail: "+ empEmailData[index]
                
                    tk.messagebox.showinfo(title="Employee Info", message=showinfo)
                    
                else:
                    print(datetime.now(), "[LOG] No record selected to delete")
                    tk.messagebox.showwarning(title="ERROR: Empty", message="Please select a record to delete!")

        

class LoginPage:

    def __init__(self):
        if len(empIDData) == 0:
            import_csv_to_arrays(self)

        self.login_screen = Tk()
        # LESPI Accepting Var
        self.lespi = tk.IntVar()
        self.lespi.set(0)
        
        self.login_screen.title("Login - PIM System")
        self.login_screen.geometry("300x450+660+210")
        self.login_screen.minsize(300,450)
        self.login_screen.maxsize(300,450)


        # Image
        logo=PhotoImage(file='logo.png')
        Label(image=logo).place(relx=0.27, rely=0.07)


        # Labels
        self.lblEnterCredentialsTitle = tk.Label()
        self.lblEnterCredentialsTitle.place(relx=0.233, rely=0.0, height=22, width=160)
        self.lblEnterCredentialsTitle.configure(text='''Please Enter Use Credentials''')

        self.lblUsernameTitle = tk.Label()
        self.lblUsernameTitle.place(relx=0.233, rely=0.444, height=22, width=160)
        self.lblUsernameTitle.configure(text='''Username''')

        self.lblPasswordTitle = tk.Label()
        self.lblPasswordTitle.place(relx=0.233, rely=0.578, height=22, width=160)
        self.lblPasswordTitle.configure(text='''Password''')
        
        self.lblViewLespiLink = tk.Label()
        self.lblViewLespiLink.place(relx=0.233, rely=0.733, height=22, width=160)
        self.lblViewLespiLink.configure(text='''View LESPI Document''', fg="blue", cursor="hand2")
        self.lblViewLespiLink.bind("<Button-1>", lambda e: self.callback("https://docs.google.com/document/d/1qIkFXqtk_erBnGtNM5_b785t2F3X2FVdUqxs0NIr1EM/edit?usp=sharing"))


        # Entry
        self.entryUsername = tk.Entry()
        self.entryUsername.place(relx=0.233, rely=0.511, height=20, relwidth=0.533)

        self.entryPassword = tk.Entry()
        self.entryPassword.place(relx=0.233, rely=0.644, height=20, relwidth=0.533)
        self.entryPassword.configure(show='*')


        # Radio Buttons
        self.radioAcceptLespi = tk.Radiobutton()
        self.radioAcceptLespi.place(relx=0.233, rely=0.769, relheight=0.082, relwidth=0.46)
        self.radioAcceptLespi.configure(value=1, variable=self.lespi)
        self.radioAcceptLespi.configure(text='''Agree to LESPI''')

        self.radioDisagreeLespi = tk.Radiobutton()
        self.radioDisagreeLespi.place(relx=0.233, rely=0.829, relheight=0.082, relwidth=0.46)
        self.radioDisagreeLespi.configure(value=2, variable=self.lespi)
        self.radioDisagreeLespi.configure(text='''Disagree to LESPI''')


        # Button
        self.btnSubmitLogin = tk.Button()
        self.btnSubmitLogin.place(relx=0.267, rely=0.911, height=24, width=147)
        self.btnSubmitLogin.configure(command = lambda: self.verify_login())
        self.btnSubmitLogin.configure(text='''Login''')
        
        self.login_screen.mainloop()



    # Functions

    # Verify login information (Admin or User accounts) and ensures the user accepts the LESPI Document
    def verify_login(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get()
        print(datetime.now(), "[LOG] Username:", username, "  Password:", password)
        if(self.lespi.get() == 1):
            print(datetime.now(), "[LOG] LESPI has been accepted. Checking Login Details\n")
            if username == "admin" and password == "admin":
                print(datetime.now(), "[LOG] Logging in as admin")
                self.login_screen.destroy()
                AdminPage(username)
            elif username == "user" and password == "user":
                print(datetime.now(), "[LOG] Logging in as user")
                self.login_screen.destroy()
                UserPage(username)
            else:
                print(datetime.now(), "[LOG] Incorrect login details have been entered")
                tk.messagebox.showwarning(title="ERROR: Incorrect Login", message="Incorrect login credentials. Please try again!")
        elif(self.lespi.get() == 2 or self.lespi.get() == 0):
            print(datetime.now(), "[LOG] LESPI Document hasn't been entered, login is not permitted.")
            tk.messagebox.showwarning(title="Must agree to LESPI", message="You must agree to the LESPI to login")


    def callback(self, url):
        webbrowser.open_new(url)


if __name__ == "__main__":
    LoginPage()
