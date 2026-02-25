# 3 задание
a = input('Введите первый список: ') + ' '
b = input('Введите второй список: ') + ' '

lst1 = []
lst2 = []
value = ''

for i in range(len(a)):
    if a[i] != ' ':
        value += a[i]
    if a[i] == ' ':
        lst1.append(value)
        value = ''
print(lst1)
        
for i in range(len(b)):
    if b[i] != ' ':
        value += b[i]
    if b[i] == ' ':
        lst2.append(value)
        value = ''
print(lst2)

print("Общие элементы: {}".format(' '.join(set(lst1) & set(lst2))))
