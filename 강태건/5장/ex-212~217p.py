numbers=[[10,20,30],[40,50,60,70,80]]
print(numbers[0][0])
print(numbers[0][1])
print(numbers[0][2])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])
print(numbers[1][3])
print(numbers[1][4])

data=[[10,20],[30,40],[50,60],[70,80]]
for i in range(4):
    for j in range(2):
        print("data[%d][%d]=%d" %(i,j,data[i][j]))

scores=[[75,83,90],[86,86,73],[76,95,83],[89,96,69],[89,76,93]]
for i in range(len(scores)):
    sum=0
    for j in range(len(scores[i])):
        sum=sum+scores[i][j]

scores=[[75,83,90],[86,86,73],[76,95,83],[89,96,69],[89,76,93]]
for i in range(len(scores)):
    sum=0                                                                                                                                      
    for j in range(len(scores[i])):
        sum=sum+scores[i][j]
    avg=sum/len(scores[i])
    print("%d번째 학생의 합계: %d,평균: %.2f" %(i+1,sum,avg))
    
strings=[["원두커피","라떼","콜라"],["우동","국수","피자","파스타"]]
for i in range(len(strings)):
    for j in range(len(strings[i])):
        print(strings[i][j])
    
