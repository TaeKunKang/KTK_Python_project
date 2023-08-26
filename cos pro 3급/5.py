count=0
l = list(map(int, input().split()))
m= int(input(""))
for i in range(0,6):
    if l[i]<m:
        count=count+1 
    else:
        count=count+0
print(count) 

