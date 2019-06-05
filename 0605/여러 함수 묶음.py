def Baesu_circulate():
    print("===================================================================")
    start = int(input("시작값 : "))
    end = int(input("끝값 : "))
    baesu = int(input("배수 : "))
    sum = 0
    for i in range(start,end+1):
        if i%baesu == 0:
            sum = sum + i
    print("%d에서 %d까지 %d의 배수의 합은 %d이다." %(start,end,baesu,sum))

def n_circulate():
    print("===================================================================")
    a = int(input("끝값 : "))
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
    print("1부터 %d까지의 합은 %d 입니다."%(a,sum))

def Gugu_circulate():
    print("===================================================================")
    Num = int(input("몇단을 표기할까요? : "))
    for i in range(1,10):
        print(Num,"*",i,"=",Num*i)
        
        
            


for i in range(10000):
    print("1. 1부터 n까지 정수의 합")
    print("2. n~m까지 k배수의 합")
    print("3. 구구단 출력")
    print("4. 종료")
    a = int(input("번호를 입력하세요. : "))
    if a == 1:
        n_circulate()
        print("===================================================================")
    if a == 2:
        Baesu_circulate()
        print("===================================================================")
    if a == 3:
        Gugu_circulate()
        print("===================================================================")
    if a == 4:
        print("종료되었습니다.")
        break


    
