import turtle

import random

t = turtle.Turtle()

t.shape("turtle")

t.speed(10)

for i in range(50):
    length = random.randint(1,100)
    angle = random.randint(0,360)
    
    t.left(angle)
    t.fd(length)
