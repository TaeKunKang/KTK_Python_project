x=(input("이름를 입력하세요:"))
y=int(input("일주일간 일한 시간을 입력하세요:"))
z=int(y)-40
if y>40:
    result=12000*(int(y)-40)*1.5+480000
else:
    result=12000*int(y)
print("이름: %s" %x)
print("일주일간 일한 시간: %d" %y)
print("오버타임: %d" %z)
print("주급: %d원" %result)



