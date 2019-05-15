import turtle

t = turtle.Turtle()

t.shape("turtle")

n = int(turtle.textinput("각형그리기","몇각형을 그리겠습니까?"))

for i in range(n):
    t.left(360/n)
    t.fd(100)
