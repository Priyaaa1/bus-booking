from tkinter import *
root = Tk()
root.title('Add new details')

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 1, columnspan = 6, padx = w//3)


title = Label(root, text = "ONLINE BUS BOOKING SYSTEM" , fg = 'red' , bg = 'sky blue', font = 'Arial 20 bold', )
title.grid(row = 1, column = 1, columnspan = 6,padx = w//3)


detail = Label(root, text = "Add New Details to Database", fg ="green", font = 'Arial 16 bold')
detail.grid(row=2, column=1, columnspan = 6, padx=w//3, pady=20)



def n_op():
    root.destroy()
    import new_operator_7

operator_but= Button(root, text ="New Operator", font = 'Arial 14', bg = "lightgreen", command=n_op)
operator_but.grid(row= 3, column=1, padx=100, pady=10)


def n_bus():
    root.destroy()
    import new_bus_8

bus_but= Button(root, text ="New Bus", bg = "coral2", font = 'Arial 14', command=n_bus)
bus_but.grid(row= 3, column=2, padx=50, pady=10)

def n_route():
    root.destroy()
    import new_route_9

route_but= Button(root, text ="New Route", bg = "skyblue", font = 'Arial 14', command=n_route)
route_but.grid(row= 3, column=3, padx=50, pady=10)

def n_run():
    root.destroy()
    import new_run_10

run_but= Button(root, text ="New Run", bg = "pink3", font = 'Arial 14', command=n_run)
run_but.grid(row= 3, column=4, padx=50, pady=10)



##def home():
##    root.destroy()
##    import home_2
##
##house = PhotoImage(file = ".\\home.png")
##house_but = Button(root, image=house, command=home)
##house_but.grid(row = 5, column = 1)
##
##
##def back():
##    root.destroy()
##    import home_2
##
##back_but = Button(root, text='Go Back', command=back)
##back_but.grid(row = 6, column = 1)
root.mainloop()
