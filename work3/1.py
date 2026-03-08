# 1 задание

# функция умножения
def func_mn(lst: list[str], x: int = 2) -> list[int]:
    lst_new = []
    for i in range(len(lst)):
        lst_new.append(int(lst[i])*x)
    return lst_new
        
lst = input("Введите список чисел через пробел: ").split()
x = input("Введите множитель (по умолчанию 2): ")

# случай когда ничего не ввели в множитель или ввели не число
if not(x.lstrip('-').isdigit()):
    print(f"Результат (функция): {func_mn(lst)}")
    func_mn_l = list(map(lambda num, x = 2: int(num) * int(x), lst))
    print(f"Результат (лямбда-функция): {func_mn_l}")
else:
    # когда корректный ввод множителя
    print(f"Результат (функция): {func_mn(lst, x)}")
    func_mn_l = list(map(lambda num, x: int(num) * int(x), lst))
    print(f"Результат (лямбда-функция): {func_mn_l}")