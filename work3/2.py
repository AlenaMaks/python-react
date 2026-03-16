# 2 задание

# проверка на число (не пригодилась)
# def is_int(a):
#     if not(isinstance(a, int)):
#         raise TypeError(f"Переменная {a} не является целым числом и с ней нельзя выполнить действие")

# сложение
def adding(a, b):
    return a + b

# вычитание
def subtraction(a, b):
    return a - b

# умножение
def multiplication(a, b):
    return a * b

# обычное деление
def dividing(a, b):
    if b == 0:
        raise ZeroDivisionError("На 0 делить нельзя!!!")
    return a / b

# целочисленное деление
def dividing_cel(a, b):
    if b == 0:
        raise ZeroDivisionError("На 0 делить нельзя!!!")
    return a // b

# нахождение остатка от деления
def dividing_ost(a, b):
    if b == 0:
        raise ZeroDivisionError("На 0 делить нельзя!!!")
    elif int(a) - a != 0:
        raise TypeError("Переменная 1 должна быть целочисленной для выполнения действия.")
    elif int(b) - b != 0:
        raise TypeError("Переменная 2 должна быть целочисленной для выполнения действия.")
    else:
        return a % b

# возведение в степень
def degree(a, b):
    return a**b

# максимальное число
def max_number(a, b):
    return ((a + b + abs(a - b)) / 2)

# среднее арифметическое
def avg(a, b):
    return (a + b) / 2

# отклонение в процентах
def percent(a, b):
    if a == 0:
        raise ZeroDivisionError("Переменная 1 не может быть нулём.")
    return abs(100 - (b / (a / 100)))

print('''Доступные операции:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Возведение в степень
6. Максимальное число
7. Среднее арифметическое
8. Отклонение в процентах
exit - Конец программы''')

while True:
    try:
        print("--------------")
        command = (input("Номер операции: "))
        if command == 'exit':
            break
        a = float(input("Переменная 1: "))
        b = float(input("Переменная 2: "))
        
        if command == '1':
            result = adding(a, b)
        elif command == '2':
            result = subtraction(a, b)
        elif command == '3':
            result = multiplication(a, b)
        elif command == '4':
            print("1. Обычное деление\n2. Целочисленное деление\n3. Остаток от деления")
            command_dop = input("Номер операции: ")
            if command_dop == '1':
                result = dividing(a, b)
            elif command_dop == '2':
                result = dividing_cel(a, b)
            elif command_dop == '3':
                result = dividing_ost(a, b)
            else:
                print("Такой команды не существует.")
                continue
        elif command == '5':
            result = degree(a, b)
        elif command == '6':
            result = max_number(a, b)
        elif command == '7':
            result = avg(a, b)
        elif command == '8':
            result = percent(a, b)
        else:
            print("Такой команды не существует.")
            continue
            
        print(f"Результат операции: {result}")
        
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(e)
    
    
    
    