# Лабораторная работа №8 задание 4
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: переставить столбцы с максимальной и минимальной суммой элементов

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
max_column_index = min_column_index = 0  # индексы подходящих столбцов (с мин и макс суммами)
max_sum = -inf  # максимальная сумма столбца
min_sum = inf  # минимальная сумма столбца
for j in range(width):
    curr_sum = 0  # текущая сумма
    for i in range(length):
        curr_sum += matrix[i][j]
    if curr_sum > max_sum:
        max_sum = curr_sum
        max_column_index = j
    elif curr_sum < min_sum:
        min_sum = curr_sum
        min_column_index = j
for i in range(length):
    matrix[i][max_column_index], matrix[i][min_column_index] = matrix[i][min_column_index], matrix[i][max_column_index]

# Блок 4: вывод измененной матрицы
print('Измененная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)
