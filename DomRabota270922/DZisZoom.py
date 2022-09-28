# 1.
# num = float(input('Enter any real number: '))

# num_int = int(str(num).replace('.', ''))
# sum = 0

# while num_int > 0:
#     cut_digit = num_int % 10
#     sum += cut_digit
#     num_int //= 10

# print(sum)

# 2.
# n = int(input())
# l = list()
# count = 1
# for i in range(1, n + 1):
#     count *= i
#     l.append(count)
# print(l)

# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# --------------------------------------
n = int(input('Задайте список: '))
pos_1 = int(input('Позиция 1: '))
pos_2 = int(input('Позиция 2: '))
l = []
for i in range(-n, n + 1):
    l.append(i)
print(l, l[pos_1 - 1] * l[pos_2 - 1])
# -------------------------------------------