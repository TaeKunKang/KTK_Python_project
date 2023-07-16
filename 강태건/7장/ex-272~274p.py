def func(n):
    x=n+5
    return x
a=func(10)
print(a)
b=func(20)
print(b)

def inch_to_cm(inch):
    cm=inch*2.54
    return cm 
num= int(input("인치를 입력하세요:"))
result= inch_to_cm(num)
print("%d inch => %.2f" %(num, result))