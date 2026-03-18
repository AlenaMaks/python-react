# 2 задание
from random import randint
from statistics import mean, median, pstdev
from math import sqrt

lst_numbers = [randint(1, 100) for i in range(100)]
avg = round(mean(lst_numbers), 2)
mediana = round(median(lst_numbers), 2)
deviation = round(pstdev(lst_numbers), 2) # можно stdev для выборки (разные формулы)
root = round(sqrt(sum(lst_numbers)), 2)

print(f"Среднее: {avg}, Медиана: {mediana}, Стандартное отклонение: {deviation}, Корень из суммы: {root}")
