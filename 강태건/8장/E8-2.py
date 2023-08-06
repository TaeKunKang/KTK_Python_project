n=int(input("N값을 입력하세요:"))
def sum(n):
    total =0
    for i in range(1,1001):
        if i%n==0:
            total = total+i
    return total
print(sum(n))


