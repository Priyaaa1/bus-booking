from tkinter import *
root=Tk()
root.title('Home')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

bus_img=PhotoImage(file='.\\Project\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=2,columnspan=3,padx=w/3+80)
#grid(row=0,column=0,padx=550)

Label(root,text="ONLINE BUS BOOKING SYSTEM", bg='sky blue', font="Arial 20 bold" , fg='red').grid(row=1,column=2,columnspan=3, pady=60)

Label(root,text="\n\n").grid(row=2,column=2)

def seat():
    root.destroy()
    import journey_details_3

Button(root,text="Seat Booking", bg='spring green', font="Arial 14 bold", command=seat).grid(row=3,column=2)

def booked():
    root.destroy()
    import check_booking_5

Button(root,text="Check Booked Seat", bg='green2', font="Arial 14 bold" , command=booked).grid(row=3,column=3 )

def addbus():
    root.destroy()
    import new_details_6

Button(root,text="Add Bus Details", bg='green4', font="Arial 14 bold" , command=addbus).grid(row=3,column=4)

Label(root,text="For Admin Only",font="Arial 12", fg='red').grid(row=4,column=4,pady=25)
