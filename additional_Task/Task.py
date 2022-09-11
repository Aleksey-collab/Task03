# 6.
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на |K| 
# элементов вправо,
# если K – положительное влево, если отрицательное вправо.
# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N, во второй строке записаны N целых чисел Ai,
# а в последней – целое число K. (1 ≤ N ≤ 105, |K| ≤ 105, |Ai| ≤ 100).
# Выходные данные
# В выходной файл OUTPUT.TXT выведите полученную последовательность.
# IN
# 5
# 5 3 7 4 6
# 3
# OUT
# 7 4 6 5 3

k = 3

lst = [5, 3, 7, 4, 6]


def ShiftElements(lst, K):
    index = 0
    lst_2 = []
    for i in range(len(lst)):
        if K > 0:
            if i + len(lst) - abs(K) < len(lst):
                lst_2.append(lst[i + len(lst) - abs(K)])
            else:
                lst_2.append(lst[index])
                index += 1
        else:
            if i + abs(K) < len(lst):
                lst_2.append(lst[i + abs(K)])
            else:
                lst_2.append(lst[index])
                index += 1
    return lst_2
                
print(ShiftElements(lst, k))