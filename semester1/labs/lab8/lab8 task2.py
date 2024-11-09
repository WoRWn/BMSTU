# Лабораторная работа №8 задание 2
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов

from math import inf  # импортирование функции inf из модуля math

# Блок 1: ввод исходной матрицы
matrix = []
length = int(input('Введите количество строк матрицы (минимум 1): '))  # количество строк матрицы
while length < 1:  # проверка на длину матрицы
    length = int(input('Неверный ввод. Введите количество столбцов матрицы (минимум 1): '))
width = 0  # ширина матрицы
for i in range(length):
    line = []
    while (i != 0 and len(line) != len(matrix[i-1])) or len(line) < 1:
        line = list(map(int, input('Введите {:} строку матрицы: '.format(i+1)).split()))
        width = len(line)
    matrix += [line]  # добавление в матрицу новой строки

# Блок 2: вывод исходной матрицы
print('Исходная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)

# Блок 3: изменение матрицы
max_count = -inf  # максимальное количество
min_count = inf  # минимальное количество
max_index = min_index = False  # минимальный и максимальный индексы
count = 0  # количество
for i in range(length):
    count = 0
    for j in range(width):
        if matrix[i][j] < 0:
            count += 1  # считаем отрицательные числа
    if count > max_count:  # находим новый максимум
        max_count = count
        max_index = i
    elif count < min_count:  # находим новый минимум
        min_count = count
        min_index = i
matrix[max_index], matrix[min_index] = matrix[min_index], matrix[max_index]

# Блок 4: вывод измененной матрицы
print('Измененная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)
