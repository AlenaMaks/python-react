# 4 задание
from array import array
from datetime import date, timedelta
from random import randint

days = array('i') # для хранения разницы в днях

now = date.today()
all_dates = []
for i in range(10):
    all_dates.append(now - timedelta(randint(0, 365*5)))
for i in range(len(all_dates)-1):
    days.append(abs(all_dates[i] - all_dates[i+1]).days)

for i in range(1, len(all_dates)):
    print(f"{i}. Разница между {all_dates[i-1]} и {all_dates[i]}: {days[i-1]} дней")