from tkinter import *
def take():
    st=ent1.get(1.0,'end-1c')
    print(st)
def take1():
    st1=ent2.get()
    print(st1)
def del1():
    lab1.destroy()
    but2.destroy()
    ent2.destroy()
top = Tk()
#top.geometry('1200x600')
top.grid_rowconfigure(1,pad=15)
lab=Label(top,text="In love with Python")
lab.grid(row=1,sticky=E)
lab1=Label(top,text="Lets see if this works.")
lab1.grid(row=2,sticky=E)
ent1=Text(top,width=60,height=10,padx=15)
ent2=Entry(top)
but1=Button(top,command=take,text="submit")
but2=Button(top,command=take1,text="submit")
but1.grid(row=1,column=2)
but2.grid(row=2,column=2)
ent1.grid(row=1,column=1)
ent2.grid(row=2,column=1)
c=Checkbutton(top,text="Check this box if you share the same feelings about python.")
c.grid(columnspan="2")
but=Button(top,command=del1,text="delete")
but.grid()
butt=[]
for i in range(0,5):

    butto=Button(top,text=i)
    butt.append(butto)
    butt[i].grid()
top.mainloop()