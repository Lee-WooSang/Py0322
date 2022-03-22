# if else

score = int(input("점수를 입력:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "D"

print("등급은 ", grade)

# 반복구문
value = 5
while value > 0:
    print(value)
    value -= 1

print("---실행종료---")

# 시퀀스 형식
for i in ["100", "apple", 3.14]:
    print(i, type(i))

