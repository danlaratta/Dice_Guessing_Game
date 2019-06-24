import tkinter as tk
import random

# creates window with customized size and title
window = tk.Tk()
window.geometry("300x300")
window.title("Dice Guessing Game")

# label to explain the rules
rules1 = tk.Label(text="Guess a number between 1 and 6.")
rules1.grid(row=0, column=0, columnspan=2)
rules2 = tk.Label(text="If the dice rolls your number, you win.")
rules2.grid(row=1, column=0, columnspan=2)
rules3 = tk.Label(text="If not, you lose")
rules3.grid(row=2, column=0, columnspan=2)

# creates a entry field to enter a guess
entry = tk.Entry(borderwidth=3)
entry.grid(row=3, column=0, padx=15, pady=10)


# function that makes the button perform an action
def on_click():
    # grabs the users guess from the entry field
    guess = entry.get()

    # displays the guess in a label
    display_guess = tk.Label(text="Your guess is: " + guess)
    display_guess.grid(row=4, column=0, columnspan=2)

    # clears the entry field
    entry.delete(0, "end")

    # generates a random number between 1 and 6
    dice_num = random.randrange(1, 7)

    # displays the dice number in a label
    dice_display = tk.Label(text="The dice rolled a: " + str(dice_num))
    dice_display.grid(row=5, column=0, columnspan=2)

    # determines if the user won or lost
    if str(dice_num) == guess and dice_num <= 6:
        win = tk.Label(text="You Win!!")
        win.grid(row=6, column=0, columnspan=2)
        win.after(3000, lambda: win.destroy())
    elif int(guess) > 6 or int(guess) == 0:
        error = tk.Label(text="Error, must guess between 1 and 6")
        error.grid(row=6, column=0, columnspan=2)
        error.after(3000, lambda: error.destroy())
    else:
        lose = tk.Label(text="Sorry you lose, try again")
        lose.grid(row=6, column=0, columnspan=2)
        lose.after(3000, lambda: lose.destroy())


# creates button to enter user's guess
btn = tk.Button(text="Enter", padx=5, pady=5, command=on_click)
btn.grid(row=3, column=1, padx=5, pady=10)

# creates an exit button to close out the game
exit_btn = tk.Button(text="Exit Game", padx=5, pady=5, command=window.quit)
exit_btn.grid(row=7, column=0, pady=10, columnspan=2)

window.mainloop()
