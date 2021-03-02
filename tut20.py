from tkinter import *
root=Tk()
root.geometry("655x433")
def getval():
    print(f"The value of user name is { uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")
root.title("This is Grid")
user=Label(root,text="USER")
password=Label(root,text="PASSWORD")
user.grid()
password.grid(row=1)

#variables classes in tkinter
#Booleanvar,DoubleVar,IntVar,stringVar

uservalue = StringVar()
passvalue = StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
b1=Button(root,text="SUBMIT",command=getval)
b1.grid()




root.mainloop()