import time
seconds=time.time()
print(seconds)

import time 
tm= time.gmtime(1691902316.508328)
print(tm)

import time
tm=time.localtime(1691902412.924295)
print("년:", tm.tm_year)
print("월:", tm.tm_mon)
print("일:", tm.tm_mday)
print("시:", tm.tm_hour)
print("분:", tm.tm_min)
print("초:", tm.tm_sec)

import time
string= time.ctime(1691902606.388418)
print(string)

import time
tm= time.localtime(time.time())
string=time.strftime("%Y-%m-%d %I:%M:%S %p",tm)
print(string)

import time
print("시작!")
time.sleep(5)
print("5초 후 나타남!")

import time
def func():
    sum=0
    for i in range(1,10000001):
        sum=sum+i
start= time.time()
func()
end= time.time()
print("소유시간:", end-start)
