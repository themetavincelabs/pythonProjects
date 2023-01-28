#import turtle & screen module
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def drawSpirograph(sizeOfGap):
    for i in range(int(360 / sizeOfGap)):
        tim.color(randomColor())
        tim.circle(100)  # radius
        tim.setheading(tim.heading() + sizeOfGap)

drawSpirograph(5)



#screen upload
screen = t.Screen()
screen.exitonclick()