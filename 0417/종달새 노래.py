import random
time = random.randint(1,24)
sunny = random.choice([True,False])

if 6 <= time <= 9 and sunny == True :
     print("종달새가 노래를 합니다.")
else :
    print("종달새가 노래를 하지 않습니다.")
