from tkinter import *

def calculate():
    raiseRate = int(getRaiseRate.get())
    seniority = int(getSeniority.get())
    currentSalary = int(getCurrentSalary.get())
    increasedSalary = currentSalary + (raiseRate*seniority)
    text = str(increasedSalary)
    setIncreasedSalary.config(text = text,bg="white", fg="black", font=("Calibri", 14))

text = "                                                 "

master = Tk()
master.title("Raise Calculator")
master.geometry("800x450+250+250")
master.config(bg="light gray")
master.resizable(0, 0)

frameTop = Frame(master, bg="#696969")
frameTop.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.965)

# Text1
title = Label(frameTop, text="Raise Calculator", font="Verdana 19 bold")
title.config(bg="#696969", fg="white")
title.pack(pady=10)

# Text2
title2 = Label(frameTop, text="Please enter information!", font="Verdana 12 bold")
title2.config(bg="#696969", fg="white")
title2.pack(pady=5)

# Main Frame
frameMain = Frame(master, bg="#696969")
frameMain.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.72)

# Year raise rate Frame
frameRaiseRate = Frame(frameMain, bg="#696969")
frameRaiseRate.place(relx=0, rely=0, relwidth=1, relheight=0.18)

# Seniority Frame
frameSeniority = Frame(frameMain, bg="#696969")
frameSeniority.place(relx=0, rely=0.15, relwidth=1, relheight=0.18)

# Current salary Frame
frameCurrentSalary = Frame(frameMain, bg="#696969")
frameCurrentSalary.place(relx=0, rely=0.3, relwidth=1, relheight=0.18)

# Increased salary Frame
frameIncreasedSalary = Frame(frameMain, bg="#696969")
frameIncreasedSalary.place(relx=0, rely=0.45, relwidth=1, relheight=0.18)

# Calculate Button Frame
frameButton = Frame(frameMain, bg="#696969")
frameButton.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

# Year raise rate
yearRaiseRate = Label(frameRaiseRate)
yearRaiseRate.config(text="Year raise rate:", bg="#696969", fg="white", font=("Calibri Italic", 16))
yearRaiseRate.pack(padx=20, side=LEFT)

# Entry Year raise rate
getRaiseRate = Entry(frameRaiseRate)
getRaiseRate.config(bg="white", fg="black", font=("Calibri", 14))
getRaiseRate.pack(padx=20, side=RIGHT)

# Seniority
seniority = Label(frameSeniority)
seniority.config(text="Seniority:", bg="#696969", fg="white", font=("Calibri Italic", 16))
seniority.pack(padx=20, side=LEFT)

# Entry Seniority
getSeniority = Entry(frameSeniority)
getSeniority.config(bg="white", fg="black", font=("Calibri", 14))
getSeniority.pack(padx=20, side=RIGHT)

# Current salary 
currentSalary  = Label(frameCurrentSalary)
currentSalary.config(text="Current salary:", bg="#696969", fg="white", font=("Calibri Italic", 16))
currentSalary.pack(padx=20, side=LEFT)

# Entry Current salary 
getCurrentSalary = Entry(frameCurrentSalary)
getCurrentSalary.config(bg="white", fg="black", font=("Calibri", 14))
getCurrentSalary.pack(padx=20, side=RIGHT)

# Increased salary 
increasedSalary  = Label(frameIncreasedSalary)
increasedSalary.config(text="Increased salary:", bg="#696969", fg="white", font=("Calibri Italic", 16))
increasedSalary.pack(padx=20, side=LEFT)

# Out Increased salary 
setIncreasedSalary = Label(frameIncreasedSalary)
setIncreasedSalary.config(text=text,bg="white", fg="black", font=("Calibri", 14))
setIncreasedSalary.pack(padx=20, side=RIGHT)

#Calculate Button
calculateButton = Button(frameButton)
calculateButton.config(text="Calculate", bg="white", fg="black", font=("Calibri", 16), command=calculate)
calculateButton.pack(padx=15, side=RIGHT)

# LOOP
master.mainloop()


