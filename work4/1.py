# 1 задание

# Создайте список квадратов первых 10 натуральных чисел, используя list comprehension.
list_c = [x**2 for x in range(1, 11)]
print(f"1 задание: {list_c}")

# Создайте словарь, содержащий названия дней недели и их порядковые номера, используя dict comprehension.
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
dict_week = {a: days[a-1] for a in range(1, 8)}
print(f"2 задание: {dict_week}")

# Создайте множество, содержащее теги библиотек в нижнем регистре, используя list comprehension
lst = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
lst = {lst[i].lower() for i in range(len(lst))}
print(f"3 задание: {lst}, {type(lst)}")

# Создайте список, содержащий только четные числа из исходного списка, используя list comprehension.
lst = [1, 3, 4, 87, 98, 15, 7, 4]
lst_result = [i for i in lst if i % 2 == 0]
print(f'4 задание: {lst_result}')

# Создайте словарь, где ключи — это числа от 1 до 5, а значения — их факториалы, используя dict comprehension.
def fact(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result
        
dict_fact = {a: fact(a) for a in range(1, 6)}
print(f"5 задание: {dict_fact}")
