import random
x=["가위","바위","보"]
print("============================")
print("가위바위보 게임")
print("============================")
while True:
    a=random.choice(x)
    b=random.choice(x)
    if a==b:
        print("나:", a)
        print("당신:", b)
        print("무승부입니다")
        print("-"*10)
    elif a=="가위" and b=="보":
        print("나:", a)
        print("당신:", b)
        print("나의 승리입니다")
        print("-"*10)
    elif a=="바위" and b=="가위":
        print("나:", a)
        print("당신:", b)
        print("나의 승리입니다")
        print("-"*10)
    elif a=="보" and b=="바위":
        print("나:", a)
        print("당신:", b)
        print("나의 승리입니다")
        print("-"*10)
    else:
        print("나:", a)
        print("당신:", b)
        print("나의 패배입니다")
        print("-"*10)

    g=input("계속하려면 y를 입력하세요!")
    if g!="y":
        break 
