x=int(input("정수를 입력하세요 :"))
if x>0:
    print("양수")

x=int(input("정수입력:"))
if x==5:
    print("true")
else: 
    print("false")

x=int(input("정수를 입력하세요"))
if x%2==0:
    result= "2의 배수이다"
else:
    result= "2의 배수가 아니다"
print (result)

ans1= input("사자의 영어 단어는 무엇일까요?")
result= "땡 틀렸습니다"
if ans1=="lion":
    result= "정답입니다"
print(result)

ans2= input("what is orange in korean?")
result= "틀렸습니다"
if ans2=="오렌지":
    result="정답입니다"
print(result)


ans3= int(input("이 정수를 입력하시요"))
ans4= input("입력한 정수가 짝수인지 홀수인지 정의하세요")
if ans3%2==0:
    result= "짝수"
else:
    result= "홀수" 
if ans4==result:
    result2="정답입니다"
else:
    result2="오답입니다"  
print(result2)

a=int(input("주민번호 뒷자리 첫번째 숫자를 입력헤주세요"))
if a==1 or a==3:
    print("남성입니다")
if a==2 or a==4:
    print("여성입니다")

month= input("월을 숫자로 입력하세요:")
if month=="3" or month=="4" or month=="5":
    print("%s월은 봄입니다" %month)
if month=="6" or month=="7" or month=="8":
    print("%s월은 여름입니다" %month)
if month=="9" or month=="10" or month=="11":
    print("%s월은 가을입니다" %month)
if month=="12" or month=="1" or month=="2":
    print("%s월은 겨울입니다" %month)


