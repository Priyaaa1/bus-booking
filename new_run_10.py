from tkinter import *
import sqlite3
from tkinter import messagebox
root = Tk()
root.title('New run')


def add_run():
    con=sqlite3.connect('bus_database.db')
    c=con.cursor()
    ID=route_ent.get()
    Date=station_ent.get()
    Seat=id_ent.get()
    
    if len(id_ent.get())==0 or len(name_ent.get())==0 or len(address_ent.get())==0 or len(phone_ent.get())==0 or len(email_ent.get())==0:
        messagebox.showerror('Value Missing','Please enter all details')

    else:
        c.execute('''insert into running_details(running_bus_id,running_date,a_seat) values (?,?,?)''',(ID,Date,Seat))
        con.commit()
        con.close()
        messagebox.showinfo("Message", "Record Added Successfully")



def delete_run():
    con=sqlite3.connect('bus_database.db')
    c=con.cursor()
    ID=route_ent.get()
    Date=station_ent.get()
    c.execute(''' delete from running_details where running_bus_id=? and running_date=?''',(ID,Date))
    con.commit()
    con.close()
    messagebox.showinfo("Delete", "Record Deleted Successfully")



h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 10, padx = w//3, pady=10)


title = Label(root, text = "ONLINE BUS BOOKING SYSTEM" , fg = 'red' , bg = 'skyblue', font = 'Arial 20 bold')
title.grid(row = 2, column = 0, columnspan = 10)


title = Label(root, text = "Add Bus Running Details" , fg = 'green' , font = 'Arial 18 bold')
title.grid(row = 6, column = 0, columnspan = 10, pady=20)


route_text = Label(root, text = "Bus Id", font="Arial 11")
route_text.grid(row=10, column=0)

route_ent = Entry(root)
route_ent.grid(row=10, column=1)

station_text = Label(root, text = "Running Date", font="Arial 11")
station_text.grid(row=10, column=2)

station_ent = Entry(root)
station_ent.grid(row=10, column=3)

id_text = Label(root, text = "Seat Available", font="Arial 11")
id_text.grid(row=10, column=4)

id_ent = Entry(root)
id_ent.grid(row=10, column=5)

add_but = Button(root, text = "Add Run", font="Arial 11", bg ="lightgreen",command=add_run)
add_but.grid(row = 10, column = 6, pady=10)

edit_but = Button(root, text = "Delete Run", font="Arial 11", bg = "lightgreen", command=delete_run)
edit_but.grid(row = 10, column = 7, pady=10)


house = PhotoImage(file = ".\\home.png")

def home():
    root.destroy()
    import home_2
house_but = Button(root, image=house, bg = "lightgreen", command=home)
house_but.grid(row = 12, column = 6, pady=10)

def back():
    root.destroy()
    import new_details_6

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 12, column = 7, pady=10)

root.mainloop()
