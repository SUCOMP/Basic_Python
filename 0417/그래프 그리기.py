import turtle

t = turtle.Turtle()

t.shape("turtle")

Shape = turtle.textinput("Python Turtle Graph","도형을 입력하세요(삼각형,사각형,원)")

if Shape == "사각형" :
    가로 = int(turtle.textinput("Python Turtle Graph","가로"))
    세로 = int(turtle.textinput("Python Turtle Graph","세로"))
    t.forward(가로)
    t.right(90)
    t.forward(세로)
    t.right(90)
    t.forward(가로)
    t.right(90)
    t.forward(세로)

elif Shape == "삼각형" :
    크기 = int(turtle.textinput("Python Turtle Graph","크기"))
    t.forward(크기)
    t.left(120)
    t.forward(크기)
    t.left(120)
    t.forward(크기)
else :
    크기 = int(turtle.textinput("Python Turtle Graph","크기"))
    t.circle(크기)
