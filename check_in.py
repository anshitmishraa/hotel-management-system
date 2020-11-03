from tkinter import *
from subprocess import call
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constant_variable import WIDTH, HEIGHT, AC_ROOM_CHARGES, NON_AC_ROOM_CHARGES
import random
from datetime import datetime
from datetime import timedelta

root = tk.Tk()
root.geometry(str(HEIGHT) + "x" + str(WIDTH))
root.title("CHECK-IN PROCESS | HOTEL MAURYAN EMPIRE")

heading_label = Label(root, text="Check-In Process",
                      font=('Arial 30 bold'))
heading_label.pack(pady=(50, 50))


# database connection
orginalDb = mysql.connector.connect(
    host='localhost', user='anshit', password='123456', database='hotelManagementSystem')
copyDb = mysql.connector.connect(
    host='localhost', user='anshit', password='123456', database='hotelManagementSystem')
db = mysql.connector.connect(
    host='localhost', user='anshit', password='123456', database='hotelManagementSystem')
allcur = copyDb.cursor()
cur = orginalDb.cursor()
conn = db.cursor()

# form Design
top_frame = Frame(root)
top_frame.pack()


# variable name
firstName = tk.StringVar()
lastName = tk.StringVar()
phoneNumber = tk.StringVar()
emailAddress = tk.StringVar()
numberOfPeople = tk.IntVar()
numberOfDays = tk.IntVar()


# Validation
def valid():
    fName = firstName.get()
    lName = lastName.get()
    phoneNum = phoneNumber.get()
    emailAdd = emailAddress.get()
    numPeople = numberOfPeople.get()
    numDays = numberOfDays.get()

    if roomTypes.get() == 'AC Room':
        room_types = 1
    else:
        room_types = 2
    roomTy = room_types

    if fName == '':
        messagebox.showwarning("Warning", "Please enter your First Name")
    elif lName == '':
        messagebox.showwarning("Warning", "Please enter your Last Name")
    elif phoneNum == '':
        messagebox.showwarning("Warning", "Please enter your Phone Number")
    elif emailAdd == '':
        messagebox.showwarning("Warning", "Please enter your Last Name")
    elif numPeople == '':
        messagebox.showwarning("Warning", "Please enter number of people")
    elif roomTy == '':
        messagebox.showwarning("Warning", "Please enter your Room Type")
    elif numDays == '':
        messagebox.showwarning(
            "Warning", "Please enter the number of days you want to stay")
    else:
        room_booking()


def room_booking():
    global roomNum
    room_booking = tk.Tk()
    room_booking.title("ROOM BOOOKING | HOTEL MAURYAN EMPIRE")
    room_booking.geometry(str(HEIGHT) + "x" + str(WIDTH))

    heading_room_label = Label(room_booking, text="Room Booking",
                               font=("Old English Text MT", 50))
    heading_room_label.pack(pady=(25, 25))

    room_number_label = Label(room_booking, text="Room Number", font=(
        'Arial', 25, 'bold'))
    room_number_label.pack(pady=(25, 25))

    cur.execute("SELECT * FROM room_details")

    rNumberList = []

    if roomTypes.get() == 'AC Room':
        roomType = 1
    else:
        roomType = 2

    for room_detail in cur:
        if room_detail[1] == roomType and room_detail[2] == 0:
            rNumberList.append(str(room_detail[0]))

    for room in rNumberList:
        room_number_label = Label(
            room_booking, text="%s" % (room), font=('Arial', 20))
        room_number_label.pack(padx=(15, 15))

    if (len(rNumberList) == 0 and roomType == 1):
        messagebox.showwarning(
            "Warning", "Sorry all rooms are booked. Please try for Non AC Room")
        room_booking.destroy()
    if (len(rNumberList) == 0 and roomType == 2):
        messagebox.showwarning(
            "Warning", "Sorry all rooms are booked. Please try for AC Room")
        room_booking.destroy()
    if (len(rNumberList) == 0 and roomType == 2)and (len(rNumberList) == 0 and roomType == 1):
        messagebox.showwarning(
            "Warning", "Sorry all rooms are booked. Please come back later!")
        room_booking.destroy()

    n = random.randint(0, len(rNumberList)-1)
    randomRoom = (rNumberList[n])
    r_number_label = Label(
        room_booking, text="Room Alloted: %s" % (randomRoom), font=('Arial', 20))
    r_number_label.pack(pady=(15, 15))
    roomNum = randomRoom

    # Room status button
    room_detail = Button(room_booking, text="Show Room Status", font=('ARIAL', 20), bg='blue',
                         fg='White', width=25, command=room_details, height=2)
    room_detail.pack(pady=(15, 15))

    conn.execute('UPDATE room_details SET room_status = %s WHERE room_number= %s',
                 (1, randomRoom,))
    db.commit()

    # Submit Button
    submit_buttons = Button(room_booking,
                            text="Click for Payment", width=15, bg="blue",
                            fg='White', font=('ARIAL', 20), relief=RAISED, command=click_submit)
    submit_buttons.pack(pady=(15, 15))


