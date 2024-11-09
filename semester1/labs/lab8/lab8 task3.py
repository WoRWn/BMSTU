# Лабораторная работа №8 задание 3 вариант 4
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: найти столбец, имеющий наибольшее кол-во нулевых элементов

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

# Блок 3: поиск требуемого столбца
column = []  # подходящий столбец
max_count = 0  # максимальная длина
index = False  # индекс подходящего столбца
for j in range(width):
    curr_count = 0  # текущая длина
    for i in range(length):
        if matrix[i][j] == 0:
            curr_count += 1  # считаем нулевые элементы
    if curr_count > max_count:
        max_count = curr_count  # обновляем максимум
        index = j  # сохраняем индекс столбца

# Блок 4: вывод столбца
print('Столбец с наибольшим кол-вом нулевых элементов: ')
for i in range(length):
    print(matrix[i][index])
