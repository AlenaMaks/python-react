# 2 задание
number = input("Введите число: ")
if number.isdigit():
    print(f"Число {number} является четным\n" if int(number) % 2 == 0 else f"Число {number} не является четным\n")
else:
    print("Ошибка: введено не число\n")