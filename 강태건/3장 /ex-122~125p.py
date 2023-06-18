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


print("function")
print("1.plus")
print("2.minus")
print("3.multiple")
print("4.divide")
s=input("choose calc's fuction(1/2/3/4):")
num1=int(input("첫번쨰 수 입력"))
num2=int(input("두번쨰 수 입력"))
num3=num1+num2
num4=num1-num2
num5=num1*num2
num6=num1/num2
if s=="1":
    print("%d+%d=%d"%(num1, num2, num3))
elif s=="2":
    print("%d-%d=%d"%(num1, num2, num4))
elif s=="3":
    print("%d*%d=%d"%(num1, num2, num5))
elif s=="4":
    print("%d/%d=%d"%(num1, num2, num6))
else:
    print("you did something wrong")



