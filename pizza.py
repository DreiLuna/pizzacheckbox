from tkinter import *

root= Tk()

labelc = Label(root, text ="Crust")
labelt = Label(root, text ="Toppings")
labels = Label(root, text ="Sauce")

labelc.grid(row= 0, column = 0)
labelt.grid(row=0, column = 1)
labels.grid(row=0, column = 2)

ordercom = ""
ordercom1 = ""
ordercom2 = ""

def og():
    global ordercom1
    ordercom1 =" Original,"
def hand():
    global ordercom1
    ordercom1 =" Handtossed,"
def deep():
    global ordercom1
    ordercom1 =" Deep Dish,"

def pep():
    global ordercom
    ordercom = ordercom + " Pepperoni,"

def che():
    global ordercom
    ordercom = ordercom + " Cheese,"

def sa():
    global ordercom
    ordercom = ordercom + " Sausage,"

def veg():
    global ordercom
    ordercom = ordercom + "Veggie"

def red():
    global ordercom2
    ordercom2 ="Red Sauce"

def og():
    global ordercom2
    ordercom2 ="White Sauce"

def finish():
    fordercom = str(ordercom1) + str(ordercom) + str(ordercom2)

checkog = Radiobutton(root, text="original", command= og)
checkhand = Radiobutton(root, text="Handtossed", command= hand)
checkdeep = Radiobutton(root, text="Deep Dish", command= deep)

checkpep = Checkbutton(root, text="Pepperoni", command= pep)
checkcheese = Checkbutton(root, text="Cheese", command= che)
checksa = Checkbutton(root, text="Sausage", command= sa)
checkveg = Checkbutton(root, text="Veggie", command= veg)

checkred = Radiobutton(root, text="Red", command= red)
checkwhite = Radiobutton(root, text="White", command= white)

ocbutton = Button(root, text= "Finish", command= finish)

lablec = Label(root, text= "Order Comfirmation:")
lablecc = Label(root, text=fordercom)

checkog.grid(row= , column= )
checkhand.grid(row= , column= )
checkdeep.grid(row= , column= )

checkpep.grid(row= , column= )
checkcheese.grid(row= , column= )
checksa.grid(row= , column= )
checkveg.grid(row= , column= )

checkred.grid(row= , column= )
checkwhite.grid(row= , column= )

ocbutton.grid(row= , column= )

lablec.grid(row= , column= )
labelcc.grid(row= , column= )
root.mainloop()

