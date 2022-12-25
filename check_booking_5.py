from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Check your booking')

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def check():

    import sqlite3
    with sqlite3.connect('bus_database.db') as con:
        cur=con.cursor()
    mobile= mobile_ent.get()
    if(mobile==""):
        messagebox.showwarning("Warning","Please Fill the column")
    else:
        cur.execute('''select name,gender,age,travelling_date,number_of_seats,mobile,total_fare,booking_date from booking_details where mobile=? ''',(mobile,))
        res = cur.fetchall()
        if(res==[]):
            answer=messagebox.askyesno("Message","No record found. Do you want to book now ?")
            if answer:
                root.destroy()
                import journey_details_3
        else:
            final = LabelFrame(root)
            final.grid(row = 8, column =2, columnspan=5)

            passenger_text = Label(final, text = "Passenger: ", font="Arial 10 bold")
            passenger_text.grid(row =8, column=0)

            age_text = Label(final, text = "Age: ", font="Arial 10 bold")
            age_text.grid(row =12, column=0)

            travel_text = Label(final, text = "Travel On: ", font="Arial 10 bold")
            travel_text.grid(row =14, column=0)

            seats_text = Label(final, text = "No of Seats: ", font="Arial 10 bold")
            seats_text.grid(row =16, column=0)

            g_text = Label(final, text = "Gender: ", font="Arial 10 bold")
            g_text.grid(row =10, column=0)

            phone_text = Label(final, text = "Phone: ", font="Arial 10 bold")
            phone_text.grid(row =8, column=1)

            flare_text = Label(final, text = "Fare Rs: ", font="Arial 10 bold")
            flare_text.grid(row =10, column=1)

            booked_text = Label(final, text = "Booked On: ", font="Arial 10 bold")
            booked_text.grid(row =12, column=1)

            point_text = Label(final, text = "Boarding Point: ", font="Arial 10 bold")
            point_text.grid(row =14, column=1)

            last_text = Label(final, text = "Total amount to be paid at the time of boarding the bus :")
            last_text.grid(row =20, column=0)

    
        

            for i in res:
                Label(final,text = i[0]).grid(row=9,column = 0)
                Label(final,text = i[2]).grid(row=11,column = 0)
                Label(final,text = i[1]).grid(row=13,column = 0)
                Label(final,text = i[3]).grid(row=15,column = 0)
                Label(final,text = i[4]).grid(row=17,column = 0)
                Label(final,text = i[5]).grid(row=9,column = 1)
                Label(final,text = i[6]).grid(row=11,column = 1)
                Label(final,text = i[7]).grid(row=13,column = 1)
                Label(final,text = i[6]).grid(row=20,column = 1)
                Label(final,text ="Guna").grid(row=15,column=1)
            con.commit()
            con.close()
              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 2, columnspan = 5, padx = w//2.5)

##blank = Label(root, text = "                            " )
##blank.grid(row = 1, column = 1)

title = Label(root, text = "ONLINE BUS BOOKING SYSTEM" , fg = 'red' , bg = 'sky blue', font = 'Arial 18 bold')
title.grid(row = 1, column = 2, columnspan = 5, pady=10)

##blank = Label(root, text = "                            " )
##blank.grid(row = 3, column = 0)
##blank = Label(root, text = "                            " )
##blank.grid(row = 4, column = 0)
##blank = Label(root, text = "                            " )
##blank.grid(row = 5, column = 0)


title1 = Label(root, text = "Check Your Booking" , fg = 'darkgreen' , bg = 'lightgreen', font = 'Arial 14 bold')
title1.grid(row = 2, column = 2, columnspan = 5, pady=10)

##blank = Label(root, text = "                            " )
##blank.grid(row = 5, column = 0)
##blank = Label(root, text = "                            " )
##blank.grid(row = 6, column = 0)

mobile_text = Label(root, text = "Enter Your Mobile No: ", font = 'Arial 11')
mobile_text.grid(row =3, column =1,columnspan = 5)

mobile_ent = Entry(root)
mobile_ent.grid(row =3, column=2, columnspan = 5)

check_but = Button(root, text = "Check Booking", font = 'Arial 11', command = check)
check_but.grid(row = 3, column=3, columnspan = 5)



root.mainloop()
