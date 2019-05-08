import turtle

t = turtle.Turtle()

t.shape("turtle")

color_list = ["yellow","red","blue","green"]
t.fillcolor(color_list[0])#채울 색깔
t.begin_fill()#채우기 시작
t.circle(100)#원그리기
t.end_fill()#채우기 끗

t.fd(50)
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(50)
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(50)
t.fillcolor(color_list[3])
t.begin_fill()
t.circle(100)
t.end_fill()
