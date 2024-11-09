# Лабораторная работа №8 задание 1 вариант 3
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: найти строку, имеющую наибольшее количество четных элементов

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

# Блок 3: поиск требуемой строки
max_count = 0  # максимальное количество
line = []  # подходящая строка
for i in range(length):
    curr_count = 0  # текущее количество
    for j in range(width):
        if matrix[i][j] % 2 == 0:
            curr_count += 1  # увеличиваем текущее количество
    if curr_count > max_count:
        max_count = curr_count  # обновляем максимум
        line = matrix[i]  # сохраняем строку

# Блок 4: вывод строки
print('Строка с наибольшим кол-вом четных элементов: ', *line)