def room_details():
    call(["python", "room_details.py"])

# Value Submitted to Database


def return_payment():
    payment_page = Tk()
    payment_page.title("PAYMENT | HOTEL MAURYAN EMPIRE")
    payment_page.geometry(str(HEIGHT) + "x" + str(WIDTH))

    # Payment
    heading_room_label = Label(payment_page, text="Payment",
                               font=("Old English Text MT", 50))
    heading_room_label.pack(pady=(50, 50))

    if roomTypes.get() == 'AC Room':
        room_type = AC_ROOM_CHARGES
    else:
        room_type = NON_AC_ROOM_CHARGES

    total_amount = (numberOfDays.get())*room_type
    payment_label = Label(
        payment_page, text="Payment Details", font=('Arial', 25, 'bold'))
    payment_label.pack(pady=(25, 25))

    cols = ('Number of People', 'Number Of Days',
            'Amount you have to pay(in \u20B9)', 'Check In Time', 'Check Out Time')

    style = ttk.Style(payment_page)
    style.configure("Treeview.Heading",
                    font=("Arial", 20, 'bold'), padx=150)
    style.configure("Treeview", font=("Arial", 15), rowheight=20)

    listBox = ttk.Treeview(
        payment_page, columns=cols, show='headings', height=3)

    for col in cols:
        listBox.heading(col, text=col, anchor=CENTER)
    listBox.column("0", width=int(WIDTH/4), anchor=CENTER)
    listBox.column("1", width=int(WIDTH/4), anchor=CENTER)
    listBox.column("2", width=int(WIDTH/2), anchor=CENTER)
    listBox.column("3", width=int(WIDTH/4), anchor=CENTER)
    listBox.column("4", width=int(WIDTH/4), anchor=CENTER)

    check_in = datetime.now()
    check_in_date_time = check_in.strftime("%m/%d/%Y %H:%M:%S %p")

    check_out = datetime.now() + timedelta(days=numberOfDays.get())
    check_out_date_time = check_out.strftime("%m/%d/%Y %H:%M:%S %p")

    listBox.pack(pady=(25, 25))

    value = (numberOfPeople.get(), numberOfDays.get(),
             total_amount, check_in_date_time, check_out_date_time)

    listBox.insert("", "end", values=(value))

    # Submit Button
    payment_submit_button = Button(payment_page, text="Click for Payment", width=15,
                                   bg="blue", fg='White', font=('ARIAL', 20), relief=RAISED, command=successful)
    payment_submit_button.place(relx=0.5, rely=0.65, anchor=S)


def successful():
    messagebox.showinfo("Check in", "Room Allotment Successful")


