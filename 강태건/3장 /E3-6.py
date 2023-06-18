x=int(input("숫자를 입력하세요.:"))
if x-10<0:
    print("%d는 한자리 숫자입니다." %x)
elif x-10>=0 and x-100<0:
    print("%d는 두자리 숫자입니다/" %x)
elif x-100>=0 and x-1000<0:
    print("%d는 세자리 숫자입니다." %x)
else:
    print("오류!!%d는 범위(0~999)이외의 숫자이다." %x)