# Лабораторная работа №9 задание 5
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: получить матрицу C, которая является произведением матриц A и B

# Блок 1: ввод матрицы A
matrix_a = []
length_a = int(input('Введите количество строк матрицы A (минимум 1): '))  # количество строк матрицы
while length_a < 1:  # проверка на длину матрицы
    length_a = int(input('Неверный ввод. Введите количество строк матрицы A (минимум 1): '))
width_a = 0  # ширина матрицы
for i in range(length_a):
    line = []
    while (i != 0 and len(line) != len(matrix_a[i-1])) or len(line) < 1:
        line = list(map(int, input('Введите {:} строку матрицы A: '.format(i+1)).split()))
        width_a = len(line)  # ширина матрицы
    matrix_a += [line]  # добавление в матрицу новой строки

# Блок 2: ввод матрицы B
matrix_b = []
length_b = int(input('Введите количество строк матрицы B (минимум 1): '))  # количество строк матрицы
while length_b < 1:  # проверка на длину матрицы
    length_b = int(input('Неверный ввод. Введите количество строк матрицы B (минимум 1): '))
while width_a != length_b:  # проверка на согласованность матриц
    length_b = int(input('Неверный ввод. Количество строк матрицы B должно равняться количеству столбцов матрицы A. \n'
                         'Введите количество строк матрицы B (минимум 1): '))
width_b = 0  # ширина матрицы
for i in range(length_b):
    line = []
    while (i != 0 and len(line) != len(matrix_b[i-1])) or len(line) < 1:
        line = list(map(int, input('Введите {:} строку матрицы B: '.format(i+1)).split()))
        width_b = len(line)  # ширина матрицы
    matrix_b += [line]  # добавление в матрицу новой строки

# Блок 3: вывод матрицы A
print('Матрица A: ')
for i in range(length_a):
    formatted_line = ['{:6}'.format(member) for member in matrix_a[i]]
    print(*formatted_line)

# Блок 4: вывод матрицы B
print('Матрица B: ')
for i in range(length_b):
    formatted_line = ['{:6}'.format(member) for member in matrix_b[i]]
    print(*formatted_line)

# Блок 5: вычисление матрицы C
matrix_c = [[0 for _ in range(width_b)] for _ in range(length_a)]  # задаем матрицу C
for i in range(length_a):
    for j in range(width_b):
        for k in range(length_b):
            matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]  # вычисления значения в матрице C

# Блок 6: вывод матрицы C
print('Матрица C: ')
for i in range(length_a):
    formatted_line = ['{:6}'.format(member) for member in matrix_c[i]]
    print(*formatted_line)
