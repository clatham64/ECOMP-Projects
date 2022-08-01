#get turtle running
import turtle
import random

#initialize variables
i = 0 #index 1
n = 0 #index 2
colors = ['blue', 'white', 'purple', 'cyan', 'green', 'orange'] #color wheel
turt=turtle.Turtle() #turtle
rand_val = random.randrange(0,4) #random number
turt.color(colors[rand_val]) #set a random color
n_max = 0 #index for n based on random value
n_max = rand_val+3

#set bg color
turtle.bgcolor('black')

for i in range(36):
    print(n_max)
    for n in range(n_max):
        turt.color(colors[n%6])
        turt.forward(100)
        turt.left(360/n_max)
    turt.penup()
    rand_val = random.randrange(0,4) #random number
    turt.color(colors[rand_val]) #set a random color
    n_max = rand_val+3
    turt.forward(45*n_max)
    turt.pendown()
    turt.circle(10*n_max)
    turt.penup()
    turt.backward(45*n_max)
    turt.pendown()
    turt.right(10)

turt.hideturtle()
    
    
