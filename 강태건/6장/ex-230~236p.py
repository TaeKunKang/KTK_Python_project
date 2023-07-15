animals=("토끼","거북이","사자","여우")
print(animals)
numbers=tuple(range(10))
print(numbers)

n=tuple(range(10,21))
print(n)
print("n[0]=", n[0])
print("n[2:5]=", n[2:5])
print("n[2:]=", n[2:])
print("n[:5]=", n[:5])
print("n[-2]=", n[-2])
print("n[::-1]=", n[-1])

tup1=(10,20,30,40,50)
for i in range(len(tup1)):
    print(tup1[i])

tup1=(10,20,30)
tup2=(40,50,60)
tup3=tup1+tup2
print(tup3)

admin_info=("admin","12345","webmaster@naver.com")
print("관리자정보")
print("아이디:" +admin_info[0])
print("비밀번호:" +admin_info[1])
print("이메일:" +admin_info[2])


