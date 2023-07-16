year_sale={"2016":37,"2017":98,"2018":158,"2019":233,"2020":120}
m = max(list(year_sale.values()))

t = list(year_sale.keys())
for item in t:
    if year_sale[item] == m:
        print(item)