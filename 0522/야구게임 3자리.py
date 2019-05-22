import random

list = []

for i in range(3):
    list.append(random.randint(1,9)) # 숫자 랜덤으로 3개 지정
print(list)

a = int(input("첫번째 숫자를 입력하세요 : "))
b = int(input("두번째 숫자를 입력하세요 : "))
c = int(input("세번째 숫자를 입력하세요 : ")) #숫자입력

if a not in list and b not in list and c not in list:
    print("노볼 노스트라이크")
    
elif a == list[0] and b not in list and c not in list:
    print("원스트라이크 노볼")
elif b == list[1] and a not in list and c not in list:
    print("원스트라이크 노볼")
elif c == list[2] and a not in list and b not in list:
    print("원스트라이크 노볼")
    
elif a == list[0] and b not in list and b != list[1] and c in list and c != list[2]:
    print("원스트라이크 원볼")
elif a == list[0] and c not in list and b in list and b != list[1]:
    print("원스트라이크 원볼")
    
elif b == list[1] and a not in list and c in list and c != list[2]:
    print("원스트라이크 원볼")
elif b == list[1] and c not in list and a in list and a != list[0]:
    print("원스트라이크 원볼")
    
elif c == list[2] and b not in list and a in list and a != list[0]:
    print("원스트라이크 원볼")
elif c == list[2] and a not in list and b in list and b != list[1]:
    print("원스트라이크 원볼")

elif a == list[0] and b in list and b != list[1] and c in list and c != list[2]:
    print("원스트라이크 투볼")

elif b == list[1] and a in list and a != list[0] and c in list and c != list[2]:
    print("원스트라이크 투볼")

elif c == list[2] and b in list and b != list[1] and a in list and a != list[0]:
    print("원스트라이크 투볼")

elif a == list[0] and b == list[1] and c not in list:
    print("투스트라이크")

elif a == list[0] and c == list[2] and b not in list:
    print("투스트라이크")

elif c == list[2] and b == list[1] and a not in list:
    print("투스트라이크")

elif a == list[0] and b == list[1] and c == list[2]:
    print("쓰리스트라이크")
