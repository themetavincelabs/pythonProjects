#import turtle & screen module
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

#randomWalk

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColor = (r, g, b)
    return randomColor
#directions
directions = [0, 90, 180, 370]
tim.pensize(15)
tim.speed("fastest")



#loop 200x for tim to go forward 30 degrees and to turn at random angles
for i in range(100):
    tim.color(randomColor())
    tim.forward(30)
    tim.setheading(random.choice(directions))


#colors = ["lime", "red","medium slate blue"]