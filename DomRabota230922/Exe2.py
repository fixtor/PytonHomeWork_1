# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите число X в левой части: "))
y = int(input("Введите число Y: "))
z = int(input("Введите число Z: "))

left_side = not(x and y and z)
right_side = not x or not y or not z

if left_side == right_side:
    print(f"Верно!")
else:
    print(f"Ложно!")
