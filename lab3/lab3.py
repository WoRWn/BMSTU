# Лабораторная работа №3
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: по заданным целочисленным координатам трех точек на плоскости:
# 1) вычислить длины сторон образованного треугольника;
# 2) длину медианы, проведенной из наибольшего угла;
# 3) определить является ли треугольник тупоугольным.
# По заданным координатам четвертой точки, определить находится ли точка внутри треугольника и найти расстояние
# от точки до ближайшей стороны треугольника

from math import sqrt  # загрузка sqrt из модуля math
from sys import float_info  # загрузка float_info из модуля sys

# Блок 1: ввод пользователем координат трех точек, образующих треугольник
x1 = int(input('Введите координату x точки A: '))  # координата x первой точки
y1 = int(input('Введите координату y точки A: '))  # координата y первой точки
x2 = int(input('Введите координату x точки B: '))  # координата x второй точки
y2 = int(input('Введите координату y точки B: '))  # координата y второй точки
x3 = int(input('Введите координату x точки C: '))  # координата x третей точки
y3 = int(input('Введите координату y точки C: '))  # координата y третей точки

# Блок 2: вычисление длин сторон треугольника, его медианы, проверка на тупой угол в треугольнике
vector_ab_x = x2 - x1  # вычисление координаты x вектора ab
vector_ab_y = y2 - y1  # вычисление координаты y вектора ab
vector_bc_x = x3 - x2  # вычисление координаты x вектора bc
vector_bc_y = y3 - y2  # вычисление координаты y вектора bc
vector_ca_x = x1 - x3  # вычисление координаты x вектора ca
vector_ca_y = y1 - y3  # вычисление координаты y вектора ca

length_ab = sqrt(vector_ab_x**2 + vector_ab_y**2)  # вычисление длины вектора ab
length_bc = sqrt(vector_bc_x**2 + vector_bc_y**2)  # вычисление длины вектора bc
length_ca = sqrt(vector_ca_x**2 + vector_ca_y**2)  # вычисление длины вектора ca

largest_side = length_ab  # переменная для большей стороны треугольника
if length_ab-length_bc > float_info.epsilon and length_ab-length_ca > float_info.epsilon:
    largest_side = length_ab  # ab - большая сторона
elif length_bc-length_ab > float_info.epsilon and length_bc-length_ca > float_info.epsilon:
    largest_side = length_bc  # bc - большая сторона
else:
    largest_side = length_ca  # ca - большая сторона

median_length = 0  # переменная для длины медианы, проведенной к большей стороне
if largest_side == length_ab:
    median_length = 0.5 * sqrt(2 * length_bc**2 + 2 * length_ca**2 - length_ab**2)  # длина медианы к стороне ab
elif largest_side == length_bc:
    median_length = 0.5 * sqrt(2 * length_ab**2 + 2 * length_ca**2 - length_bc**2)  # длина медианы к стороне bc
else:
    median_length = 0.5 * sqrt(2 * length_ab**2 + 2 * length_bc**2 - length_ca**2)  # длина медианы к стороне ca

obtuse = False  # переменная-флаг для проверки на наличие тупого угла у треугольника
if (length_ab**2 > length_bc**2 + length_ca**2) or (length_bc**2 > length_ab**2 + length_ca**2) or \
        (length_ca**2 > length_bc**2 + length_ab**2):
    obtuse = True  # треугольник тупоугольный

# Блок 3: вывод полученных значений
print('Длины сторон полученного треугольника:', round(length_ab, 7), round(length_bc, 7), round(length_ca, 7), sep=' ')
print('Длина медианы, проведенной их большего угла: ', median_length)
if obtuse:
    print('Треугольник является тупоугольным')
else:
    print('Треугольник не является тупоугольным')

# Блок 4: ввод пользователем координат четвертой точки
x4 = int(input('Введите координату x точки D: '))  # координата x четвертой точки
y4 = int(input('Введите координату y точки D: '))  # координата y четвертой точки

# Блок 5: вычисления, необходимые для определения нахождения четвертой точки внутри треугольника и вычисление расстояния
# от точки до ближайшей стороны
dot_inside = False
if ((x1 - x4) * (y2 - y1) - (x2 - x1) * (y1 - y4) > 0) and ((x2 - x4) * (y3 - y2) - (x3 - x2) * (y2 - y4) > 0) and \
        ((x3 - x4) * (y1 - y3) - (x1 - x3) * (y3 - y4) > 0):
    dot_inside = True  # точка внутри треугольника
elif ((x1 - x4) * (y2 - y1) - (x2 - x1) * (y1 - y4) < 0) and ((x2 - x4) * (y3 - y2) - (x3 - x2) * (y2 - y4) < 0) and \
        ((x3 - x4) * (y1 - y3) - (x1 - x3) * (y3 - y4) < 0):
    dot_inside = True  # точка внутри треугольника

min_distance = 0  # расстояние от четвертой точки до ближайшей стороны
if dot_inside:
    distance_to_ab = abs((y1 - y2) * x4 + (x2 - x1) * y4 + (x1 * y2 - x2 * y1)) / sqrt((y1 - y2)**2 + (x2 - x1)**2)
    distance_to_bc = abs((y2 - y3) * x4 + (x3 - x2) * y4 + (x2 * y3 - x3 * y2)) / sqrt((y2 - y3)**2 + (x3 - x2)**2)
    distance_to_ca = abs((y3 - y1) * x4 + (x1 - x3) * y4 + (x3 * y1 - x1 * y3)) / sqrt((y3 - y1)**2 + (x1 - x3)**2)
    if distance_to_ab-distance_to_bc < float_info.epsilon and distance_to_ab-distance_to_ca < float_info.epsilon:
        min_distance = distance_to_ab  # расстояние от четвертой точки до ab
    elif distance_to_bc-distance_to_ab < float_info.epsilon and distance_to_bc-distance_to_ca < float_info.epsilon:
        min_distance = distance_to_bc  # расстояние от четвертой точки до bc
    else:
        min_distance = distance_to_ca  # расстояние от четвертой точки до ca

# Блок 6: вывод значения ближайшего расстояния, при условии нахождения точки внутри треугольника
if dot_inside:
    print('Расстояние от точки до ближайшей стороны треугольника: ', round(min_distance, 15))
else:
    print('Точка не находится внутри треугольника')
