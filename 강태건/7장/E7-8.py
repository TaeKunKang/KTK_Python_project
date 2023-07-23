def func(string):
    result=""
    index=len(string)
    while index>0:
        result=result+string[index-1]
        index=index-1
    return result
string= input("문자열의 입력하세요")
print(func(string))
