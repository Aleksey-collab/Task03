# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = 45

def binary(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return int(b)

print(binary(45))
print(binary(3))
print(binary(2))
