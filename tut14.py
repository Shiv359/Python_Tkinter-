from tkinter import *
root=Tk()
root.title("My NewsPaper")
root.geometry("900x800")
#root.minsize(200,200)
#root.maxsize(1000,1000)
photo=PhotoImage(file="3.png")
shiv_label=Label(image=photo)
shiv_label.pack()




root.mainloop()