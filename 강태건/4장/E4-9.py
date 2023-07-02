print("-"*30)
print("cm     mm    m    inch")
print("-"*30)
cm=0
while cm<=51:
    cm=cm+1
    mm=cm*10
    m=cm*0.01
    inch=cm*0.39
    print("%2d    %2d   %2.2f   %2.2f" %(cm, mm, m, inch))
print("-"*30)