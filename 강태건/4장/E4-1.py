count=0
for i in range(201,800):
    if i%5!=0:
        print("%d"%i, end=" ")
        count= count+1
        if count%10==0:
            print()