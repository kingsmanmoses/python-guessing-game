from tkinter import *
import tkinter.font as font
from random import randint

attempts = 10
answer = randint(0, 999)


# Function to check if the users input is equal, greater or lesser than the random number
def check_guess():
    global attempts
    global text
    attempts -= 1
    guess = int(entry_window.get())  # Variable to store the users input
    if answer == guess:  # This will run if the users guess is equal to the random number
        text.set('You win!, congratulations!!!')
        btn_submit.pack_forget()
    elif attempts == 0:  # This will run when the user runs out of guess
        text.set('Sorry you have run out of guesses')
        btn_submit.pack_forget()
    elif guess < answer:  # This will run if the users guess is lesser than the random number
        text.set(f'You have {attempts} attempts remaining, try guessing higher')
    elif guess > answer:  # This will run if the users guess is higher than the random number
        text.set(f'You have {attempts} attempts remaining, try guessing lower')


root = Tk()

root.title('Number Guessing Game')  # Title of the window
root.geometry('500x250')  # Specifying the size of the window

# A variable that stores a font family, size and weight
myFont = font.Font(family='Helvetica', size=9, weight='bold')

# Creating label
label = Label(root, text='Guess any number between 0 and 999')
label.config(font=('Helvetica bold', 15,))
label.pack(side=TOP, pady=10)

# Creating an entry box the user will use for input
entry_window = Entry(root, width=55, borderwidth=2, font='Helvetica 11')
entry_window.pack()

# Creating a button that when clicked assigns the users guess to a variable and checks some conditions
btn_submit = Button(root, text='Submit guess', command=check_guess)
btn_submit.config(background='green', foreground='white', borderwidth=0.3, height=2, width=15)
btn_submit['font'] = myFont
btn_submit.pack(side=TOP, pady=10)

# Creating a button that would be used to exit the game at any point
btn_quit = Button(root, text='Quit', command=root.destroy)
btn_quit.config(background='red', foreground='white', borderwidth=0.3, height=2, width=10)
btn_quit['font'] = myFont
btn_quit.pack(side=TOP, pady=10)

# Default string to be displayed once the program runs
text = StringVar()
text.set('You have 10 attempts remaining, Good luck!')

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

# Used to change the start position of the window to the center of the screen
root.eval('tk::PlaceWindow . center')

root.mainloop()
