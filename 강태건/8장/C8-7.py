def binary_search(n,x):
    start=0
    end=len(n)-1
    while start <= end:
        mid=(start+end)//2
        if x==n[mid]:
            return mid
        elif x>n[mid]:
            end= mid+1
        else:
            start=mid-1
    return -1
data=[93,91,89,87,80,61,55,43,41,38,32,30,25,20,8,2]
print(data)
search_num=89
index=binary_search(data,search_num)
print("%d의 인덱스번호: %d" %(search_num, index))