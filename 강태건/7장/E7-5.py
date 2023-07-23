x=1
y=2
z=3
a=4
print("-선택옵션?")
print("%d.더하기" %x)
print("%d.빼기" %y)
print("%d.곱하기" %z)
print("%d.나누기" %a)
b= int(input("원하는 연산을 선택하세요(1/2/3/4):"))
c= int(input("첫 번째 숫자를 입력하세요:"))
d= int(input("두 번째 숫자를 입력하세요:"))
if b==x:
    print(c+d)
elif b==y:
    print(c-d)
elif b==z:
    print(c*d)
elif b==a:
    print(c/d)
else:
    print("오류")
