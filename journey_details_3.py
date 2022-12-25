import string
from tkinter import *
from tkinter.messagebox import *
import sqlite3
import tkinter as tk
root = Tk()
root.title('Journey details')

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

clicked = StringVar()
clicked.set("Male")



def bookbus():

    def confirm ():
        answer = askyesno("Booking Confirmation", "Are you sure you want to book the bus?" )
        if answer:
            Name=name_ent.get()
            Age=age_ent.get()
            Seats=seats_ent.get()
            Mobile1=mobile_ent.get()
            Gender=clicked.get()
            T_date=ent_date.get()
            conn=sqlite3.connect('bus_database.db')
            c=conn.cursor()
            c.execute(''' select count(*)+1 from booking_details''')
            a=c.fetchone()
            count=a[0]
            c.execute('''insert into booking_details (name,gender,age,mobile,bus,travelling_date,booking_date,number_of_seats,rowid) values (?,?,?,?,?,?,DATE(),?,?)''',(Name,Age,Gender,Mobile1,booked_bus_id,T_date,Seats,count))

            c.execute('''update running_details set a_seat=a_seat-? where running_bus_id=? and running_date=?''',(Seats,booked_bus_id,T_date))

            c.execute('''update booking_details set total_fare=?*? where bus=?''',(Fare,Seats,booked_bus_id))
            #st=("Total bill is of "+ Fare + "rupees")
            

            conn.commit()
            conn.close()

            root.destroy()
            import ticket_4



    booked_bus_id=rv1.get()
    
    if booked_bus_id=='None':
        messagebox.showwarning("Warning", "Please select a bus")
    else:
        blank = Label(root, text = "                            " )
        blank.grid(row = 11, column = 0)

        blank = Label(root, text = "                            " )
        blank.grid(row = 12, column = 0)

        blank = Label(root, text = "                            " )
        blank.grid(row = 13, column = 0)

        blank = Label(root, text = "                            " )
        blank.grid(row = 14, column = 0)

        fill_label = Label(root, text = "Fill Passengers Details to book the Bus Ticket" , fg = 'red' , bg = 'sky blue', font = 'Arial 18 bold')
        fill_label.grid(row = 15, column = 0, columnspan = 8)

        blank = Label(root, text = "                            " )
        blank.grid(row = 16, column = 0)

        name_text = Label(root, text = "Name", font="Arial 11")
        name_text.grid(row = 17, column=0)

        name_ent = Entry(root)
        name_ent.grid(row =17, column=1)
        Name=name_ent.get()

        gender_text = Label(root, text = "Gender", font="Arial 11")
        gender_text.grid(row = 17, column=2)

        gender_drop = OptionMenu(root, clicked , "Male", "Female", "Other")
        gender_drop.grid(row = 17, column = 3)

        seats_text = Label(root, text = "No of Seats", font="Arial 11")
        seats_text.grid(row = 17, column=4)

        seats_ent = Entry(root)
        seats_ent.grid(row =17, column=5)
        Seats=seats_ent.get()

        mobile_text = Label(root, text = "Mobile No", font="Arial 11")
        mobile_text.grid(row = 17, column=6)

        mobile_ent = Entry(root)
        mobile_ent.grid(row =17, column=7)
        Mobile=mobile_ent.get()

        age_text = Label(root, text = "Age")
        age_text.grid(row = 17, column=8)

        age_ent = Entry(root)
        age_ent.grid(row =17, column=9)
        Age=age_ent.get()



        conn=sqlite3.connect('bus_database.db')
        c=conn.cursor()
        
        c.execute('''select fare from bus_details where bus_id=?''',(booked_bus_id,))
        m=c.fetchone()
        Fare=m[0]


        conn.commit()
        conn.close()

        book_button = Button(root, text = "Book Seat", bg ="sea green2", font="Arial 11", command = confirm)
        book_button.grid(row = 17, column=10)

    

