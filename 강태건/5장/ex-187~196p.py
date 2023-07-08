colors=["빨간색","파란색","노란색","검정색","초록색"]
for color in colors:
    print(color)

colors=["빨간색","파란색","노란색","검정색","초록색"]
n=len(colors)
for i in range(0,n):
    print(colors[i])

animals=["코끼리","호랑이","사슴","팽권","여우"]
i=0
while i <len(animals):
    print(animals[i])
    i=i+1

flowers=["목련","벗꽃","장미","백일홍"]
print(flowers)
flowers[1]="무궁화"
print(flowers)

arr=[1,3,5,4,25]
print(arr)
arr.append(10)
print(arr)

scores=[]
while True:
    score=int(input("성적을 입력하세요(종료:-1):"))

    if score==-1:
        break
    else:
        scores.append(score)
print(scores)

fruits=["apple","orange","banana","cherry"]
print(fruits)

fruits.insert(1,"melon")
print(fruits)
fruits.insert(2,"strawberry")
print(fruits)

number=[5,20,13,7,8,22,7,17]
print(number)
idx=number.index(7)
print(idx)

member=["홍진웅", 20,"경기도 김포시","jiwoong@naver.com","010-1234-5679"]
print(member)
member.remove(20)
print(member) 

data=[10,20,30,40,50,60,70,80]
print(data)
x=data.pop(2)
print(x)
print(data)
x=data.pop(3)
print(x)
print(data)

data=[3,12,7,-3,-9]
print(data)
data.clear()
print(data)