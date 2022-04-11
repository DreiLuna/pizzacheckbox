from tkinter import *

root= Tk()


r1_v = IntVar()
r1_v.set(1)
r2_v = StringVar()
r2_v.set("red")

labelc = Label(root, text ="Crust", font=('Arial 15 underline'))
labelt = Label(root, text ="Toppings", font=('Arial 15 underline'))
labels = Label(root, text ="Sauce", font=('Arial 15 underline'))

labelc.grid(row= 0, column = 0)
labelt.grid(row=0, column = 1)
labels.grid(row=0, column = 2, padx=15)

ordercom = ""
ordercom1 = "Original, "
ordercom2 = "Red Sauce"
ordercom3 = ""
ordercom4 = ""
ordercom5 = ""
ordercom0 = ""
fordercom = ""
def og():
    global ordercom1
    ordercom1 =" Original,"
def hand():
    global ordercom1
    ordercom1 =" Handtossed,"
def deep():
    global ordercom1
    ordercom1 =" Deep Dish,"

def pep(count):
    global ordercom0
    

    if count == 1:
        ordercom0 = " Pepperoni,"
    elif count == 0:
        ordercom0 = ""

def che(count):
    global ordercom3

    if count == 1:
        ordercom3 = " Cheese,"
    elif count== 0:
        ordercom3 = ""

def sa(count):
    global ordercom4

    if count== 1:
        ordercom4 = " Sausage,"
    elif count== 0:
        ordercom4 = ""

def veg(count):
    global ordercom5
    
    if count == 1:
        ordercom5 = " Veggie,"
    elif count == 0:
        ordercom5 = ""




def red():
    global ordercom2
    ordercom2 =" Red Sauce"

def white():
    global ordercom2
    ordercom2 =" White Sauce"

varp = IntVar()
varc = IntVar()
vars = IntVar()
varv = IntVar()

def finish():
    one = 1
    zero = 0
    global fordercom
    global ordercom3
    global ordercom4
    global ordercom5
    global ordercom0
    
    if varp.get() == 1:
        pep(one)
    else:
        pep(zero)
    
    if varc.get() == 1:
        che(one)
    else:
        che(zero)

    if vars.get() == 1:
        sa(one)
    else:
        sa(zero)

    if varv.get() == 1:
        veg(one)
    else:
        veg(zero)


    fordercom = str(ordercom1) + str(ordercom0)+ str(ordercom3)+ str(ordercom4)+ str(ordercom5) + str(ordercom2)
    lablecc.configure(text=fordercom)
    '''
    checkpep.deselect()
    checkcheese.deselect()
    checksa.deselect()
    checkveg.deselect()
    ordercom3 = ""
    ordercom4 = ""
    ordercom5 = ""
    ordercom0 = ""
    '''





checkog = Radiobutton(root, text="original", command= og, variable= r1_v, value = 1)
checkhand = Radiobutton(root, text="Handtossed", command= hand, variable= r1_v, value = 2)
checkdeep = Radiobutton(root, text="Deep Dish", command= deep, variable= r1_v, value = 3)

checkpep = Checkbutton(root, text="Pepperoni",  variable=varp, onvalue=1, offvalue=0)
checkcheese = Checkbutton(root, text="Cheese",  variable=varc, onvalue=1, offvalue=0)
checksa = Checkbutton(root, text="Sausage",  variable=vars, onvalue=1, offvalue=0)
checkveg = Checkbutton(root, text="Veggie", variable=varv, onvalue=1, offvalue=0)

checkred = Radiobutton(root, text="Red", command= red, variable= r2_v, value = "red")
checkwhite = Radiobutton(root, text="White", command= white, variable= r2_v, value = "white")

ocbutton = Button(root, text= "Finish", command= finish)

lablec = Label(root, text= "Order Comfirmation:")
lablecc = Label(root, text=fordercom)

checkog.grid(row=1 , column=0 )
checkhand.grid(row=2 , column=0 )
checkdeep.grid(row=3 , column=0 )

checkpep.grid(row=1 , column=1 )
checkcheese.grid(row=2 , column=1 )
checksa.grid(row=3 , column= 1)
checkveg.grid(row=4 , column= 1)

checkred.grid(row=1 , column= 2)
checkwhite.grid(row=2 , column= 2)

ocbutton.grid(row=5 , column= 2)

lablec.grid(row=6 , column=0 )
lablecc.grid(row=7 , column=0, columnspan=3)
root.mainloop()

