import string
from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()
root.title('New bus')

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

clicked = StringVar()
clicked.set("AC 2+2")
              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 1, columnspan = 12, padx = w//3)


title = Label(root, text = "ONLINE BUS BOOKING SYSTEM" , fg = 'red' , bg = 'skyblue', font = 'Arial 18 bold')
title.grid(row = 1, column = 5, columnspan = 4, pady=10)


title = Label(root, text = "Add Bus Details" , fg = 'green' , font = 'Arial 14 bold')
title.grid(row = 2, column = 5, columnspan = 4, pady=20)


add_bus = Label(root, text = "Bus ID")
add_bus.grid(row=3, column=0, pady=10)

ent_bus = Entry(root)
ent_bus.grid(row=3, column=1, pady=10)

type_bus = Label(root, text = "Bus Type")
type_bus.grid(row=3, column=2, pady=10)

drop_bus = OptionMenu(root, clicked ,"AC 2+2", "AC 3+2", "Non AC2+2", "Non AC 3+2", "AC-Sleeper 2+1", "Non-AC SLeeper 2+1" )
drop_bus.grid(row=3, column=3, pady=10)
BUS_TYPE=clicked.get()

capacity_text = Label(root, text = "Capacity")
capacity_text.grid(row=3, column=4, pady=10)

cap_ent = Entry(root)
cap_ent.grid(row=3, column=5, pady=10)

fare_text = Label(root, text = "Fare")
fare_text.grid(row=3, column=6, pady=10)

fare_ent = Entry(root)
fare_ent.grid(row=3, column=7, pady=10)

opt_text = Label(root, text = "Operator ID")
opt_text.grid(row=3, column=8, pady=10)

opt_ent = Entry(root)
opt_ent.grid(row=3, column=9, pady=10)

route_text = Label(root, text = "Route ID")
route_text.grid(row=3, column=10, pady=10)

route_ent = Entry(root)
route_ent.grid(row=3, column=11, pady=10)

blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 13, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 14, column = 0)

def add_record():
    Add_Bus=ent_bus.get()
    BUS_TYPE=clicked.get()
    Capacity=cap_ent.get()
    Fare=fare_ent.get()
    Op_id=opt_ent.get()
    Rt_id=route_ent.get()

    if len(ent_bus.get())==0 or len(cap_ent.get())==0 or len(fare_ent.get())==0 or len(opt_ent.get())==0 or len(rt_ent.get())==0:
        messagebox.showerror('Value Missing','Please enter all details')

    else:
        con=sqlite3.connect('bus_database.db')
        c=con.cursor()
    
        c.execute(''' select op_name from bus_details where op_id=?''',(Op_id,))
        r=c.fetchone()
        O=r[0][0]
        c.execute('''insert into bus_details (bus_id,op_name,bus_type,seat_capacity,fare,op_id,rt_id) values (?,?,?,?,?,?,?)''',(Add_Bus,O,BUS_TYPE,Capacity,Fare,Op_id,Rt_id))
    
        # c.execute(''' UPDATE bus_details SET op_name=? WHERE OP_ID=? AND BUS_ID=?''',(Op_name,Op_id,Add_Bus))
        con.commit()
        con.close()
        messagebox.showinfo("bus entry", "Bus record added")

def edit_record():
    Add_Bus=ent_bus.get()
    BUS_TYPE=clicked.get()
    Capacity=cap_ent.get()
    Fare=fare_ent.get()
    Op_id=opt_ent.get()
    Rt_id=route_ent.get()
    
    con=sqlite3.connect('bus_database.db')
    c=con.cursor()
    
    c.execute(''' select op_name from bus_details where op_id=?''',(Op_id,))
    r=c.fetchone()
    O=r[0]
    c.execute('''update bus_details SET bus_type=?,seat_capacity=? ,op_id=?, rt_id=?, fare=? where bus_id=?''',(BUS_TYPE,Capacity,Op_id,Rt_id,Fare,Add_Bus))
    
    # c.execute(''' UPDATE bus_details SET op_name=? WHERE OP_ID=? AND BUS_ID=?''',(Op_name,Op_id,Add_Bus))
    con.commit()
    con.close()
    messagebox.showinfo("bus entry", "Bus record added")

    #label10 = ttk.Label(frame_bottom, text='  ' +bus_id+ '   ' +BUS_TYPE+ '  ' +Capacity)

add_but = Button(root, text = "Add Bus", bg = 'sea green2', command=add_record)
add_but.grid(row = 5, column = 6)

edit_but = Button(root, text = "Edit Bus",bg = 'sea green2', command=edit_record)
edit_but.grid(row = 5, column = 7)

house = PhotoImage(file = ".\\home.png")

def home():
    root.destroy()
    import home_2

house_but = Button(root, image=house,bg = 'sea green2', command=home)
house_but.grid(row = 5, column = 8)

def back():
    root.destroy()
    import new_details_6

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 5, column = 9)

root.mainloop()
