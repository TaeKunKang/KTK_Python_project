x=int(input("시작수를 입력하세요:"))
y=int(input("끝수를 입력하세요:"))
a=x
for i in range(x,y):
    i%a!=0
    print(i)