def click_submit():
    global roomNum

    fName = firstName.get()
    lName = lastName.get()
    phoneNum = phoneNumber.get()
    emailAdd = emailAddress.get()
    numPeople = numberOfPeople.get()
    numDays = numberOfDays.get()

    if roomTypes.get() == 'AC Room':
        room_types = 1
    else:
        room_types = 2
    roomTy = room_types

    cur.execute('INSERT INTO customer_details'
                '(fName, lName, phoneNum, emailAdd,roomNum, roomTy, numPeople, '
                'numDays) '
                ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',
                (fName, lName, phoneNum, emailAdd, roomNum, roomTy, numPeople, numDays))
    orginalDb.commit()

    allcur.execute('INSERT INTO orginial_customer_details'
                   '(fName, lName, phoneNum, emailAdd,roomNum, roomTy, numPeople, '
                   'numDays) '
                   ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',
                   (fName, lName, phoneNum, emailAdd, roomNum, roomTy, numPeople, numDays))
    copyDb.commit()

    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    phone_number_entry.delete(0, 'end')
    email_address_entry.delete(0, 'end')
    return_payment()


# Name Label
first_name = Label(top_frame, text="First Name : ", font=('Arial', 20))
last_name = Label(top_frame, text="Last Name : ", font=('Arial', 20))
first_name_entry = Entry(top_frame, textvar=firstName, bd=5,
                         bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
last_name_entry = Entry(top_frame, bd=5, textvar=lastName,
                        bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

first_name.grid(row=0, column=0, padx=15, pady=10, sticky=E)
last_name.grid(row=1, column=0, padx=15, pady=10, sticky=E)
first_name_entry.grid(row=0, column=1, pady=10, ipady=5, ipadx=60)
last_name_entry.grid(row=1, column=1, pady=10, ipady=5, ipadx=60)

# phone number
phone_number_label = Label(
    top_frame, text="Mobile Number : ", font=('Arial', 20))
phone_number_entry = Entry(top_frame, textvar=phoneNumber, bd=5,
                           bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

phone_number_label.grid(row=2, column=0, padx=15, pady=10, sticky=E)
phone_number_entry.grid(row=2, column=1, ipady=5, ipadx=60)

# Email Address
email_address_label = Label(
    top_frame, text="Email Address : ", font=('Arial', 20))
email_address_entry = Entry(top_frame, textvar=emailAddress, bd=5,
                            bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

email_address_label.grid(row=3, column=0, padx=15, pady=10, sticky=E)
email_address_entry.grid(row=3, column=1, ipady=5, ipadx=60)

# Number of Days
number_of_day_label = Label(
    top_frame, text="Number of Days : ", font=('Arial', 20))
number_of_day_box = Spinbox(top_frame, textvar=numberOfDays, bg="#ccefff", fg='blue', from_=1, to=30, width=5, bd=5,
                            font=('Arial', 15))

number_of_day_label.grid(row=6, column=0, padx=15, pady=10, sticky=E)
number_of_day_box.grid(row=6, column=1, ipady=5, sticky=W)

# room Type
room_type_label = Label(top_frame, text="Room Type : ", font=('Arial', 20))

rTypeList = []
rTypeList.append("AC Room")
rTypeList.append("Non-AC Room")
fontExample = ("ARIAL", 20, "bold")

# Combobox creation
room_type = ttk.Combobox(
    top_frame, width=20, height=33, textvariable=rTypeList, font=fontExample, values=rTypeList)

room_type.grid(row=7, column=1, pady=10, sticky=E)
room_type.current(0)
roomTypes = room_type

room_type_label.grid(row=7, column=0, pady=10, sticky=E)

# Number of Person
number_of_person_label = Label(
    top_frame, text="Number of People : ", font=('Arial', 20))
number_of_person_box = Spinbox(top_frame, textvar=numberOfPeople, bg="#ccefff", fg='blue', from_=1, to=2, width=5, bd=5,
                               font=('Arial', 15))

number_of_person_label.grid(row=8, column=0, padx=15, pady=10, sticky=E)
number_of_person_box.grid(row=8, column=1, ipady=5, sticky=W)


# Room Book Button
submit_button = Button(root, text="Click to Book Your Room", width=25, bg="blue", fg='White', font=('ARIAL', 20), relief=RAISED,
                       command=valid)
submit_button.place(relx=0.41, rely=0.6)


root.mainloop()
