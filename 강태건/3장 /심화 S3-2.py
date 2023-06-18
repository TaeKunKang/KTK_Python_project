x=int(input("첫번째 시간의 시를 입력하세요:"))
y=int(input("첫번째 시간의 분을 입력하세요:"))
a=int(input("두번째 시간의 시를 입력하세요:"))
b=int(input("두번째 시간의 분을 입력하세요:"))
if x<a:    
    print("-빠른 시간: %d:%d" %(x,y))
    print("-늦은 시간: %d:%d" %(a,b))
elif x>a:
    print("-빠른 시간: %d:%d" %(a,b))
    print("-늦은 시간: %d:%d" %(x,y))
elif x==a and y<b:
    print("-빠른 시간: %d:%d" %(x,y))
    print("-늦은 시간: %d:%d" %(a,b))
elif x==a and y>b:
    print("-빠른 시간: %d:%d" %(a,b))
    print("-늦은 시간: %d:%d" %(x,y))
else:
    print("시간이 같아요!")
 