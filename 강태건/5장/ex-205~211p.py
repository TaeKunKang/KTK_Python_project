string1="python is fun!"
print(string1)
x=string1.find("fun")
print(x)

string1="사과는 맛있다. 나는 사과를 좋아한다"
print(string1)
x=string1.replace("사과","딸기")
print(x)

phone1="010-3654-8289"
print(phone1)
phone2=phone1.replace("-","")
print(phone2)

hello="have a nice day"
print(hello)
list1=hello.split(" ")
print(list1)
print(type(list1))

names=["황예린","홍지수","안지영"]
print(names)
x="/".join(names)
print(x)

sentences=["Love me, love me dog.", "No news is good news","Blood is thicker than water"]
for sentence in sentences:
    x=sentence.replace(" ", "_")
    print(x)