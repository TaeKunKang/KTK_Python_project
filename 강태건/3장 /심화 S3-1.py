x=(input("등급를 입력하세요:"))
if x=="A+":
    result="등급:%s, 평점:4.5" %x
elif x=="A":
    result="등급:%s, 평점:4.0" %x
elif x=="B+":
    result="등급:%s, 평점:3.5" %x
elif x=="B":
    result="등급:%s, 평점:3.0" %x
elif x=="C+":
    result="등급:%s, 평점:2.5" %x
elif x=="C":
    result="등급:%s, 평점:2.0" %x
elif x=="D+":
    result="등급:%s, 평점:1.5" %x
elif x=="D":
    result="등급:%s, 평점:1.0" %x
elif x=="F":
    result="등급:%s, 평점:0" %x
else:
    result="입력 오류!"
print(result)