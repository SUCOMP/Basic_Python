import turtle

t = turtle.Turtle()

t.shape("turtle")



while True:
    명령 = input("명령을 입력하세요 : ")
    if 명령 == "r" :
        t.left(90)
        t.forward(100)
    if 명령 == "l" :
        t.right(90)
        t.forward(100)