def showbus():
    if len(ent_To.get())==0 or len(ent_From.get())==0 or len(ent_date.get())==0:
        showerror('Value Missing','Please Enter all details')

    else:
        select_text = Label(root, text = "Select Bus", fg = "dark green",font='Arial 10 bold')
        select_text.grid(row = 8, column=0)

        opt_text = Label(root, text = "Operator", fg = "dark green",font='Arial 10 bold')
        opt_text.grid(row = 8, column=1)

        type_text = Label(root, text = "Bus Type", fg = "dark green",font='Arial 10 bold')
        type_text.grid(row = 8, column=2)

        available_text = Label(root, text = "Available", fg = "dark green",font='Arial 10 bold')
        available_text.grid(row = 8, column=3)

        fare_text = Label(root, text = "Capacity", fg = "dark green",font='Arial 10 bold')
        fare_text.grid(row = 8, column=4)

        fare_text = Label(root, text = "Fare", fg = "dark green",font='Arial 10 bold')
        fare_text.grid(row = 8, column=5)


        conn=sqlite3.connect('bus_database.db')
        c=conn.cursor()
    
        To=ent_To.get()
        From=ent_From.get()
        Date=ent_date.get()
        c.execute('''Select op_name,bus_type,a_seat,seat_capacity,fare,bus_id from bus_details,running_details, route_details as f, route_details as t where f.station_name=? and t.station_name=? and running_date=? and running_bus_id=bus_id and f.station_id<t.station_id and f.route_id=rt_id and t.route_id=rt_id''',(From,To,Date))
        res=c.fetchall()
        num=10
        
        for i in res:
            r1=tk.Radiobutton(root,variable=rv1,value=i[5])
            r1.grid(row=num,column=0)

            operator=Label(root, text = i[0], fg = "blue1")
            operator.grid(row = num, column=1)
            b_type=Label(root, text = i[1], fg = "blue1")
            b_type.grid(row = num, column=2)
            a_seat=Label(root, text = i[2], fg = "blue1")
            a_seat.grid(row = num, column=3)
            t_seat=Label(root, text = i[3], fg = "blue1")
            t_seat.grid(row = num, column=4)
            fare=Label(root, text = i[4], fg = "blue1")
            fare.grid(row = num, column=5)
            num=num+1
    
        conn.commit()
        conn.close()

        book_button = Button(root, text="Proceed to Book", bg = "sea green2", font="Arial 11", command = bookbus)
        book_button.grid(row =10 , column= 6)

    

rv1=tk.StringVar()
rv1.set(None)
booked_bus_id=""  
Name=""
Age=""
Gender=""
Seats=""
Mobile1=""
Fare=0

bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 8, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "ONLINE BUS BOOKING SYSTEM" , fg = 'red' , bg = 'skyblue', font = 'Arial 18 bold')
title.grid(row = 2, column = 0, columnspan = 8)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)

title1 =Label(root, text = "Enter Journey Details", bg="lightgreen", fg = "darkgreen", font = "Arial 14 bold" )
title1.grid(row=4, column = 0, columnspan =8 )


blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

To_text = Label(root, text = "To", font="Arial 11")
To_text.grid(row = 6, column =0)

ent_To = Entry(root, width=20)
ent_To.grid(row = 6, column =1)


From_text = Label(root, text = "From", font="Arial 11")
From_text.grid(row = 6, column =2)

ent_From = Entry(root, width=20)
ent_From.grid(row = 6, column =3)


date_text = Label(root, text = "Journey Date", font="Arial 11")
date_text.grid(row = 6, column =4)

ent_date = Entry(root, width=20)
ent_date.grid(row = 6, column =5)



show_button = Button(root, text = "Show Bus", fg = "black", bg ="sea green2", font="Arial 11", command = showbus)
show_button.grid(row = 6, column =6)

house = PhotoImage(file = ".\\home.png")

def home():
    root.destroy()
    import home_2

home_button = Button(root, image = house, bg="sea green2", command=home)
home_button.grid(row =6 , column= 7)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)

def back():
    root.destroy()
    import home_2

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 6, column = 9)

root.mainloop()





