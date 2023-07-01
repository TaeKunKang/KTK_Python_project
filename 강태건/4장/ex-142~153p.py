for x in range(5):
    print("안녕하세요")

sum=0
for i in range(1,11):
    sum=sum+i
    print("i의 값: %d => 합계: %d" %(i,sum))

for i in range(10):
    print(i, end="")
print()
for i in range(1,11):
    print(i, end="")
print()
for i in range(2,10,2):
    print(i, end="")
print()
for i in range(20,0,-2):
    print(i, end="")
    
year=2021 
month=10
day=20
print(year, end="/")
print(month,end="/")
print(day)

sum=0
for i in range(100,201,5):
    sum=sum+i
print("5의 배수의 합걔: %d" %sum)

sum=0 
for i in range(100,201):
    if i%5==0:
        sum=sum+i
print("5의 배수의 합: %d" %sum)

word= input("영어 문장을 입력하세요:")
for x in word:
    print(x)
    
phone= input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요:")
for x in phone:
    if x!="-":
        print("%s"%x, end="")

print("-"*30)
print(" 섭씨 화씨")
print("-"*30)
for c in range(-20,31,5):
    f=c*9.0/5.0+32.0
    print("%5d %6.1f" %(c,f))
print("-"*30)

