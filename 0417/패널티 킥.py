import random

Save = random.choice(["왼쪽","중앙","오른쪽"])

Kick = input("어디로 킥을 하시겠어요?(왼쪽,중앙,오른쪽) : ")

if Kick == Save :
    print("패널티 킥이 실패하였습니다.")
else :
    print("패널티 킥이 성공하였습니다.")
