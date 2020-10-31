import pymysql
import tkinter as tk
from tkinter import *
from tkinter import ttk
from constant_variable import WIDTH, HEIGHT

my_connect = pymysql.connect(
    host="localhost",
    user="anshit",
    passwd="123456",
    database="hotelManagementSystem"
)


####### end of connection ####
my_conn = my_connect.cursor()

root = tk.Tk()
root.geometry(str(HEIGHT) + "x" + str(WIDTH))
root.title("ROOM DETAILS | HOTEL MAURYAN EMPIRE")

my_conn.execute("SELECT * FROM room_details")

style = ttk.Style()
style.configure("Treeview.Heading", font=(
    "Arial", 30, 'bold'), padx=150)
style.configure("Treeview", font=("Arial", 20), rowheight=60)

label_1 = tk.Label(root, text=" ", font=(
    "Arial", 25))
label_1.grid(row=0, columnspan=5)
label_2 = tk.Label(root, text="Room Details", font=(
    "Old English Text MT", 40))
label_2.grid(row=1, columnspan=5)
label_3 = tk.Label(root, text=" ", font=(
    "Arial", 25))
label_3.grid(row=2, columnspan=5)
cols = ('Room Number', 'Room Type', 'Room Status')


listBox = ttk.Treeview(
    root, columns=cols, show='headings', height=13)
vsb = ttk.Scrollbar(root, orient="vertical", command=listBox.yview)
vsb.place(x=WIDTH+WIDTH/1.315, y=HEIGHT/12.5, height=HEIGHT/2.33)
listBox.configure(yscrollcommand=vsb.set)


for col in cols:
    listBox.heading(col, text=col)
listBox.column("0", width=int(WIDTH/1.65))
listBox.column("1", width=int(WIDTH/1.7))
listBox.column("2", width=int(WIDTH/1.7))


listBox.grid(row=3, column=0)

for staff in my_conn:
    value = list(staff)
    if staff[2] == 0:
        value[2] = "NOT OCCUPIED"
    elif staff[2] == 1:
        value[2] = "OCCUPIED"
    if staff[1] == 1:
        value[1] = "AC"
    elif staff[1] == 2:
        value[1] = "NON AC"

    listBox.insert("", "end", values=(value))

root.mainloop()
