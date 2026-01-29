num = [12, 45, 2, 99, 4]
max_num = num[0]
for n in num:
    if n >max_num:
        max_num = n
    else:
        continue
print(max_num)