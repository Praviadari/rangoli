from turtle import *  # imports turtle

speed(1000)  # speed the cursor
bgcolor('black')  # background color
r, g, b = 255, 0, 0

for i in range(255 * 2):
    colormode(255)
    if i < 255 // 3:
        g += 3
    elif i < 255 * 2 // 3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255 * 4 // 3:
        g -= 3
    elif i < 255 * 5 // 3:
        r += 3
    else:
        b -= 3
    fd(50 + i)
    rt(91)
    pencolor(r, g, b)



import turtle
from turtle import color
import random


def pen(colour):
    turtle.color(colour)


def fireworks(size):
    for num in range(20):
        turtle.forward(size)
        turtle.rt(180 - (360 / 20))


def move():
    turtle.penup()
    x = random.randint(-800, -400) #range in x
    y = random.randint(-300, 400) #range in y
    turtle.goto(x, y)
    turtle.pendown()


def move1():
    turtle.penup()
    x = random.randint(400, 800)
    y = random.randint(-300, 300)
    turtle.goto(x, y)
    turtle.pendown()


turtle.bgcolor("black")
turtle.speed(0)

colors = ['red', 'yellow', 'blue', 'cyan', 'magenta', 'orange']
for _ in range(30):
    color = random.choice(colors)
    pen(color)
    fireworks(random.randint(50, 100))
    move()

colors = ['red', 'yellow', 'blue', 'cyan', 'magenta', 'orange']
for _ in range(30):
    color = random.choice(colors)
    pen(color)
    fireworks(random.randint(50, 100))
    move1()
