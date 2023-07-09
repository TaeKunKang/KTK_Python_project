s=[64,89,100,85,77,58,79,67,96,87,87,36,82,98,84,76,63,69,53,22]
soo=0
woo=0
mi=0
yang=0
ga=0
i=0
while i <len(s):
    if 100>=s[i] and s[i]>=90:
        soo=soo+1
    if 89>=s[i] and s[i]>=80:
        woo=woo+1
    if 79>=s[i] and s[i]>=70:
        mi=mi+1
    if 69>=s[i] and s[i]>=60:
        yang=yang+1
    if 59>=s[i] and s[i]>=0:
        ga=ga+1
    i=i+1
print("수: %d명" %soo)
print("우: %d명" %woo)
print("미: %d명" %mi)
print("양: %d명" %yang)
print("가: %d명" %ga)
