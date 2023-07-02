##### 🔥 반복문

> 반복문의 2가지 구문

```py
    반복문은 같은 블록의 코드를 반복해서 수행할 때 사용된다. 
    1. for 문 
        for는 '~하는 동안'이란 의미를 갖는다. 파이썬을 포함한 많은 프로그래밍 언어에서 사용되는 for문은 조건에 따라 문장들을 반복 수행하게 된다.  
    2. while 문 
        while문은 for과 함께 많이 사용되는 반복문으로서 사용 형태는 다음과 같다.
```
##### 🔥 for문의 3가지 형식

> 형식

```py
    1. for 변수 in range(종료값):
            문장1, 문장2, ...
    2. for 변수 in range(시작값, 종료값):
            문장1, 문장2, ...
    3. for 변수 in range(시작값, 종료값, 증가_감소):
            문장1, 문장2, ...
```
##### 🔥 while문의 형식

> 형식

```py
    변수_초기화

    while 조건식:
        문장1
        문장2
        ...
        변수값_중가_감소
```
##### 🔥 이중 for문 

> 구구단표 만들기

```py
    이중 for문은 for문을 이중으로 사용하는 것을 말한다. 2단에서 9단까지의 구구단 표를 만드는 과정을 통하여 이중 for문의 사용법을 익혀보자!
1.
        a=2
    for b in range(1,10):
        print("%d x %d= %d" %(a,b,a*b))
2.  
    print("-"*30)
    for a in range(2,10):
        for b in range(1,10):
            print("%d x %d= %d" %(a,b,a*b))
    print("-"*30)
```
##### 🔥 while문 break

> break문을 사용하여 빠져나가기

```py
    for문이나 while문을 사용하다 보면 반복 루프를 수행 중 중간에 루프를 빠져나가고 싶은 경우가 종종 생긴다. 이 때 사용하는 것이 break문이다. 일반적으로 break문은 if문과 같이 사용되어 반복 루프가 진행되는 동안 조건식을 만족하면 반복 루프를 빠져 나가게 한다.
    
    형식
    for 변수 in range():
        문장1
        문장2
        ...
        if 조건식:
            break
1. 
    for i in range(1,1001):
        print(i)

        if i==10:
            break
```
##### 🔥 for문 예제

> 예제

```py
1.
    count=0
for i in range(201,800):
    if i%5!=0:
        print("%d"%i, end=" ")
        count= count+1
        if count%10==0:
            print()
2.
    print("-"*40)
print("   cm   mm   m   inch")
print("-"*40)
for cm in range(1,101):
    mm=cm*10.0
    m=cm*0.01
    inch=cm*0.3937
    print("   %d   %d   %.2f   %d" %(cm,mm,m,inch))  
3.
    for i in range(1,11):
    print("*"*i)
4.
    number=input("숫자를 입력하세요:")
total=0
for a in number:
    a=int(a)
    if a%2==1:
        total=total+1
print("홀수의 개수: %d개" %total)
5. 
    print("-"*50)
print("%7s %7s %7s" %("킬로그램", "파운드", "온스"))
print("-"*50)
for kg in range(100,201,2):
    pound= kg*2.204623
    ounce= kg*35.273962
    print("     %d        %.1f      %.1f" %(kg, pound, ounce))
print("-"*50)
```
##### 🔥 while문 예제

> 예제

```py
1.
    n=1
sum=0
count=0

while n<=100:
    if n%2==1:
        sum=sum+n
        print("%6d" %sum,end="")
        count=count+1
        if count%10==0:
            print()
    n=n+1
2.
    print("-"*30)
print("    달러   원화    유로")
print("-"*30)
dollar=10
while dollar<=100:
    won=dollar*1080
    euro=dollar*0.81
    print("%7d%8.0f%7.1f" %(dollar, won, euro))
    dollar=dollar+10
print("-"*30)
3.
    sentence=input("문장을 입력해주세요:")
i=len(sentence)-1
while i>=0:
    if sentence[i]==" ":
        print("-", end="")
    else:
        print("%s" %sentence[i], end="")
        i=i-1
```

