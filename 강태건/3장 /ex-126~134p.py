print("="*50)
now_year=int(input("현재년은?"))
now_month=int(input("현재월은?"))
now_day=int(input("현재일은?"))
birth_year=int(input("출생년은?"))
birth_month=int(input("출생월은?"))
birth_day=int(input("출생일은?"))
if birth_month<now_month:
    age=now_year-birth_year
elif birth_month==now_month:
    if birth_day<now_day:
        age=now_year-birth_year
    else:
        age=now_year-birth_year-1
else:
    age= now_year-birth_year-1
print("="*50)
print("오늘날짜: %d년%d월%d일" %(now_year, now_month, now_day))
print("생년월일: %d년%d월%d일" %(birth_year, birth_month, birth_day))
print("-"*50)
print("만나이:%d세" %age)
print("="*50)


spend=int(input("구매 금액은?"))
if spend>=10000 and spend<50000:
    rate=5.0
elif spend>=50000 and spend<300000:
    rate=7.5
elif spend>=300000:
    rate=10.0
else:
    rate=0
discount=spend*rate/100
pay=spend-discount
print("구매가격: %.0f" %spend)
print("할인율: %.1f" %rate)
print("할인금액: %.0f" %discount)
print("지불금액: %.0f" %pay)

print("서비스 만족도:")
print(" 1.매우 만족")
print(" 2.만족")
print(" 3.불만족")
a=input("서비스 만족도는?(1/2/3)")
price= int(input("음식 값은?"))

if  a==1:
    tip=int(price*0.2)
    servie="매우 만족"
elif a==2:
    tip=int(price*0.1)
    servie="만족"
else:
    tip=0
    service="불만족"
print("서비스 만족도:%s, 팁:%d" %(service,tip))