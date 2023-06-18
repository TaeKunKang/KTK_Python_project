##### 🔥 조건문

> If문의 세가지 구문

```py
if~구문 
=만약 조건을 만족하면 ~작업을 수행하라

if~else~구문 
=만약 조건을 만족하면 ~작업을 수행하고, 그렇지 않으면 ~작업을 수행하라 

if~elif~else~구문
= 만약 조건1을 만족하면 작업1을 수행하고 조건2를 만족하면 작업2를 수행하고, 조건3을 만족하면 작업3을 수행하고,...,그렇지 않으면 작업 n을 수행하라.
```
##### 🔥 비교 연산자와 논리 연산자

> 연산자

```py
    비교 연산자= <,>,>=,<=,!=
    논리 연산자= and, or, not

    x=int(input("정수를 입력하세요 :"))
    if x>0:
        print("양수")

    x=int(input("정수입력:"))
    if x==5:
        print("true")
    else: 
        print("false")
```
##### 🔥 if~ 구문

> 기본구조,예제

```py
    ans1= input("사자의 영어 단어는 무엇일까요?")
    result= "땡 틀렸습니다"
    if ans1=="lion":
        result= "정답입니다"
    print(result)

    ans2= input("what is orange in korean?")
    result= "틀렸습니다"
    if ans2=="오렌지":
        result="정답입니다"
    print(result)    
```
##### 🔥 if~else~구문

> 판별,판정에대한예제

```py
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
```
##### 🔥 if~elif~else~구문

> 기본구조,예제

```py
    score=int(input("score?:"))
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    print(grade)
```
##### 🔥 if문의 중첩

> 기본 구조

```py
    if 조건식:
        <문장들>
    elif 조건식:
        if 조건식:
            <문장들>
        else:
            <문장들>
    else:
        <문장들>    
```
##### 🔥 조건문

> 

```py
    
```