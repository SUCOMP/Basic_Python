import turtle as t

n = int(input("몇각형?"))
t.speed(1000)

def n_shape(k):
    for j in range(k):
        t.left(360/k)
        for i in range(n):
            t.fd(100)
            t.left(360/n)


n_shape(100)
