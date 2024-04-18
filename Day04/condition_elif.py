#condition_elif.py


# num = int(input("점수 입력:"))
# if num >= 90:
#     print("A등급")
# elif num >= 80:
#     print("B등급")
# elif num >= 70:
#     print("C등급")
# else:
#     print("과락입니다...")

# guk = int(input("국어 점수 입력:"))
# eng = int(input("영어 점수 입력:"))
# mat = int(input("수학 점수 입력:"))
# avg = (guk+eng+mat)/3
# if avg >= 90:
#     print("A등급")
# elif avg >= 80:
#     print("B등급")
# elif avg >= 70:
#     print("C등급")
# elif avg >= 60:
#     print("D등급")
# else:
#     print("F입니다...")

# nested condition
# if 문의 depth는 2번까지 지향하는 걸로!
score = int(input("점수 입력:"))
if score >60:
    if score == 100:
        print("만점입니다")
    else:
        print("합격입니다!")
else:
    if score ==0:
        print("dddd")
    else:
        print("불합격입니다.")