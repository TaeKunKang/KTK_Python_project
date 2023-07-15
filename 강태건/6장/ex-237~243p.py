member={"name":"황예린", "age":22, "email":"yerin@hanmail.net"}
print(member)
score=dict([("국어",80),("영어",90),("수학",100)])
print(score)

user={"id":"kim55", "name":"강성준", "level":7, "point":10000}
print(user)
print(user["id"])
print(user["name"])
print(user["point"])

score={"kor":90,"eng":89,"math":98}
print(score)
score["music"]=100       #추가
print(score)

words={"door":"문","chair":"의자", "table":"책상","house":"집"}
print(words)
words["table"]="테이블"
print(words)
words["house"]="하우스 "
print(words)

car={"brand":"현대","model":"아반떼","start":1990,"year":2021}
print(car)
x=car.pop("start")     #pop() 삭제 
print(x)
print(car)

car={"brand":"현대","model":"아반떼","start":1990,"year":2021}
print(car)
car.clear()           #clear() 모두 삭제
print(car)

area_code={"서울":"02","부산":"051","대구":"053","광주":"062"}
for key in area_code: #반복 루프에서 key는 area_code의 키의 의미
    print("%s지역번호:%s" %(key, area_code[key]))


















