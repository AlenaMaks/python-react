# 3 задание
age = input("Введите ваш возраст: ")
if age[0] == "-" and age[1:].isdigit():
    print("Ошибка: возраст не может быть отрицательным!\n")
elif not(age.isdigit()):
    print("Ошибка: введено не число!\n")
else:
    print("Вы совершеннолетний.\n" if int(age) >= 18 else "Вы несовершеннолетний.\n")
