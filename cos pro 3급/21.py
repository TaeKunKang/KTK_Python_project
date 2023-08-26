line = input()
count = 0
for x in line:
    if "A" <= x <= "Z":
        count += 1
print(count)