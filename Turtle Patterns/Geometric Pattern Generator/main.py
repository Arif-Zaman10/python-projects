from turtle import Turtle, Screen
import random


tim = Turtle()

loop = 0
angle = 3
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
while loop<8:
    tim.color(random.choice(colors))
    for i in range(angle):
        tim.forward(100)
        tim.right(360/angle)

    loop += 1
    angle += 1


screen = Screen()
screen.exitonclick()