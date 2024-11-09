# Лабораторная работа №8 задание 6
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: выполнить транспонирование матрицы

# Блок 1: ввод исходной матрицы
matrix = []
length = int(input('Введите порядок матрицы (минимум 1): '))  # количество строк матрицы
while length < 1:  # проверка на длину матрицы
    length = int(input('Неверный ввод. Введите порядок матрицы (минимум 1): '))
flag = False  # флаг для проверки правильности ввода матрицы
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

# Блок 3: изменение матрицы
for i in range(length):
    for j in range(i+1, length):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Блок 4: вывод измененной матрицы
print('Измененная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)


