#akna tegemine
from tkinter import *
from tkinter import ttk

aken = Tk()
aken.title("Keedame putru")
aken.geometry("500x600")
aken.resizable(0,0)
tekstikast = Label(aken, text="Pudrule!", width=20, font="Tahoma 12", anchor="w")
tekstikast.grid(row=0, column=1)

nr=0
def OK():
    liitrid = int(sisestus.get())
    hel = rbValue.get()
    liitridhel = (liitrid*hel)/1000
    kogus.config(text=liitridhel)
    liitrile.config(text=hel)
    

tuhikast1 = Label(aken, text="", width=20, font="Tahoma 12", anchor="w")
tuhikast1.grid(row=1, column=1)

tekstikast = Label(aken, text="Vali helbed :", width=20, font="Tahoma 12", anchor="w")
tekstikast.grid(row=3, column=0)
rbValue=DoubleVar() 
vk1 = Radiobutton(aken, text="nisuhelbed", value=300, variable=rbValue, font="Tahoma12", anchor="w")
vk1.grid(row=2, column=1, sticky="w")
vk2 = Radiobutton(aken, text="riisihelbed", value=450, variable=rbValue,font="Tahoma12", anchor="w" )
vk2.grid(row=3, column=1, sticky="w")
vk1 = Radiobutton(aken, text="kaerahelbed", value=325, variable=rbValue, font="Tahoma12", anchor="w")
vk1.grid(row=4, column=1, sticky="w")
vk2 = Radiobutton(aken, text="manna", value=330, variable=rbValue,font="Tahoma12", anchor="w" )
vk2.grid(row=5, column=1, sticky="w")


tekstikast = Label(aken, text="Piima liitrid:", width=20, font="Tahoma 12", anchor="w")
tekstikast.grid(row=6, column=0, pady=(20,0))
sisestus = Entry(aken, width=20, font="Tahoma 12")
sisestus.grid(row=6, column=1, pady=(20.0))


nupp = Button(aken, text="OK", width=10, font="Tahoma12", command=OK)
nupp.grid(row=7, column=1, padx=2, pady=2)
 
separator = ttk.Separator(aken, orient="horizontal")
separator.grid(row=8, column=0, columnspan=2, sticky="ew", padx=20)

tekstikast = Label(aken, text="Helbeid 1 l kohta :", width=20, font="Tahoma12", anchor="w")
tekstikast.grid(row=9, column=0)
liitrile = Label(aken, text="0.0g", width=20, font="Tahoma12", anchor="w")
liitrile.grid(row=9, column=1)
tekstikast5 = Label(aken, text="g", width=20, font="Tahoma 12", anchor="w")
tekstikast5.grid(row=9, column=2, pady=(20,0))

tekstikast = Label(aken, text="Helbeid vaja:", width=20, font="Tahoma12", anchor="w")
tekstikast.grid(row=10, column=0)
kogus = Label(aken, text="0.0kg", width=20, font="Tahoma12", anchor="w")
kogus.grid(row=10, column=1)
tekstikast5 = Label(aken, text="kg", width=20, font="Tahoma 12", anchor="w")
tekstikast5.grid(row=10, column=2, pady=(20,0))
