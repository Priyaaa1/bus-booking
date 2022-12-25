from tkinter import *
from tkinter import messagebox 
root = Tk()
root.title('Ticket')

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
    

bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 1, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "ONLINE BUS BOOKING SYSTEM" , fg = 'red' , bg = 'sky blue', font = 'Arial 18 bold')
title.grid(row = 2, column = 1, columnspan = 3, padx = w//3, pady=15)

##blank = Label(root, text = "                            " )
##blank.grid(row = 3, column = 0)
##blank = Label(root, text = "                            " )
##blank.grid(row = 4, column = 0)
##blank = Label(root, text = "                            " )
##blank.grid(row = 5, column = 0)

ticket_text = Label(root, text ="Bus Ticket", font='Arial 12 bold')
ticket_text.grid(row = 6, column=1, columnspan=3)

final = LabelFrame(root)
final.grid(row = 7, column =1, columnspan=3)

passenger_text = Label(final, text = "Passenger: ", font = 'Arial 10 bold')
passenger_text.grid(row =8, column=0)

seats_text = Label(final, text = "Gender: ", font = 'Arial 10 bold')
seats_text.grid(row =10, column=0)

age_text = Label(final, text = "Age: ", font = 'Arial 10 bold')
age_text.grid(row =12, column=0)

travel_text = Label(final, text = "Travel On: ", font = 'Arial 10 bold')
travel_text.grid(row =14, column=0)

seats_text = Label(final, text = "No of seats: ", font = 'Arial 10 bold')
seats_text.grid(row =16, column=0)

g_text = Label(final, text = "Phone: ", font = 'Arial 10 bold')
g_text.grid(row =8, column=1)

phone_text = Label(final, text = "Fare: ", font = 'Arial 10 bold')
phone_text.grid(row =10, column=1)

fare_text = Label(final, text = "Booked on: ", font = 'Arial 10 bold')
fare_text.grid(row =12, column=1)

detail_text = Label(final, text = "Boarding point: ", font = 'Arial 10 bold')
detail_text.grid(row =14, column=1)

booked_text = Label(final, text = "Bus details: ", font = 'Arial 10 bold')
booked_text.grid(row =16, column=1)

last_text = Label(final, text = "Total amount in rupees you have to pay at the time of boarding the bus :")
last_text.grid(row =20, column=0)


import sqlite3
con=sqlite3.connect('bus_database.db')
cur=con.cursor()
        
cur.execute('''select max(rowid) from booking_details''')
a=cur.fetchone()
num=a[0]
cur.execute('''select name,gender,age,travelling_date,number_of_seats,mobile,total_fare,booking_date,op_name,station_name from booking_details, bus_details, route_details where bus_id=bus and station_id=1 and route_id=rt_id and rowid=?''',[num])
res = cur.fetchall()
for i in res:
    Label(final,text = i[0]).grid(row=9,column = 0)
    Label(final,text = i[2]).grid(row=11,column = 0)
    Label(final,text = i[1]).grid(row=13,column = 0)
    Label(final,text = i[3]).grid(row=15,column = 0)
    Label(final,text = i[4]).grid(row=17,column = 0)
    Label(final,text = i[5]).grid(row=9,column = 1)
    Label(final,text = i[6]).grid(row=11,column = 1)
    Label(final,text = i[7]).grid(row=13,column = 1)
    Label(final,text = i[9]).grid(row=15,column = 1)
    Label(final,text = i[6]).grid(row=20,column = 1)
    Label(final,text = i[8]).grid(row=17,column = 1)
con.commit()
con.close()

messagebox.showinfo('Message','Seat Booked')


house = PhotoImage(file = ".\\home.png")

def home():
    root.destroy()
    import home_2

house_but = Button(root, image=house, bg="sea green2", command=home)
house_but.grid(row = 18, column = 2)

def back():
    root.destroy()
    import journey_details_3

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 20, column = 2)

root.mainloop()
