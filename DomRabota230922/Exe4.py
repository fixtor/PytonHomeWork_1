# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input("Введите номер четверти от 1 - 4 на оси X,Y: "))

if number  == 1:
    print(f"Диапазон возможных значений в четверти {number}", "X > 0, Y > 0", sep=" -> ")
elif number == 2:
    print(f"Диапазон возможных значений в четверти {number}", "X < 0, Y > 0", sep=" -> ")
elif number == 3:
    print(f"Диапазон возможных значений в четверти {number}", "X < 0, Y < 0", sep=" -> ")
elif number == 4:
    print(f"Диапазон возможных значений в четверти {number}", "X > 0, Y < 0", sep=" -> ")
else:
    print("В этой системе координат, нет таких четвертей")

