import datetime
time1=datetime.timedelta(days=3, hours=3, minutes=30)
time2=datetime.timedelta(days=5, hours=5, minutes=40)
print(time2-time1)

import datetime
today=datetime.date.today()
print(today)

import datetime
today=datetime.date.today()
week=datetime.timedelta(weeks=1)
next_week=today+week
print("오늘:", today)
print("일주일 후:", next_week)

from datetime import datetime
today=datetime.now()
print("%s년" %today.year)
print("%s월" %today.month)
print("%s일" %today.day)
print("%s시" %today.hour)
print("%s분" %today.minute)
print("%s초" %today.second)
string=today.strftime("%Y/%m/%d %H:%M:%S")
print(string)

