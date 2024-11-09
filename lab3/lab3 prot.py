# Защита лабораторной работы №3
# Гаев Дмитрий ИУ7-14Б

from math import sqrt  # загрузка sqrt из модуля math
from sys import float_info  # загрузка float_info из модуля sys

x1 = int(input('Введите координату x точки A: '))  # координата x первой точки
y1 = int(input('Введите координату y точки A: '))  # координата y первой точки
x2 = int(input('Введите координату x точки B: '))  # координата x второй точки
y2 = int(input('Введите координату y точки B: '))  # координата y второй точки
x3 = int(input('Введите координату x точки C: '))  # координата x третей точки
y3 = int(input('Введите координату y точки C: '))  # координата y третей точки

distance_to_ab = abs((y1 - y2) * x3 + (x2 - x1) * y3 + (x1 * y2 - x2 * y1)) / sqrt((y1 - y2)**2 + (x2 - x1)**2)
distance_to_bc = abs((y2 - y3) * x1 + (x3 - x2) * y1 + (x2 * y3 - x3 * y2)) / sqrt((y2 - y3)**2 + (x3 - x2)**2)
distance_to_ca = abs((y3 - y1) * x2 + (x1 - x3) * y2 + (x3 * y1 - x1 * y3)) / sqrt((y3 - y1)**2 + (x1 - x3)**2)

max_height = 0  # максимальная высота треугольника
if distance_to_ab-distance_to_ca > float_info.epsilon and distance_to_ab-distance_to_bc > float_info.epsilon:
    max_height = distance_to_ab
elif distance_to_bc-distance_to_ab > float_info.epsilon and distance_to_bc-distance_to_ca > float_info.epsilon:
    max_height = distance_to_bc
else:
    max_height = distance_to_ca

print('Максимальная высота в треугольнике: ', round(max_height, 10))
