# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from datetime import datetime
import time



def fibb(n):
    lst = []
    f1, f2 = 1, 1
    for i in range(abs(n)):
        lst.append(f1)
        f1, f2 = f2, f1 + f2
    return lst
start_time = datetime.now()        
def neg_fibb(n):
    lst = []
    f1, f2 = 1, -1
    for i in range(abs(n)):
        lst.append(f1)
        f1, f2 = f2, (f1 + 1) - (f2 + 1)
    return lst
print(f'Вариант 1: отработал за {datetime.now() - start_time}')

start_time2 = datetime.now()  
def neg_fibb_2(n):
    lst = fibb(n)
    for i in range(len(lst)):
        if i %2 != 0:
            lst[i] = lst[i]*(-1)
    lst1 = lst[::-1]
    return lst1
print(f'Вариант 2: отработал за {datetime.now() - start_time2}')    
n = 10


print(neg_fibb(n)[::-1] + [0] + fibb(n))
print(neg_fibb_2(n) + [0] + fibb(n))