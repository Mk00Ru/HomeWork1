# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def check_part(x, y):
    if x > 0 < y:
        return 1
    elif x < 0 < y:
        return 2
    elif x < 0 > y:
        return 3
    elif x > 0 > y:
        return 4

x_cord = int(input("Введите X: "))
y_cord = int(input("Введите Y: "))
print(check_part(x_cord, y_cord))
