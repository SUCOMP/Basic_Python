score = int(input("당신의 점수를 입력하세요 : "))

if score >= 90:
    print("당신의 듭급은 A입니다.")
if 80 <= score and score < 90:
    print("당신의 듭급은 B입니다.")
if 70 <= score and score < 80:
    print("당신의 듭급은 C입니다.")
if 60 <= score and score < 70:
    print("당신의 듭급은 D입니다.")
if score < 60:
    print("당신의 듭급은 F입니다.")
