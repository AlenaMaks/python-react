# 2 задание

stop = int(input("Введите конечное значение: "))
def easy_num(stop):
    for i in range(2, stop + 1): 
        fl = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                fl = False
                break
        
        # если мы не нашли делителей, то флаг остается True, значит число является простым    
        if fl:
            yield i
        
for num in easy_num(stop):
    print(num)

# print(next(easy_num(stop)))