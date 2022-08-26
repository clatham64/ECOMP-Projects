#Import stuff
from tkinter import *
import random
import time

#initialize vars
colors = ['dodgerblue','darkolivegreen','red','cyan','purple','gold']


#make window
window = Tk()
window.title('Catching Vibes')

#Make canvas
canvas = Canvas(window,width=600,height = 400, bg = 'black')
canvas.pack()

#set up welcome screen with titlle and directions
title = canvas.create_text(300,150, text = 'Catching Vibes', \
fill = 'white', font = ('Helvetica',40))
directions = canvas.create_text(300,300, text = 'Catch vibes! \nArrows move up down\n\
press \'q\' to quit.', \
fill = 'white', font = ('Helvetica',20))

#set up score
score = 0
score_display = Label(window, text = 'Score :'+str(score))
score_display.pack()

player_image = PhotoImage(file="Net.gif")
#use image to create char at 50,200
char = canvas.create_image(50,200,image = player_image)

#variables and lists for vibes
vibe_list = [] #vibes
vibe_type = [] #vibe color
vibe_speed = 5 #vibe speed

#Make vibes function
def make_vibe():
    #pick random y postion
    ypos = random.randint(1,400)

    #pick random color for vibe
    vibe_check = random.randint(0,5)

    #make the vibe
    vibe = canvas.create_oval(600, ypos, 630, ypos+30, fill = colors[vibe_check])

    #add it to the lists
    vibe_list.append(vibe)
    vibe_type.append(colors[vibe_check])

    #make more vibes
    window.after(1000*random.randint(1,3), make_vibe)

#move vibes
def move_vibes():
    for vibe_num in range(len(vibe_list)):
        vibe = vibe_list[vibe_num-1]
        canvas.move(vibe, -vibe_speed, random.randint(-2, 2)*2)
        #check if end of screen - delete
        if canvas.coords(vibe)[0] < 0:
            canvas.delete(vibe)
            vibe_list.remove(vibe)
            vibe_type.pop(vibe_num-1)
        #keep moving
    window.after(50,move_vibes)


        
#function updates score
def update_score():
    #global vars
    global score
    score += 1
    score_display.config(text='Score :' + str(score))

def end_game():
    window.destroy()

def end_title():
    canvas.delete(title)
    canvas.delete(directions)

#check for collisions
def collision(i1, i2, dist):
    xdistance = abs(canvas.coords(i1)[0]-canvas.coords(i2)[0])
    ydistance = abs(canvas.coords(i1)[1]-canvas.coords(i2)[1])
    overlap = xdistance <dist and ydistance < dist
    return overlap

#checks if the player hit vibes, update based on vibe hit
def vibe_hit():
    #Check if you hit each vibe
    for vibe_num in range(len(vibe_list)):
        vibe = vibe_list[vibe_num-1]
        if collision(char, vibe, 30):
            #change canvas collor to match vibe
            canvas.configure(bg =vibe_type[vibe_num-1])
            #delete the vibe
            canvas.delete(vibe)
            vibe_list.remove(vibe)
            vibe_type.pop(vibe_num-1)
            #update the score
            update_score()
    window.after(100, vibe_hit)

#player movement/quiting
move_dir = 0

def check_input(event):
    global move_dir
    key = event.keysym
    if key == "Up":
        move_dir = "Up"
    elif key == "Down":
        move_dir = "Down"
    elif key == "q":
        game_over = canvas.create_text(300,200,text = "Goodbye!", fill = 'black', font = ('Helvetica', 50))
        window.after(2000, end_game())
        return
    
def end_input(event):
    global move_dir
    move_dir = "None"

def move_char():
    if move_dir == "Down" and canvas.coords(char)[1]<400 :
        canvas.move(char, 0, 10)
    if move_dir == "Up" and canvas.coords(char)[1] > 0:
        canvas.move(char, 0, -10)
    window.after(16, move_char)

canvas.bind_all('<KeyPress>', check_input)
canvas.bind_all('<KeyRelease>', end_input)

window.after(3000, end_title)
window.after(3000, make_vibe)
window.after(3000, move_vibes)
window.after(3000, vibe_hit)
window.after(3000, move_char)
        
    
window.mainloop()
