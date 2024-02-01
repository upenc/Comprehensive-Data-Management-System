from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from datetime import datetime
import mysql.connector


root=Tk()
root.title("Monthly Bill")
root.geometry('700x400+300+200')
root.resizable(False,True)
root.configure(bg="#326273")


def connect_to_database():
    mydb = {
        'host': 'localhost',
        'user': 'project',
        'password': 'Chatur@123',
        'database': 'mydatabase'
    }

    connection = mysql.connector.connect(**mydb)
    return connection

def clear():
    Location_combobox.set('')
    DateValue.set('')
    SnacksValue.set('')
    LunchValue.set('')
    DinnerValue.set('')
    TeaValue.set('')
    RequestValue.set('')

def add_data():
    try:
        location = Location_combobox.get()
        date = DateValue.get()
        formatted_date = datetime.strptime(date, '%m/%d/%y').strftime('%Y-%m-%d')
        snacks = int(SnacksValue.get())
        lunch = int(LunchValue.get())
        dinner = int(DinnerValue.get())
        tea = int(TeaValue.get())
        request_of = RequestValue.get()

        connection = connect_to_database()
        cursor = connection.cursor()

        query = "INSERT INTO `bill` (`Date`, `location`, `Snacks`, `Lunch`, `Dinner`, `Tea`, `request_of`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (formatted_date, location, snacks, lunch, dinner, tea, request_of)
        cursor.execute(query, data)

        connection.commit()
        connection.close()

        messagebox.showinfo("Submission Successful", "Data has been successfully submitted!")
        clear()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

#icon
icon_image = PhotoImage(file="log.png")
root.iconphoto(False,icon_image)
#combobox for location
Location_combobox = Combobox(root,values=['Process','Machanical','VAT','Packing Plant','Railway'],width=43,font="arial 12")
Location_combobox.place(x=200,y=100)
#heading
Label(root,text="SK Canteen",font="Kis 13",bg="#326273",fg="#fff").place(x=320,y=40)
#label
Label(root,text="Location:",font=23,bg="#326273",fg="#fff").place(x=100,y=100)
Label(root,text="Date:",font=23,bg="#326273",fg="#fff").place(x=100,y=150)
Label(root,text="Snacks:",font=23,bg="#326273",fg="#fff").place(x=100,y=200)
Label(root,text="Lunch:",font=23,bg="#326273",fg="#fff").place(x=100,y=250)
Label(root,text="Dinner:",font=23,bg="#326273",fg="#fff").place(x=430,y=250)
Label(root,text="Tea:",font=23,bg="#326273",fg="#fff").place(x=430,y=200)
Label(root,text="Request of:",font=23,bg="#326273",fg="#fff").place(x=100,y=300)

#Entry
DateValue= StringVar()
SnacksValue = StringVar()
LunchValue = StringVar()
DinnerValue = StringVar()
TeaValue = StringVar()
RequestValue = StringVar()

DateEntry(root, textvariable=DateValue, width=43, bd=2, font=20).place(x=200, y=150)
SnacksEntry = Entry(root,textvariable=SnacksValue,width=13,bd=2,font=20).place(x=200,y=200)
LunchEntry = Entry(root,textvariable=LunchValue,width=13,bd=2,font=20).place(x=200,y=250)
DinnerEntry = Entry(root,textvariable=DinnerValue,width=13,bd=2,font=20).place(x=487,y=250)
TeaEntry = Entry(root,textvariable=TeaValue,width=13,bd=2,font=20).place(x=487,y=200)
RequestEntry = Entry(root,textvariable=RequestValue,width=45,bd=2,font=20).place(x=200,y=300)


Button(root,text="Submit",bg="#326273",fg="white",width=12,height=2,command=add_data).place(x=260,y=350)
Button(root,text="Clear",bg="#326273",fg="white",width=12,height=2,command=clear).place(x=380,y=350)
Button(root,text="Exit",bg="#326273",fg="white",width=12,height=2,command=lambda:root.destroy()).place(x=500,y=350)


root.mainloop()