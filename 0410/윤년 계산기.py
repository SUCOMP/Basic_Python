Years = int(input("연도를 입력하시요 : "))

if (Years % 4 == 0 or Years % 400 == 0) and Years % 100 != 0:
    print(Years,"년은 윤년입니다.")
else:
    print(Years,"년은 윤년이 아닙니다.")
