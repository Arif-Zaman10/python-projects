from turtle import Turtle, Screen
import random



tim = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tim.speed("fastest")
tim.color(random_color())

current_heading = tim.heading()
while current_heading < 360:
    tim.circle(100)
    current_heading += 10
    tim.setheading(current_heading)

screen.exitonclick()

