def is_prime(n):
    prime= True
    if n>1:
        for i in range(2,n):
            if n%i==0:
                prime=False 
    return prime
number=int(input("수를 입력하세요:"))
if is_prime(number):
    print("소수이다!")
else:
    print("소수가 아니다!")


def square_sum(n):
    sm=0
    for i in range(1,n+1):
        sm=sm+(i*i*i)
    return sm
N=int(input("N의값을 입력하세요:"))
print(square_sum(N))
