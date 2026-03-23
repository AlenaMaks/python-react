# 1 задание

def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

assert average_num(['1', 2, '3']) == 2
assert average_num('Привет') == 'Bad request'
assert average_num('1234') == 'Bad request' # из-за попытки изменить строку через индекс
assert average_num(['1234']) == 1234 # enumerate работает со списком и не индексирует строку
assert average_num(['12', 4]) == 8
assert average_num(['01', 1]) == 1
assert average_num(['s', 9, '3']) == 'Bad request'
assert average_num(['3.0', 2.5]) == 'Bad request' # '3.0' выдает ошибку при переводе в int
assert average_num([3.0, 2.5]) == 2.75
assert average_num([True, False]) == 0.5 # преобразуются в числовые значения 0 и 1
assert average_num(['5', '-5']) == 0

# при вводе int вместо list исключение TypeError
# при вводе пустого списка искоючение ZeroDivisionError