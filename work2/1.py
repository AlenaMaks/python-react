# 1 задание
a = input("Введите числа через пробел: ") + " "
lst = []

# вариант с split, но его не было в лекции
# for b in a.split():
#     lst.append(b)

value = ''
for i in range(len(a)):
    if a[i] != ' ':
        value += a[i]
    if a[i] == ' ':
        lst.append(value)
        value = ''
        
print(lst)

st = int(input("Введите степень: "))
for i in range(len(lst)):
    if lst[i].lstrip('-').isdigit():
        lst[i] = int(lst[i])**st
    else:
        lst[i] = lst[i] * st

print("Вывод: ", end = '')
for b in lst:
    print(b, end = ' ')