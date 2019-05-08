import turtle

t = turtle.Turtle()

n = int(input("몇각형 만들레?"))

for i in range(n):
    t.fd(100)
    t.left(360/n)
