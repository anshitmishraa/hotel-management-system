from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from constant_variable import WIDTH, HEIGHT

root = Tk()
root.geometry(str(HEIGHT) + "x" + str(WIDTH))

heading_label = Label(root, text="Check-Out Process",
                      font=("Old English Text MT", 50))
heading_label.pack(pady=(50, 50))

root.title("CHECK-OUT PROCESS | HOTEL MAURYAN EMPIRE")

# Database Update
mydb = mysql.connector.connect(
    host='localhost', user='anshit', password='123456', database='hotelManagementSystem')
cur = mydb.cursor()
orginalDb = mysql.connector.connect(
    host='localhost', user='anshit', password='123456', database='hotelManagementSystem')
conn = orginalDb.cursor()

# form Design
top_frame = Frame(root)
top_frame.pack()

# Name Label
rnumber_label = Label(top_frame, text="Room Number", font=('ARIAL', 25))
rnumber_label.grid(row=0, column=0, padx=15, pady=10, sticky=E)

cur.execute("SELECT * FROM customer_details")

rNumberList = []
rNumberList.append("Select your Room Number")
fontExample = ("ARIAL", 18, "bold")

for staff in cur:
    if staff[4]:
        rNumberList.append(str(staff[4]))

if len(rNumberList) == 1:
    messagebox.showwarning(
        "Warning", "Sorry, there is no room in our system that is occupied. We are currently working on it.")
    root.destroy()

# Combobox creation
monthchoosen = ttk.Combobox(
    root, width=30, height=33, textvariable=rNumberList, font=fontExample, values=rNumberList)

monthchoosen.place(relx=0.5, rely=0.3, anchor=S)
monthchoosen.current(0)


def incomplete_data():
    rNumber = monthchoosen.get()

    if rNumber == 'Select your Room Number':
        messagebox.showwarning("Warning", "Please select your Room Number")
    else:
        review()


def click_proceed():
    global review_box, customer_review, feedback
    review_box.destroy()
    customerReview = customer_review.get()

    conn.execute(
        'INSERT INTO review_form (feedback, review) VALUES(%s,%s)', (feedback.get(), customerReview))

    orginalDb.commit()

    click_proceeds()


def click_proceeds():
    rNumber = monthchoosen.get()
    sql_Delete_query = ('DELETE FROM  customer_details where roomNum = %s')
    conn.execute(sql_Delete_query, (rNumber,))

    orginalDb.commit()

    cur.execute(
        'UPDATE room_details SET room_status = %s WHERE room_number= %s', (0, rNumber,))
    mydb.commit()

    orginalDb.close()

    mydb.close()

    messagebox.showwarning("info", "Thank you for visiting us!")
    root.destroy()


def review():
    global review_box, customer_review, feedback
    # variable name
    review_box = tk.Tk()
    customer_review = tk.StringVar(review_box)

    review_box.title("FEEDBACK FORM | HOTEL MAURYAN EMPIRE")
    review_box.geometry(str(HEIGHT) + "x" + str(WIDTH))

    heading_review_label = Label(review_box, text="What About Our Services?",
                                 font=("bold", 30))
    heading_review_label.pack(pady=(50, 50))

    feedback = StringVar(review_box, "1")

    values = {"Good \U0001F600": "1",
              "Bad \U0001F641": "2",
              "Average \U0001F610": "3",
              "Not Sure \U0001F615": "4"}

    for (text, value) in values.items():
        Radiobutton(review_box, text=text, variable=feedback, indicatoron=0,
                    width=20,
                    font=("Arial", 20),
                    pady=20,
                    value=value).pack(anchor=tk.CENTER)

    remark_label = Label(review_box, text="Remark", font=(
        "bold", 25))
    remark_label.pack(pady=(50, 50))
    entry_box = Entry(review_box, font=("Arial", 25), textvar=customer_review,
                      width=50, fg='blue', bg="#ccefff")
    entry_box.pack(padx=(50, 50))

    B1 = Button(review_box, text="Submit", width=10, font=(
        'ARIAL', 20), command=click_proceed)
    B1.pack(pady=50)


# Proceed Button
proceed_button = Button(root, text="PROCEED", width=10, bg="blue", fg='white', font=('ARIAL', 20),
                        relief=RAISED, command=incomplete_data)
proceed_button.place(relx=0.5, rely=0.45, anchor=S)


root.mainloop()
