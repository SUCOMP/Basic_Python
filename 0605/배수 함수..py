start = int(input("시작값 : "))
end = int(input("끝값 : "))
baesu = int(input("배수 : "))

def Baesu_circulate(start,end,baesu):
    sum = 0
    for i in range(start,end+1):
        if i%baesu == 0:
            sum = sum + i
    print("%d에서 %d까지 %d의 배수의 합은 %d이다." %(start,end,baesu,sum))

Baesu_circulate(start,end,baesu)
