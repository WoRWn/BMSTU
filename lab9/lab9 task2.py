# Лабораторная работа №9 задание 2
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: повернуть квадратную целочисленную матрицу на 90 градусов по часовой стрелке,
# затем на 90 градусов против часовой стрелки

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
        width = len(line)  # ширина матрицы
    matrix += [line]  # добавление в матрицу новой строки

# Блок 2: вывод исходной матрицы
print('Исходная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)

# Блок 3: поворот матрицы на 90 градусов по часовой
for i in range((length + 1) // 2):
    for j in range(length // 2):
        matrix[i][j], matrix[j][length - i - 1], matrix[length - i - 1][length - j - 1], matrix[length - j - 1][i] = \
            matrix[length - j - 1][i], matrix[i][j], matrix[j][length - i - 1], matrix[length - i - 1][length - j - 1]

# Блок 4: вывод промежуточной матрицы
print('Промежуточная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)

# Блок 5: поворот матрицы на 90 градусов против часовой
for i in range((length + 1) // 2):
    for j in range(length // 2):
        matrix[i][j], matrix[j][length - i - 1], matrix[length - i - 1][length - j - 1], matrix[length - j - 1][i] = \
            (matrix[j][length - i - 1], matrix[length - i - 1][length - j - 1], matrix[length - j - 1][i], matrix[i][j])

# Блок 6: вывод итоговой матрицы
print('Итоговая матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)
