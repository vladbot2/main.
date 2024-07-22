from tkinter import *

bomb = 100
score = 0
press_return = True

def start(event):
    global press_return, bomb, score
    if not press_return:
        return
    bomb = 100
    score = 0
    label.config(text="")
    update_bomb()
    update_score() 
    update_display()
    press_return = False

def update_display():
    global bomb, score
    if bomb > 50:
        bomb_label.config(image=normal_photo)
    elif 0 < bomb <= 50:
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text="Fuse: " + str(bomb))
    score_label.config(text="Score: " + str(score))
    if is_alive():
        root.after(100, update_display)

def update_bomb():
    global bomb
    bomb -= 1  
    if is_alive():
        root.after(200, update_bomb)  

def update_score():
    global score
    score += 1
    if is_alive():
        root.after(1000, update_score)  

def click():
    global bomb
    if is_alive():
        bomb += 2  

def is_alive():
    global bomb, press_return
    if bomb <= 0:
        label.config(text="Bang! Bang! Bang!")
        press_return = True
        return False
    else:
        return True

root = Tk()
root.title("Bang Bang")
root.geometry("500x550")

label = Label(root, text="Press [Enter] to start the game", font=("Comic Sans MS", 12))
label.pack()

fuse_label = Label(root, text="Fuse: " + str(bomb), font=("Comic Sans MS", 14))
fuse_label.pack()

score_label = Label(root, text="Score: " + str(score), font=("Comic Sans MS", 14))
score_label.pack()

no_photo = PhotoImage(file="img/bomb_no.gif")
normal_photo = PhotoImage(file="img/bomb_normal.gif")
bang_photo = PhotoImage(file="img/pow.gif")

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root, text="", bg="#FF0000", fg="#FFFFFF", width=15, font=("Comic Sans MS", 14), command=click)
click_button.pack()

root.bind("<Return>", start)

root.mainloop()
