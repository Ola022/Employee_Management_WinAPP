import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

root = tk.Tk()
root.resizable(False, False)
# Calculate the center position of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 540  # Set your window width
window_height = 650  # Set your window height

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window geometry to be centered
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# root.geometry("540x650")
root.title("Employee Management System")

employee_data = [
    [1, "Tunde Ola", "myemail001.@gmail.com", "CEO", "Clock In"],
    [2, "Tunde Luck", "myemail002.@gmail.com", "Admin", "Clock In"],
    [3, "Tunde Peter", "myemail003.@gmail.com", "Staff", "Clock Out"],
    [4, "Tunde edenut", "myemail004.@gmail.com", "Manager", "Clock In"],
    [5, "mufasa edenut", "myemail005.@gmail.com", "Director", "Clock Out"],

]


def load_employee_data():
    clear_error()
    for item in record_table.get_children():
        record_table.delete(item)

    for r in range(len(employee_data)):
        record_table.insert(parent="", index="end", text="",
                            iid=r, values=employee_data[r])


def put_employee_in_entry():
    selection = record_table.selection()
    if selection:
        index = int(selection[0])
        employee_id.delete(0, tk.END)
        employee_name.delete(0, tk.END)
        employee_email.delete(0, tk.END)
        employee_role.delete(0, tk.END)
        employee_clock_status.set("")

        emp_id = employee_data[index][0]
        emp_name = employee_data[index][1]
        emp_email = employee_data[index][2]
        emp_role = employee_data[index][3]
        emp_clock_status = employee_data[index][4]

        employee_id.insert(0, emp_id)
        employee_name.insert(0, emp_name)
        employee_email.insert(0, emp_email)
        employee_role.insert(0, emp_role)
        employee_clock_status.set(emp_clock_status)
    else:
        # Handle the case when no selection is made
        print("No record selected")


def add_emp_data(emp_id, emp_name, emp_email, emp_role, emp_clock_status):
    try:
        if int(emp_id) and int(emp_id) > 0:
            if int(emp_id) in [emp[0] for emp in employee_data]:
                display_error("Employee ID already exits!")
                messagebox.showerror("Error", "Employee ID already exists!")
            else:
                if emp_name and emp_email and emp_role and emp_clock_status:
                    employee_data.append([emp_id, emp_name, emp_email, emp_role, emp_clock_status])
                    messagebox.showinfo("Success", "Form submitted successfully!")
                    load_employee_data()
                    clear_employee_data()
                else:
                    messagebox.showerror("Error", "Enter Other Employee Details(Name, Email, Role) !")
                    display_error("Enter Other Employee Details(Name, Email, Role) ")
        else:
            display_error("Enter valid number greater than 0")
    except ValueError:
        messagebox.showerror("Error", "Employee ID must be a valid number!")


def update_employees_data(emp_id, emp_name, emp_email, emp_role, index, clock_status_text):
    if index is not None:
        employee_data[index] = [emp_id, emp_name, emp_email, emp_role, clock_status_text]
        load_employee_data()
        clear_employee_data()
    else:
        display_error("Please select Employee first")


def delete_employees_data(index):
    if index is not None:
        del employee_data[index]
        load_employee_data()
        clear_employee_data()
    else:
        display_error("Please select Employee first")


def clear_employee_data():
    employee_id.delete(0, tk.END)
    employee_name.delete(0, tk.END)
    employee_email.delete(0, tk.END)
    employee_role.delete(0, tk.END)
    employee_clock_status.set("Clock In")
    search_entry.delete(0, tk.END)
    load_employee_data()


def find_employee_by_id(emp_id):
    if emp_id != "":
        emp_data_index = []
        for i, data in enumerate(employee_data):
            if (str(emp_id) in str(data[0])) or (str(emp_id).lower() in str(data[1]).lower()):
                emp_data_index.append(i)

        for item in record_table.get_children():
            record_table.delete(item)
        for r in emp_data_index:
            record_table.insert(parent="", index="end", text="",
                                iid=r, values=employee_data[r])
    else:
        load_employee_data()


def display_error(text):
    error_label.config(text=text, fg="red")


def clear_error():
    error_label.config(text="")


head_frame = tk.Frame(root)
heading_lb = tk.Label(head_frame, text="Employee Management System", font=("Bold", 12), fg="white", bg="green")
heading_lb.pack(fill=tk.X, pady=5)
# ------------ First Input   ---------------
employee_id_lb = tk.Label(head_frame, text="Employee Id: ", font=("Bold", 10))
employee_id_lb.place(x=0, y=50)
employee_id = tk.Entry(head_frame, font=("Bold", 10))
employee_id.place(x=110, y=50, width=180)

# ------------ NAME Input   ---------------
employee_name_lb = tk.Label(head_frame, text="Employee Name: ", font=("Bold", 10))
employee_name_lb.place(x=0, y=100)
employee_name = tk.Entry(head_frame, font=("Bold", 10))
employee_name.place(x=110, y=100, width=180)

