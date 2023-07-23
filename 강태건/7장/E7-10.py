print("-선택옵션")
print("1.길이 환산(센티미터 --> 인치)")
print("2.무게 환산(킬로그램 --> 파운드)")
x=int(input("원하는 환산 단위를 선택하세요(1/2):"))
def func(km):
    if x==1:
        cm=km*0.393701
        return cm
h=int(input("센티미터의 단위를 길이를 입력하세요:"))
print("%d센티미터-->%.2f인치" %(h, func(h)))
def func(kg):
    if x==2:
        p=kg*2.204623
        return p
k=int(input("킬로그램의 단위를 길이를 입력하세요:"))
print("%d센티미터-->%.2f인치" %(k, func(k)))


