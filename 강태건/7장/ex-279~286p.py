def func():
    x=100
    print(x)
func()

def func():
    x=100
    print(x)
func()
#print(x)   #x가 정의되지 않음

def func():
    print()
x=100
func()
print(x)

def func():
    global x    #여기서 x는 메인 루틴의 전역 변수임
    x=200
    print(x)
x=100
print(x)
func()
print(x)

def cir_area():
    global r
    result=r*r*3.14
    return result
def cir_length():
    global r
    result=2*3.14*r
    return result
r= float(input("반지름을 입력하세요:"))
area= cir_area()
length= cir_length()
print("원의 면적: %.1f, 원주의 길이: %.1f" %(area, length))

def cir_area():
    global r
    result=r*r*3.14
    return result
def cir_length():
    global r
    result=2*3.14*r
    return result
r= float(input("반지름을 입력하세요:"))
area= cir_area(r)     #인수 r
length= cir_length(r) # 인수 r
print("원의 면적: %.1f, 원주의 길이: %.1f" %(area, length))
