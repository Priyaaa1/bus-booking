from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()
root.title('New operator')

def add():
    con=sqlite3.connect('bus_database.db')
    c=con.cursor()
    
    Op_id=id_ent.get() 
    Op_name=name_ent.get()
    Op_add=address_ent.get()
    Phone=phone_ent.get()
    Email=email_ent.get()

    if len(id_ent.get())==0 or len(name_ent.get())==0 or len(address_ent.get())==0 or len(phone_ent.get())==0 or len(email_ent.get())==0:
        messagebox.showerror('Value Missing','Please enter all details')

    else:
        c.execute('''insert into operator(operator_name,operator_id,address,phone,email) values (?,?,?,?,?)''',(Op_name,Op_id,Op_add,Phone,Email))
    
        con.commit()
        con.close()
    
        messagebox.showinfo("operator entry update", "operator record updated succesully")

def edit():
    con=sqlite3.connect('bus_database.db')
    c=con.cursor()
    
    Op_id=id_ent.get() 
    Op_name=name_ent.get()
    Op_add=address_ent.get()
    Phone=phone_ent.get()
    Email=email_ent.get()   
    c.execute('''update operator set operator_name=?,operator_id=?,address=?,phone=?,email=? where operator_id=?''',(Op_name,Op_id,Op_add,Phone,Email,Op_id))
    
    con.commit()
    con.close()
    
    messagebox.showinfo("operator entry update", "operator record updated succesully")


h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
            
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 12, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 0)

title = Label(root, text = "ONLINE BUS BOOKING SYSTEM" , fg = 'red' , bg = 'skyblue', font = 'Arial 20 bold')
title.grid(row = 2, column = 0, columnspan = 12, pady=10)


add_text = Label(root, text = "Add Bus Operator Details", bg= "lightgreen", fg = "dark green", font = 'Arian 16 bold')
add_text.grid(row = 6, column = 0, columnspan = 12, pady=20)


id_text = Label(root, text = "Operator id", font = 'Arial 10', pady=15)
id_text.grid(row = 10, column = 0)

id_ent = Entry(root, width= 10)
id_ent.grid(row = 10, column =1)


name_text = Label(root, text = "Name", font = 'Arial 10', pady=15)
name_text.grid(row = 10, column = 2)

name_ent = Entry(root)
name_ent.grid(row = 10, column =3)


address_text = Label(root, text = "Address", font = 'Arial 10', pady=15)
address_text.grid(row = 10, column = 4)

address_ent = Entry(root)
address_ent.grid(row = 10, column =5)


phone_text = Label(root, text = "Phone", font = 'Arial 10', pady=15)
phone_text.grid(row = 10, column = 6)

phone_ent = Entry(root)
phone_ent.grid(row = 10, column =7)


email_text = Label(root, text = "Email", font = 'Arial 10', pady=20)
email_text.grid(row = 10, column = 8)

email_ent = Entry(root)
email_ent.grid(row = 10, column =9)

add_but = Button(root, text = "Add bus", bg= "sea green2", font='Arial 10' , command=add)
add_but.grid(row =10, column = 10)

edit_but = Button(root, text = "Edit", bg = "sea green2", font='Arial 10', command = edit)
edit_but.grid(row =10, column = 11)


def home():
    root.destroy()
    import home_2

houses = PhotoImage(file = ".\\home.png")
Button(root, image = houses, bg = 'light green', command=home).grid(row = 14, column = 8)

def back():
    root.destroy()
    import new_details_6

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 14, column = 9)

root.mainloop()
