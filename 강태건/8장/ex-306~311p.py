def reverse_sentence(s):
    words=s.split(" ")
    result=""
    for word in words:
        result=word+""+result
    return result
sentence="Nice to meet you"
print(reverse_sentence(sentence))

def check_word(s,keyword):
    if (s.find(keyword)==-1):
        print("'%s'은 존재하지않는다!" %keyword)
    else:
        print("'%s'은 존재한다!" %keyword)
string="A good book is a great friend"
word="friend"
print("문장:", string)
print("찾는 단어:", word)
check_word(string, word)

def replace_word(string, word_list, word):
    arr=string.split(" ")
    new_arr=[]
    for x in arr:
        if x in word_list:
            new_arr.append(word)
        else:
            new_arr.append(x)
    result=" ".join(new_arr)
    return result
string="python java php apple orange banana"
word_list=["apple","orange","banana"]
word="fruits"
print("문자열:",string)
print("단어 리스트:", word_list)
print("치환할 단어:", word)

new_str=replace_word(string, word_list, word)
print("치환된 문자열:", new_str)

def string_shift(string,d,direction):
    if direction=="left":
        left_part= string[d:]
        right_part= string[0:d]
    else:
        left_part=string[len(string)-d:]
        right_part=string[0:len(string)-d]
    result=left_part+right_part
    return result
string="pythonprogramming"
str_left=string_shift(string,2,"left")
str_right=string_shift(string,3,"right")
print("원래 문자열:", string)
print("좌측으로 2칸 이동:", str_left)
print("우측으로 3칸 이동:", str_right)