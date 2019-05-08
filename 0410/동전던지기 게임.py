import random

print("동전던지기 게임을 시작합니다.")
ran = random.randrange(2)

if ran == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")

print("게임이 종료됩니다.")
