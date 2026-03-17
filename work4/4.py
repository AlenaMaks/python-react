# 4 задание

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"\nФункция {func.__name__} вызвана с аргументами: ")
        print(f"Позиционные элементы: {args}")
        print(f"Именованные элементы: {kwargs}")
        return func(*args, **kwargs) # без использования переменной result
    return wrapper

# основная функция обёрнутая в декоратор
@decorator
def rectangle_S(a, b):
    return a * b

a = int(input("Первая сторона: "))
b = int(input("Вторая сторона: "))

print(f"Площадь прямоугольника: {rectangle_S(a, b)}")