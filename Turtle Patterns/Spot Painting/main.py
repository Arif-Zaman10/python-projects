# import colorgram 

# colors = colorgram.extract('Turtle Projects\Spot Painting\spot_painting_hirst.jpg',30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), 
 (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), 
 (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), 
 (151, 176, 164), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 98), (213, 184, 173), 
 (145, 116, 121), (176, 197, 202)]

# start drawing from bottom left
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(10):  # 10 rows
    for _ in range(10):  # 10 dots per row
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen.exitonclick()
