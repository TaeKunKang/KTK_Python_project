def say_hello(name):
    print("%s님 안녕하세요!" %name)
say_hello("홍지수")
say_hello("안지영")
say_hello("황예린")

def print_name(first_name, last_name):
    name=first_name+last_name
    print("이름:",name)
print_name("홍", "정원")

def f(n):
    if n%2==0:
        print("%d은 짝수이다." %n)
    else:
        print("%d은 홀수이다" %n)
x=int(input("양의 정수를 입력하세요:"))
f(x)

def f(n):
    if n%2==0:
        print("%d is even" %n)
    else:
        print("%d is odd" %n)
x=int(input("양의 정수를 입력하세요:"))
f(x)
#print(n)    #오류

def average(*args):
    num_args=len(args)
    sum=0
    for i in range(num_args):
        sum =sum+args[i]
    avg=sum/num_args
    print("%d과목 평균:%.1f" %(num_args, avg))
average(85.96,87)
average(77,93,85,97,72)

def func(food):
    for x in food:
        print(x)
fruits=["사과","오렌지","바나나"]
func(fruits)

def func(food):
    food.append("딸기")
    food.append("수박")
fruit=["사과", "오렌지", "바나나"]
print(fruits)
func(fruits)
print(fruits)
