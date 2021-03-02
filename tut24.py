from tkinter import *
root=Tk()
root.geometry("655x433")
def getval():
    print("Submitting Form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),payvalue.get(),foodservicevalue.get()} ")

    with open("record.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),payvalue.get(),foodservicevalue.get()}\n ")
root.title("Shiv Travels")

l1=Label(root,text="Welcome to Shiv Travles",font="comicscansms 13 bold",pady=15)
l1.grid(row=0,column=3)

name=Label(root,text="Name")
phone=Label(root,text="Phone No.")
gender=Label(root,text="Gender")
paymode=Label(root,text="Payment Mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
paymode.grid(row=4,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
payvalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
payentry=Entry(root,textvariable=payvalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
payentry.grid(row=4,column=3)

foodservice=Checkbutton(text="want to pre book your meals",variable=foodservicevalue)
foodservice.grid(row=5,column=3)

b1=Button(text="SUBMIT ",command=getval)
b1.grid(row=6,column=3)

root.mainloop()