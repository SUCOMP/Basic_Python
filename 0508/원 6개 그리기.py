import turtle

t = turtle.Turtle()

t.speed(20)

n = int(input("원 몇개 그리고 싶뉘?: "))

for i in range(n):
    t.left(360/n)
    t.circle(200)
