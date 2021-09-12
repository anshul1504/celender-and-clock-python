from tkinter import *
import calendar
import time
t=Tk()
w=210
h=260
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))
t.resizable(0,0)
t.title("CALENDER")
t.configure(bg="light blue")

def show():
    a=int(s1.get())
    b=int(s2.get())
    c1=calendar.month(b,a)
    t1.delete(0.0,END)
    t1.insert(INSERT,c1)

def times():
    current_time=time.strftime("%I:%M:%S:%p")
    clock_lb1 = Label(bg="black",fg="light blue",text=current_time,font=("",15))
    clock_lb1.after(200,times)
    clock_lb1.place(x=47,y=5,height=17)
    
times()

u1=Label(text="Month",font=("",10),bg="black",fg="red")
u1.place(x=5,y=30,width=50,height=30)

u2=Label(text="Year",font=("",10),bg="black",fg="red")
u2.place(x=100,y=30,width=50,height=30)

s1=Spinbox(font=("",8),values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4,bg="black",fg="cyan")
s1.place(x=60,y=30,width=35,height=30)

s2=Spinbox(font=("",8),from_=1950,to=2100,width=4,bg="black",fg="cyan")
s2.place(x=160,y=30,width=45,height=30)

b1=Button(text="Search",font=("",15),bg="black",fg="orange",activebackground="orange",activeforeground="black",command=show)
b1.place(x=20,y=75,width=171,height=20)

t1=Text(width=21,height=8,bg="black",fg="white")
t1.place(x=20,y=110)

t.mainloop()