admin_info={"id":"admin","password":"12345"}
input_id=input("아이디를 입력하세요:")
input_pass= input("비밀번호를 입력하세요:")
if input_id=="admin" and input_pass=="12345":
    print("정보에 접근 권한이 있습니다!")
else:
    print("정보에 접근 권한이 없습니다!")