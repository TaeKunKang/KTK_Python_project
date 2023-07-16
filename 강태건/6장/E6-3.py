year_sale={"2016":237,"2017":98,"2018":158,"2019":233,"2020":120}
sum=0
for key in year_sale:
    sum=sum+year_sale[key]
avg=sum/len(year_sale)
print("5년간 총 판매량: %d" %sum)
print("5년간 연 평균 판매량: %d" %avg)