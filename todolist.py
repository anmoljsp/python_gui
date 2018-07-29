from tkinter import *
from PIL import Image
import os

def dele():
    for h in m:
        h.destroy()
def take(event):
    l.append(ent1.get("1.0",'end-1c'))
    x=Message(frame,text=ent1.get("1.0",'end-1c'),width=800,bg="orchid2",pady=15)
    m.append(x)
    x.grid(sticky=W)
    frame.grid_rowconfigure(len(m),pad=15)
    ent1.delete("1.0",END)
    # dele()
    # i=0
    # m=[]
    # for note in l:
    #     x=Message(frame,text=note,width=300,bg="orchid2",pady=15)
    #     m.append(x)
    #     m[i].grid(columnspan=5,sticky=W)
    #     frame.grid_rowconfigure(i,pad=15)
    #     i+=1

def see():
    for h in m:
        print("1")

root=Tk()
root.columnconfigure(ALL,weight=1)
frame=Frame(root,bg="green",width=800,height=400)
frame.config(borderwidth=2,relief="sunken")
frame.grid(sticky=N+W+S+E)

l=[]
l=["This is my first note obviously.Lets create a few notes.", "This should ideally come in the second slot if it works, at all.",
  "I guess we should see if this works first before moving any further."]
# myscrollbar=Scrollbar(canvas,orient="vertical",command=canvas.yview)
# canvas.configure(yscrollcommand=myscrollbar.set)
#
# myscrollbar.grid(column=2,rowspan=100)
i=0
b=[]
m=[]
for note in l:
    x=Message(frame,text=note,width=800,bg="orchid2",pady=15)
    m.append(x)
    frame.columnconfigure(0,weight=1)
    m[i].grid(sticky=W+E)
    p=Button(frame,text="remove")
    b.append(p)
    b[i].grid(row=i,column=101)
    frame.grid_rowconfigure(i,pad=15)
    i+=1
frame1=Frame(root,width=800,height=50,bg="red")
root.columnconfigure(0,weight="1")
frame1.columnconfigure(0,weight="1")
frame1.grid(sticky="nwse")
ent1=Text(frame1,padx=15,height=10)
ent1.grid(sticky=W+E)
but1=Button(frame1,text="submit")
but1.bind("<Button-1>",take)
but1.grid()
root.title("To-do list")
root.geometry("1200x600+0+0")
root.mainloop()
