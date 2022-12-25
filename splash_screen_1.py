from tkinter import *
root=Tk()
root.title('splash screen')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

bus_img=PhotoImage(file='.\\Project\Bus_for_project.png')
Label(root,image=bus_img).pack()
#grid(row=0,column=0,padx=550)

Label(root,text="ONLINE BUS BOOKING SYSTEM", bg='LightSkyBlue1', font="Arial 18 bold" , fg='red2' ).pack()

Label(root,text="\n\n\n\nName : Priya Maheshwari\n\n\nEr : 211B226\n\n\nMobile : 9589309224\n\n\n\n", font="Arial 12" , fg='medium blue').pack()

Label(root,text="Submitted  to : Dr. Mahesh Kumar", bg='LightSkyBlue1', font="Arial 18 bold" , fg='red2' ).pack()

Label(root,text="Project Based Learning", font="Arial 14", fg='red2').pack()

def fun(e=0):
    root.destroy()
    import home_2
root.bind('<KeyPress>', fun)
