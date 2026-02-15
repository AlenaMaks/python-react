while True:
    number = input("Введите число: ")
    if number == 'exit':
        print("Выход из программы...\n")
        break
    elif not(number.lstrip('-').isdigit()):
        print('Ошибка: данные не являются числом.\n')
    else:
        lenNumber = len(number.lstrip('-'))
        print(f"В этом числе {lenNumber} цифры.\n")