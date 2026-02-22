from turtle import Turtle, Screen
import random

# screen.colormode(255) 

tim = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

direction = [ 0, 180, 270, 90]
tim.pensize(15)
tim.speed("fastest")
for _ in range(350):
    tim.color(random_color())
    tim.forward(30)
    tim.right(random.choice(direction))



screen.exitonclick()

