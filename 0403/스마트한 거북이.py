import turtle

t = turtle.Turtle()

t.shape("turtle")

t.penup()
t.goto(100,0)
t.write("0입니다.")
t.goto(100,100)
t.write("양수입니다")
t.goto(100,-100)
t.write("음수입니다.")

t.goto(0,0)

number = int(input("숫자를 입력하세요 : "))
if number >0:
    t.goto(100,100)
    t.write("양수입니다")

elif number == 0:
    t.goto(100,0)
    t.write("0입니다.")

else:
    t.goto(100,-100)
    t.write("음수입니다.")
