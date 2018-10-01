from tkinter import *
from tkinter import messagebox
top = Tk()

kg = IntVar()
cm = IntVar()
def calculate():
    BMI = int(kg.get() / (cm.get()/100) ** 2)
    if BMI <= 18.5:
        HumanBMI = "Underweight"
    elif BMI < 24.9 and BMI >= 18.5:
        HumanBMI = "Average"
    elif BMI < 29.9 and BMI >= 25:
        HumanBMI = "Overweight"
    elif BMI >= 30:
        HumanBMI = "Obese"
    messagebox.showinfo("BMI","Your BMI is " + str(BMI) + ", You are " + HumanBMI)

L1 = Label(top, text="Height(cm)")

L2 = Label(top, text= "Weight(kg)")

E1 = Entry(top, bd =5, textvariable = kg)

E2 = Entry(top, bd =5,textvariable = cm)


B1 = Button(top, text  = "Calculate", command = calculate)
L1.grid(row=3)
L2.grid(row=0)
E1.grid(row=2)
E2.grid(row=4)
B1.grid(row=3,column=1)


top.mainloop()
