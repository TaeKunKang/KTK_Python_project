x= int(input("양의 정수를 입력하세요"))
if x%2==0:
    print("짝수이다")
else:
    print("홀수이다")

p= int(input("필기시험 점수는?"))
s= int(input("실기시험 점수는?"))
if p>=80 and s>=80:
    result= "합격하셨습니다"
else:
    result= "불합격하셨습니다"
print(result)

char=input("영소문자를 적으세요")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("모음이다")
else:
    print("자음이다")

height= int(input("키는?"))
weight= int(input("몸무계는?"))
s=(height-100)*0.9
print("="*100)
print("키:", height)
print("몸무계", weight)
if weight>s:
    print("비만")
else:
    print("표준이나 마름")

