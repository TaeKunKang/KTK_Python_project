year= input("년은?")
month= input("달은?")
day= input("일은?")
print(year,month,day,sep=".") 

w=int(input("사각형의 너비는?"))
h=int(input("사각형의 높이는?"))
L= 2*w +2*h
A= w*h 
print("사각형의 너비: %dcm" % (w))
print("사각형의 높이: %dcm" % (h))
print("둘레길이: %dcm" % (L))
print("면적: %dcm2" % (A))

r= float(input("반지름을 입력하세요:"))
length= 2*r*3.14
area= r**2*3.14
print("반지름: %.2fcm" %r)
print("원의둘레: %.2fcm" %length)
print("원의면적: %.2fcm2" %area)

inch=float(input("인치는?"))
cm= inch*2.54
print("%.1finch => %.2fcm" %(inch, cm))

price= int(input("책값은?:"))
discount=float(input("할인률은?"))
delivery=int(input("배송비는?"))
pay= price-(price*(discount/100))+ delivery
print("책값: %d원" %price)
print("할인률 %f" %discount)
print("배송비 %d원" %delivery)
print("결제금액 %d원" %pay)