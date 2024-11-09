# Лабораторная работа №8 задание 5
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: найти максимальное значение матрицы над главной диагональю и минимальное
# под побочной диагональю

from math import inf  # импортирование функции inf из модуля math

# Блок 1: ввод исходной матрицы
matrix = []
length = int(input('Введите порядок матрицы (минимум 1): '))  # количество строк матрицы
while length < 1:  # проверка на длину матрицы
    length = int(input('Неверный ввод. Введите порядок матрицы (минимум 1): '))
width = 0  # ширина матрицы
for i in range(length):
    line = []
    while width != length or len(line) < 1:
        line = list(map(int, input('Введите {:} строку матрицы: '.format(i+1)).split()))
        width = len(line)
    matrix += [line]  # добавление в матрицу новой строки

# Блок 2: вывод исходной матрицы
print('Исходная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)

# Блок 3: поиск значений
max_num = -inf  # максимальное значение
for i in range(length - 1):
    for j in range(i + 1, length):
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]  # обновляем максимум
min_num = inf  # минимальное значение
for i in range(1, length):
    for j in range(length - i, length):
        if matrix[i][j] < min_num:
            min_num = matrix[i][j]  # обновляем минимум

# Блок 4: вывод значений
print('Максимальное значение над главной диагональю: {:}'.format(max_num))
print('Минимальное значение под побочной диагональю: {:}'.format(min_num))
