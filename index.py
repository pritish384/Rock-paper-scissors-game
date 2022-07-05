#modules
from tkinter import *
import random


#variables
game_items = ("Rock" , "Paper" , "Scissor")



#functions
def Rock():
    computer = random.choice(game_items)
    if computer == "Paper":
        result = "You lost , Computer choosed Paper"
    elif computer == "Rock":
        result = "Tie , Computer choosed Rock"
    else:
        result = "You won , Computer choosed Scissor"
    result_text.set(result)


def Paper():
    computer = random.choice(game_items)
    if computer == "Scissor":
        result =  "You lost , Computer choosed Scissor"
    elif computer == "Paper":
         result = "Tie , Computer choosed Paper"
    else:
         result = "You won , Computer choosed Rock"
    result_text.set(result)




def Scissor():
    computer = random.choice(game_items)
    if computer == "Rock":
         result = "You lost , Computer choosed Rock"
    elif computer == "Scissor":
         result = "Tie , Computer choosed Scissor"
    else:
         result = "You won , Computer choosed Paper"      
    result_text.set(result)   


#window configuration
root = Tk()
root.title("Stone Paper Scissor Game by Pritish")
root.geometry("400x400")
root.resizable(width=False, height=False)
root.configure(bg="#11A7DF")
result_text = StringVar()

#Assets
photo1 = PhotoImage(file="assets/Rock.png").subsample(3,3)
photo2 = PhotoImage(file="assets/Paper.png").subsample(3,3)
photo3 = PhotoImage(file="assets/Scissor.png").subsample(3,3)

#Elements
label = Label(root, text="Stone Paper Scissor", fg="black", font="Castellar", background="#11A7DF")
label2 = Label(root, text="Result :-", fg="black", font="Castellar", background="#11A7DF")
btn1 = Button(root, image=photo1, command = Rock , background="#DFEE23")
btn2 = Button(root, image= photo2 , command = Paper , background="#DFEE23")
btn3 = Button(root, image=photo3, command = Scissor , background="#DFEE23")
btn4 = Button(root, text = 'Close', command = root.destroy )
entry = Entry(root, state="disabled" , textvariable=result_text ,width=35)

#pack
label.pack()
label2.place(x=50 , y =95)
btn1.place(x=60 , y=182)
btn2.place(x=180 , y=180)
btn3.place(x=300 , y = 180)
btn4.place(x=180 , y=350)
entry.place(x=150 , y = 100)

#mainloop
root.mainloop()