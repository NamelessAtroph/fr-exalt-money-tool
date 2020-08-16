from tkinter import *

#Base
global window
window=Tk()
window.title("Exalt Calculator")
frame1=Frame(window) #Entries
frame2=Frame(window) #Buttons
lbllvl=Label(frame1,text="Level")
level=Entry(frame1)
nmbr=Entry(frame1)
lblnmbr=Label(frame1,text="Number of Dragons")
price=Entry(frame1)
lblprice=Label(frame1,text="Fodder Price")

#Geometry
frame1.pack()
lbllvl.pack()
level.pack()
lblnmbr.pack()
nmbr.pack()
lblprice.pack()
price.pack()

#Run
window.mainloop()