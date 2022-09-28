# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

in_number = float(input('Введите вещественное число: '))
num_int = int(str(in_number).replace('.', ''))
sum = 0
while num_int > 0:
    cut_digit = num_int % 10
    sum = sum + cut_digit
    num_int //= 10
print(f"{in_number}", f"{sum}", sep=" -> ")