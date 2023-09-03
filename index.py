# modules
import random
from tkinter import *


# variables
game_items = ("Rock" , "Paper" , "Scissor")


# functions
def make_move(player_move):
	computer_move = random.choice(game_items)
	
	if computer_move == player_move:
		result = "Tie"

	elif (
		player_move == "Rock" and computer_move == "Scissor" or
		player_move == "Paper" and computer_move == "Rock" or
		player_move == "Scissor" and computer_move == "Paper"
	):
		result = "You Win"

	else:
		result = "You Lost"

	result_text.set(f"{result}, Computer choosed {computer_move}")


# window configuration
root = Tk()
root.title("Stone Paper Scissor Game by Pritish")
root.geometry("400x400")
root.resizable(width=False, height=False)
root.configure(bg="#11A7DF")

result_text = StringVar(root)

icon = PhotoImage(file='./assets/logo.ico')
root.tk.call('wm', 'iconphoto', root._w, icon)

result_text = StringVar()



#Assets
rock_img = PhotoImage(file="assets/Rock.png").subsample(3,3)
paper_img = PhotoImage(file="assets/Paper.png").subsample(3,3)
scissor_img = PhotoImage(file="assets/Scissor.png").subsample(3,3)

# Elements
label = Label(root, text="Stone Paper Scissor", fg="black", font="Castellar", background="#11A7DF")
label2 = Label(root, text="Result :-", fg="black", font="Castellar", background="#11A7DF")
btn1 = Button(root, image=rock_img, command=lambda: make_move("Rock"), background="#DFEE23")
btn2 = Button(root, image= paper_img , command=lambda: make_move("Paper"), background="#DFEE23")
btn3 = Button(root, image=scissor_img, command=lambda: make_move("Scissor"), background="#DFEE23")
btn4 = Button(root, text='Close', command=root.destroy)
entry = Entry(root, width=35, state="disabled", textvariable=result_text)

# pack
label.pack()
label2.place(x=50, y =95)
btn1.place(x=60, y=182)
btn2.place(x=180, y=180)
btn3.place(x=300, y = 180)
btn4.place(x=180, y=350)
entry.place(x=150, y = 100)

# mainloop
root.mainloop()
