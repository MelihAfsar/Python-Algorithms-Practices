import random
from tkinter import *

number = [0]

def randomNumberGenerator():
    number[0] = str(random.randrange(1,100))
    print(number[0])

def controlFunction():    
    guessNumber = getGuessNumber.get()
    
    print("information is checked...")
    if (number[0] == guessNumber):
        print("Bravo. You know")
        control.config(text="Bravo. You know.", bg="#696969", fg="white",font=("Calibri Italic", 16))
    else:
        print("you didn't know.")
        control.config(text="You didn't know.", bg="#696969", fg="white",font=("Calibri Italic", 16))




master = Tk()
master.title("NUMBER GAME")
master.geometry("1366x768+250+250")
master.config(bg="light gray")
master.resizable(0, 0)

frameTop = Frame(master, bg="#696969")
frameTop.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.985)

# Generate Button
frameMain = Frame(master, bg="#696969")
frameMain.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.3)

# Title
title = Label(frameTop, text="Number Game", font="Verdana 20 bold")
title.config(bg="#696969", fg="white")
title.pack(pady=20)

# Title2
title2 = Label(frameTop, text="Press the button to generate a random number.", font="Verdana 15 bold")
title2.config(bg="#696969", fg="white")
title2.pack(pady=25)

# Main Frame
frameMain = Frame(master, bg="#696969")
frameMain.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.3)

# guessNumber Frame
guessNumber = Frame(frameMain, bg="#696969")
guessNumber.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)

# Entry guessNumber
getGuessNumber = Entry(guessNumber)
getGuessNumber.config(bg="white", fg="black", font=("Calibri", 14))
getGuessNumber.pack(padx=40, side=RIGHT)

# guessNumber Label
guessNumber = Label(guessNumber)
guessNumber.config(text="Enter the number you guessed:", bg="#696969", fg="white", font=("Calibri Italic", 16))
guessNumber.pack(padx=20, side=LEFT)

# Generate Button Frame
frameButton = Frame(frameMain, bg="#696969")
frameButton.place(relx=0, rely=0.4, relwidth=1, relheight=0.3)

# Generate Button
generateButton = Button(frameButton)
generateButton.config(text="Generate Numbers", bg="white", fg="black", font=("Calibri", 16), command=randomNumberGenerator)
generateButton.pack(padx=100, side=LEFT)

# Check Button
generateButton = Button(frameButton)
generateButton.config(text="Check it", bg="white", fg="black", font=("Calibri", 16), command=controlFunction)
generateButton.pack(padx=100, side=RIGHT)

# Control information Frame
frameControl = Frame(frameMain, bg="#696969")
frameControl.place(relx=0, rely=0.85, relwidth=1, relheight=0.1)

# Control information
control = Label(frameControl)
control.config(text="", bg="#696969", fg="white", font=("Calibri Italic", 15))
control.pack()

master.mainloop()
