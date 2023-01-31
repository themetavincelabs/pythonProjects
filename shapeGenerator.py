#import turtle & screen module
from turtle import Turtle, Screen
import random

tim = Turtle()

#from https://trinket.io/docs/colors
colors = ["royal blue", "dark slate gray", "light salmon"]


#use angels to draw shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)