# ------------ EMAIL Input   ---------------
employee_email_lb = tk.Label(head_frame, text="Employee Email: ", font=("Bold", 10))
employee_email_lb.place(x=0, y=150)
employee_email = tk.Entry(head_frame, font=("Bold", 10))
employee_email.place(x=110, y=150, width=180)

# ------------ Role Input   ---------------
employee_role_lb = tk.Label(head_frame, text="Employee Role: ", font=("Bold", 10))
employee_role_lb.place(x=0, y=200)
employee_role = tk.Entry(head_frame, font=("Bold", 10))
employee_role.place(x=110, y=200, width=180)

# ------------ Clock in & out    ---------------
employee_clock_status_lb = tk.Label(head_frame, text="Clock Status: ", font=("Bold", 10))
employee_clock_status_lb.place(x=0, y=250)

employee_clock_status = tk.StringVar()
check_in_button = tk.Radiobutton(head_frame, text="Clock In", variable=employee_clock_status,
                                 value="Clock In", font=("Bold", 10), fg="green", )  ##a569bd
check_out_button = tk.Radiobutton(head_frame, text="Clock Out", variable=employee_clock_status,
                                  value="Clock Out", font=("Bold", 10), fg="green")
check_in_button.select()
check_in_button.place(x=110, y=250)
check_out_button.place(x=200, y=250)

# ------------ BUTTON REGISTer    ---------------
register_btn = tk.Button(head_frame, text="Insert", font=("Bold", 12), fg="white", bg="green",
                         command=lambda: add_emp_data(employee_id.get(),
                                                      employee_name.get(),
                                                      employee_email.get(),
                                                      employee_role.get(),
                                                      employee_clock_status.get()))
register_btn.place(x=0, y=300)

# ------------ btn UPDATE   ---------------
update_btn = tk.Button(head_frame, text="Update", font=("Bold", 12), fg="white", bg="blue",
                       command=lambda: update_employees_data(
                           employee_id.get(),
                           employee_name.get(),
                           employee_email.get(),
                           employee_role.get(),
                           index=int(record_table.selection()[0]) if record_table.selection() else None,
                           clock_status_text=employee_clock_status.get()
                       ))
update_btn.place(x=80, y=300)

# ------------ btn DELETE    ---------------
delete_btn = tk.Button(head_frame, text="Delete ", font=("Bold", 12), fg="white", bg="red",
                       command=lambda: delete_employees_data(
                           index=int(record_table.selection()[0]) if record_table.selection() else None
                       ))
delete_btn.place(x=170, y=300)

# ------------ btn CLEAR Input   ---------------
clear_btn = tk.Button(head_frame, text="Clear ", font=("Bold", 12),
                      command=lambda: clear_employee_data())
clear_btn.place(x=259, y=300)

# ------------ ERROR label   ---------------
error_label = tk.Label(head_frame, text="", fg="red")
error_label.place(x=0, y=340)

head_frame.pack(pady=10)
head_frame.pack_propagate(False)
head_frame.configure(width=400, height=360)

# ------------ Search BAR input   ---------------
search_bar_frame = tk.Frame(root)
search_lb = tk.Label(search_bar_frame, text="Search By ID/Name: ", font=("Bold", 10), fg="green")
search_lb.pack(anchor=tk.W)
search_entry = tk.Entry(search_bar_frame, font=("Bold", 10), width=180)
search_entry.pack(anchor=tk.W)
search_entry.bind("<KeyRelease>", lambda e: find_employee_by_id(search_entry.get()))

search_bar_frame.pack(pady=0)
search_bar_frame.pack_propagate(False)
search_bar_frame.configure(width=450, height=50)

# ------------ RECORD FRAME   ---------------
record_frame = tk.Frame(root)
record_lb = tk.Label(record_frame, text="Select Record for delete or Update: ", bg="green", fg="white",
                     font=("Bold", 11))
record_lb.pack(fill=tk.X)

record_table = ttk.Treeview(record_frame)
record_table.pack(fill=tk.X, pady=5)
scrollbar = ttk.Scrollbar(record_frame, orient="vertical", command=record_table.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
record_table.bind("<<TreeviewSelect>>", lambda e: put_employee_in_entry())
record_table["column"] = ["Id", "Name", "Email", "Roles", "Clock_Status"]
record_table.column("#0", anchor=tk.W, width=0, stretch=tk.NO)

record_table.column("Id", anchor=tk.W, width=0)
record_table.column("Name", anchor=tk.W, width=100)
record_table.column("Email", anchor=tk.W, width=140)
record_table.column("Roles", anchor=tk.W, width=80)
record_table.column("Clock_Status", anchor=tk.W, width=80)

record_table.heading("Id", text="Id", anchor=tk.W)
record_table.heading("Name", text="Name", anchor=tk.W)
record_table.heading("Email", text="Email", anchor=tk.W)
record_table.heading("Roles", text="Roles", anchor=tk.W)
record_table.heading("Clock_Status", text="Clock Status", anchor=tk.W)

record_frame.pack(pady=0)
record_frame.pack_propagate(False)
record_frame.configure(width=450, height=200)
load_employee_data()

root.mainloop()
