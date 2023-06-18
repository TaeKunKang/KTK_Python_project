## 자료형

##### 🔥 변수명

> 문자열 안에서의 변수 사용

```py
    x=35
    print(x)

    a=15
    b=37
    c=int(a)+int(b)
    print(c)

    school= "한국대학교"
    print(school)
```
##### 🔥 숫자와 연산자

> 사칙연산, 실수

```py
    5+3-(-12)
    20

    a=1/3
    print(a)
    
    a=5+3*2
    11

    a=10%3
    print(a)
    1
```
##### 🔥 문자열 

> 문자열 추출,연결,반복,문자열 길이, 포맷팅

```py
    s="안녕히계세요, 반감습니다."
    s[0]
    '안'

    print("성적:"+str(score))
    성적: 80

    x="토끼"*10
    print(x)
    토끼토끼토끼토끼토끼토끼토끼토끼토끼토끼토끼토끼

    x="가는 말이 고와야 오는 말이 곱다."
    n=len(x)
    print("문자열의 길이:"+str(n))
    문자열의 길이: 19

    animal="cat"
    x="나는 %s를 좋아합니다" %animal
    print(x)
    나는 고양이를 좋아합니다
```
##### 🔥 키보드 입력

> input

```py
    a=input("첫번째 정수를 입력하세요")
    b=input("두번째 정수를 입력하세요")
    c=a+b
    print(c)
```
##### 🔥 화면출력

> sep

```py
name= "홍진영"
print(name)

a=10
b=20
print(a,b,a-b,100)

year= 2021 
month= 11
day= 15 
print(year, month, day, sep="/")

hp1="010"
hp2="1234"
hp3="5678"
print(hp1, hp2, hp3, sep="-")

price= 1000
print(price,"원")

print(price, "원", sep="")
```
##### 🔥 주석문

> 주석문 익히기

```py
    name= input("whats your name?")
    birth= int(input("당신이 태어난해?"))
    age= 2023- birth+1
    print("%s님의 나이는 %d세입니다." %(name, age))

    name= input("what's your name?")    #변수 name= 이름
    birth= int(input("당신이 태어난 해는?")) # 변수 birth= 탄생년
    age= 2023-birth
    print("%s의 나이는 %d입니다" %(name, age))
```
