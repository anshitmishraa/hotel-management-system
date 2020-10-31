from tkinter import *
import tkinter as tk
from tkinter import messagebox
from subprocess import call
from constant_variable import WIDTH, HEIGHT

# Hotel Title
root = Tk()
root.title("HOTEL MAURYAN EMPIRE")
root.geometry(str(HEIGHT) + "x" + str(WIDTH))


# Background Image
C = Canvas(root, bg="blue", height=1920, width=1080)
filename = PhotoImage(
    file="hotel-staff-png-transparent.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Welcome Label
welcome_bar = Label(root, text="Welcome to the Hotel Mauryan Empire",
                    font=("Old English Text MT", 50))
welcome_bar.pack(pady=(50, 50))


def check_in():
    call(["python", "check_in.py"])


def check_out():
    call(["python", "check_out.py"])


def staff_details():
    call(["python", "staff_details.py"])


def exit():
    bye_message = messagebox.showinfo(
        'Bye!!!', 'Thank you so much for visiting us. We are hoping that you will visit us again. Have a Nice Day')
    root.quit()


# Buttons
check_in_button = Button(root, text="Check In", width=56,
                         height=4, command=check_in)
check_in_button.place(relx=0.5, rely=0.3, anchor=CENTER)
check_out_button = Button(root, text="Check Out", width=56,
                          height=4, command=check_out)
check_out_button.place(relx=0.5, rely=0.4, anchor=CENTER)
staff_detail_button = Button(root, text="Staff Detail", width=56,
                             height=4, command=staff_details)
staff_detail_button.place(relx=0.5, rely=0.5, anchor=CENTER)
exit_button = Button(root, text="Exit", width=56,
                     height=4, command=exit)
exit_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# Run Program
root.mainloop()
