def func():
    m= km*0.621371
    return m
km= int(input("킬로미터를 입력하세요?:"))
print("%d킬로미터는 %.2f마일이다" %(km, func()))
