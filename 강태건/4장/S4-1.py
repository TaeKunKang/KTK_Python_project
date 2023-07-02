count=0
i=0
while i<=999:
    i=i+1
    if i%3!=0:
        print("%d" %i, end=" ")
        count=count+1
        if count%10==0:
            print()


