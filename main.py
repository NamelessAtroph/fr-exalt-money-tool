from tkinter import *

#Base
global window
global level
global nmbr
global price
global lvlmin
global lvlmax
window=Tk()
window.title("Exalt Calculator")
frame1=Frame(window) #Entries
frame2=Frame(window) #Buttons
frame3=Frame(window) #Text
lbllvl=Label(frame1,text="Level")
level=Entry(frame1)
nmbr=Entry(frame1)
lblnmbr=Label(frame1,text="Number of Dragons")
price=Entry(frame1)
lblprice=Label(frame1,text="Fodder Price")
gobtn=Button(frame2,text="Go")
yscroll=Scrollbar(frame3)
txt=Text(frame3,width=25,height=7,yscrollcommand=yscroll.set)
yscroll.config(command=txt.yview)

#Level Dictionary
lvlmin=dict={'1':'2000','2':'3000','3':'4500','4':'6000','5':'7500','6':'9000','7':'10500','8':'12000','9':'13500','10':'15000','11':'16500','12':'18000','13':'19500','14':'21000','15':'22500','16':'24000','17':'25500','18':'27000','19':'28500','20':'30000','21':'31500','22':'33000','23':'34500','24':'36000','25':'37500'}
#Payout source: https://www1.flightrising.com/forums/gde/746775
lvlmax=dict={'1':'3000','2':'4500','3':'6000','4':'7500','5':'9000','6':'10500','7':'12000','8':'13500','9':'15000','10':'16500','11':'18000','12':'19500','13':'21000','14':'22500','15':'24000','16':'25500','17':'27000','18':'28500','19':'30000','20':'31500','21':'33000','22':'34500','23':'36000','24':'37500','25':'39000'}

#Text info
txt.insert('1.1',"Number of Dragons: "+"0"+"\nTotal levels: "+"0"+"\n"+"\nMinimum Revenue: "+"0"+"\nMaximum Revenue: "+"0"+"\nAverage Revenue: "+"0"+"\n"+"\nMinimum Profit: "+"0"+"\nMaximum Profit: "+"0"+"\nAverage Profit: "+"0")

#Configure The Button
#gobtn.configure(command=payouts)

#Geometry
frame1.pack()
lbllvl.pack()
level.pack()
lblnmbr.pack()
nmbr.pack()
lblprice.pack()
price.pack()
frame2.pack()
gobtn.pack()
frame3.pack()
txt.pack(side=LEFT)
yscroll.pack(side=RIGHT, fill=Y)

#Run
window.mainloop()