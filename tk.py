from tkinter import *
top=Tk()
def printmy():
    print("Anmol is here")
def printmy2(event):
    print("AJSP is here too")
def scrollup(event):
    print("You Scrolled Up")
def rightclick(event):
    print("Right Button Pressed")
def leftclick(event):
    print("Left Button Pressed")
# Code to add widgets will go here...
l=Label(top,text="ehfwbwe,dndqwud",fg="white",bg="red")
l.pack()
m=Label(top,text="ehfwbwe,dndqwud",fg="white",bg="black")
m.pack(fill="x")
n=Label(top,text="ehfwbwe,dndqwud",fg="white",bg="purple")
n.pack(side=LEFT,fill="y")
but= Button(top,text="knn",fg="cyan",bg="black",command=printmy)
but1= Button(top,text="nnk",fg="black",bg="cyan")
but1.pack(side=RIGHT)
but1.bind("<Button-4>",scrollup)
but1.bind("<Button-1>",leftclick)
but1.bind("<Button-3>",rightclick)
but1.bind("<Enter>",printmy2)
but.pack(side=LEFT)

top.mainloop()