import tkinter as tk
from tkinter import messagebox
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",  
    password="admin",  
    database="employee_db"
)
    
    

def add_employee():
    id = id_entry.get()
    fname=fname_entry.get()
    lname=lname_entry.get()
    salary=salary_entry.get()
    phone=num_entry.get()

    if id and fname:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO employee (emp_id,emp_fname,emp_lname,emp_sal,emp_num) VALUES (%s,%s,%s,%s,%s)",(id,fname,lname,salary,phone))
        mydb.commit()
        cursor.close()
        messagebox.showinfo("Success", "Employee added successfully")
        id_entry.delete(0, tk.END)
        fname_entry.delete(0, tk.END)
        lname_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)
        num_entry.delete(0, tk.END)
        view_employees()
    else:
        messagebox.showwarning("Input Error", "Please enter a name.")

def delete_employee():
    id=id_entry.get()
    if id :
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM employee where emp_id=%s",(id,))
        mydb.commit()
        cursor.close()
        messagebox.showinfo("Success", "Employee deleted successfully")
        id_entry.delete(0, tk.END)
        fname_entry.delete(0, tk.END)
        lname_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)
        num_entry.delete(0, tk.END)
        view_employees()
    else:
        messagebox.showwarning("Input Error", "Please enter an id.")


def view_employees():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee")
    records = cursor.fetchall()
    cursor.close()
    
    
    
    employee_list.delete(1.0, tk.END)

    
    if records:
        for record in records:
            employee_list.insert(tk.END, f"ID: {record[0]}, FirstName: {record[1]},LastName: {record[2]},Salary: {record[3]},Phone: {record[4]}\n")
    else:
        employee_list.insert(tk.END, "No employees found.")


app = tk.Tk()
app.title("Employee Management System")

tk.Label(app, text="id:").grid(row=0, column=0)
id_entry = tk.Entry(app)
id_entry.grid(row=0, column=1)

tk.Label(app, text="first name:").grid(row=1, column=0)
fname_entry = tk.Entry(app)
fname_entry.grid(row=1, column=1)

tk.Label(app, text="last name:").grid(row=2, column=0)
lname_entry = tk.Entry(app)
lname_entry.grid(row=2, column=1)

tk.Label(app, text="salary :").grid(row=3, column=0)
salary_entry = tk.Entry(app)
salary_entry.grid(row=3, column=1)

tk.Label(app, text="phone number:").grid(row=4, column=0)
num_entry = tk.Entry(app)
num_entry.grid(row=4, column=1)


tk.Button(app, text="Add Employee", command=add_employee).grid(row=5, column=1, columnspan=2)
tk.Button(app, text="Delete Employee", command=delete_employee).grid(row=6, column=1, columnspan=2)

employee_list = tk.Text(app, height=10, width=80)
employee_list.grid(row=7, column=0, columnspan=2)

view_employees()  

app.mainloop()