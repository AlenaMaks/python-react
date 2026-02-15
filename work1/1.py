# 1 задание
name = input("Ваше имя: ")
lastname = input("Фамилия: ")
age = int(input("Возраст: "))

print("\nРеализация через format:\nВаше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, lastname, age))
print(f"\nРеализация через f-string:\nВаше имя: {name}, Фамилия: {lastname}, Возраст: {age} лет.")

