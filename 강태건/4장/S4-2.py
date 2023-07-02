
while True:
    x=int(input("점수를 입력하세요:"))
    if x>0 and x<59:
        print("등급:가")
    elif x>60 and x<69:
        print("등급:양")
    elif x>70 and x<79:
        print("등급:미")
    elif x>80 and x<89:
        print("등급:우")
    else:
        print("등급:수") 
    z=print("계속하시겠습니까?(중단:q,계속:y)")
    if z=="q":
        break

