x=int(input("점수를 입력하세요:"))
if x>0 and x<59:
    result="성적:%d점, 등급:가" %x
elif x>60 and x<69:
    result="성적:%d점, 등급:양" %x
elif x>70 and x<79:
    result="성적:%d점, 등급:미" %x
elif x>80 and x<89:
    result="성적:%d점, 등급:우" %x
elif x>90 and x<100:
    result="성적:%d점, 등급:수" %x
else:
    result="입력 오류!"
print(result)
