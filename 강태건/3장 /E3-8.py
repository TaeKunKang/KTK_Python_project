x=int(input("숫자를 입력하세요:"))
y=int(input("숫자를 입력하세요:"))
print("원하는 연산은?")
z=input("+.-,*,/ 중 하나를 선택하세요:")
if z=="+":
    result=int(x)+int(y)
elif z=="-":
    result=int(x)-int(y)
elif z=="*":
    result=int(x)*int(y)
elif z=="/":
    result=int(x)/int(y)
else:
    result="선택오류"
print(result)



