number=[7,9,15,18,30,-3,7,12,-16,-12]
sum=0
i=1
while i<(len(number)):
    sum=sum+number[i]
    print("짝수이 요소:%d" %number[i])   
    i=i+2
print(sum)