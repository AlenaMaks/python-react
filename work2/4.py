# 4 задание
a = input("Введите строку: ") + ' '

lst = []
value = ''

for i in range(len(a)):
    if a[i] != ' ':
        value += a[i]
    if a[i] == ' ':
        lst.append(value.lower())
        value = ''

set_lst = set(lst)
for key in set_lst:
    print(f"{key}: {lst.count(key)}")