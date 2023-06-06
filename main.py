from tkinter import *
from tkinter import messagebox

root = Tk()

# X Starts
clicked = True
count = 0
winner = False


# new game
def new_game():
    global count, clicked, winner
    b1.config(text=' ', state=ACTIVE)
    b2.config(text=' ', state=ACTIVE)
    b3.config(text=' ', state=ACTIVE)
    b4.config(text=' ', state=ACTIVE)
    b5.config(text=' ', state=ACTIVE)
    b6.config(text=' ', state=ACTIVE)
    b7.config(text=' ', state=ACTIVE)
    b8.config(text=' ', state=ACTIVE)
    b9.config(text=' ', state=ACTIVE)
    count = 0
    clicked = True
    winner = False


# disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Check to see if someone won
def win_check():
    global winner
    if (b1["text"] == b2["text"] == b3["text"] == 'X'
            or b4["text"] == b5["text"] == b6["text"] == 'X'
            or b7["text"] == b8["text"] == b9["text"] == 'X'
            or b1["text"] == b4["text"] == b7["text"] == 'X'
            or b2["text"] == b5["text"] == b8["text"] == 'X'
            or b3["text"] == b6["text"] == b9["text"] == 'X'
            or b1["text"] == b5["text"] == b9["text"] == 'X'
            or b3["text"] == b5["text"] == b7["text"] == 'X'):
        winner = True
        messagebox.showinfo(title="Tic Tac Toe", message="Congratulations X, you have won!")
        disable_all_buttons()
    elif (b1["text"] == b2["text"] == b3["text"] == 'O'
            or b4["text"] == b5["text"] == b6["text"] == 'O'
            or b7["text"] == b8["text"] == b9["text"] == 'O'
            or b1["text"] == b4["text"] == b7["text"] == 'O'
            or b2["text"] == b5["text"] == b8["text"] == 'O'
            or b3["text"] == b6["text"] == b9["text"] == 'O'
            or b1["text"] == b5["text"] == b9["text"] == 'O'
            or b3["text"] == b5["text"] == b7["text"] == 'O'):
        winner = True
        messagebox.showinfo(title="Tic Tac Toe", message="Congratulations O, you have won!")
        disable_all_buttons()
    elif count == 9:
        messagebox.showinfo(title="Tic Tac Toe", message="No winner this time, try again!")
        disable_all_buttons()


# Button click
def b_click(b):
    global clicked, count
    if b["text"] == ' ' and clicked is True:
        b["text"] = 'X'
        clicked = False
        count += 1
        win_check()
    elif b["text"] == ' ' and clicked is False:
        b["text"] = 'O'
        clicked = True
        count += 1
        win_check()
    else:
        pass


# making buttons
b1 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", height=3, width=7, font=("Arial", 20), bg="SystemButtonFace", command=lambda: b_click(b9))

# Grid set up
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)

b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)

b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
b9.grid(row=3, column=3)

new_game_button = Button(text="Start New Game", height=1, width=15, font=("Arial", 10), command=new_game)
new_game_button.grid(row=5, column=2)

root.mainloop()
