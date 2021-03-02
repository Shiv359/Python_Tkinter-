from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("655x455")
root.title("Sliders")
def paise():
    print(f"we have credited {myslider2.get()} dollars to your account")
    tmsg.showinfo("Amount Credited",f"we have credited {myslider2.get()} dollars to your account")

def feedfile():
    print(f"The experience of user is {myslider3.get()}")
    with open("record2.txt","a") as f:
        f.write(f"The experience of user is {myslider3.get()}\n")
#myslider=Scale(root,from_=0,to_=455)
#myslider.pack()
Label(root,text="How many dollars yowu want").pack()
myslider2=Scale(root,from_=0,to_=455,orient=HORIZONTAL)

myslider2.pack()
Button(root,text="get dollars",command=paise).pack()

Label(root,text="rate your experience").pack()
myslider3=Scale(root,from_=0,to_=10,orient=HORIZONTAL)
myslider3.pack()
Button(root,text="Submit your rating",pady=9,command=feedfile).pack()

root.mainloop()