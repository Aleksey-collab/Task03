# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def convert(arr):
    return [arr[i] % 1 for i in range(len(arr))]
    
n = [1.1, 1.2, 3.1, 5, 10.01]

print(int((max(convert(n)) - min(convert(n))) * 100) / 100)