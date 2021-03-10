my_list = []

for i in range(1, 1001, 2):
    my_list.append(i**3)

res = []
for i in my_list:
    i = str(i)
    el = 0
    for n in i:
        el += int(n)
    if el % 7 == 0:
        res.append(el)
new_res = []
for i in res:
    i += 17
    i = str(i)
    el = 0
    for n in i:
        el += int(n)
    if el % 7 == 0:
        new_res.append(el)

print(my_list)
print(res)
print(new_res)
