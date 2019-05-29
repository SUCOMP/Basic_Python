import turtle as t

t.shape("turtle")

def square(length):
    for i in range(4):
        t.fd(length)
        t.left(90)

square(100)
t.pu()
t.goto(-200,0)
t.pd()
square(100)
t.pu()
t.goto(200,0)
t.pd()
square(100)

