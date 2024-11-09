# Лабораторная работа №9 задание 3
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: посчитать для каждого столбца матрицы A кол-во значений, больших среднего арифметического в
# соответствующих столбцах матрицы B, умножить каждый элемент столбца на соответствующее этому столбцу значение

# Блок 1: ввод матрицы A
matrix_a = []  # матрица A
length_a = int(input('Введите количество строк матрицы A (минимум 1): '))  # количество строк матрицы
while length_a < 1:  # проверка на длину матрицы
    length_a = int(input('Неверный ввод. Введите количество строк матрицы A (минимум 1): '))
width_a = 0  # ширина матрицы
for i in range(length_a):
    line = []  # строка матрицы A
    while (i != 0 and len(line) != len(matrix_a[i-1])) or len(line) < 1:
        line = list(map(int, input('Введите {:} строку матрицы A: '.format(i+1)).split()))
        width_a = len(line)
    matrix_a += [line]  # добавление в матрицу новой строки

# Блок 2: ввод матрицы B
matrix_b = []  # матрица B
length_b = int(input('Введите количество строк матрицы B (минимум 1): '))  # количество строк матрицы
while length_b < 1:  # проверка на длину матрицы
    length_b = int(input('Неверный ввод. Введите количество строк матрицы B (минимум 1): '))
width_b = 0  # ширина матрицы
for i in range(length_b):
    line = []  # строка матрицы B
    while (i != 0 and len(line) != len(matrix_b[i-1])) or len(line) < 1 or width_a != width_b:
        if i != 0 and width_a != width_b:  # ошибка ввода, матрицы не одинаковой ширины
            line = list(map(int, input('Ширина матрицы B должна равняться ширине матрицы A\n'
                                       'Введите {:} строку матрицы B: '.format(i + 1)).split()))
        else:
            line = list(map(int, input('Введите {:} строку матрицы B: '.format(i+1)).split()))
        width_b = len(line)  # ширина матрицы
    matrix_b += [line]  # добавление в матрицу новой строки

# Блок 3: преобразование матрицы
counter_list = []
for j in range(width_b):
    column_sum = 0  # сумма значений столбца
    for i in range(length_b):
        column_sum += matrix_b[i][j]  # увеличиваем сумму
    aver = column_sum / length_b  # сохраняем среднее арифметическое
    counter = 0
    for i in range(length_a):
        if matrix_a[i][j] > aver:
            counter += 1  # обновляем счетчик
    counter_list.append(counter)
    for i in range(length_b):
        if counter != 0:
            matrix_b[i][j] *= counter  # преобразуем элементы матрицы B

# Блок 4: вывод списка количества чисел и преобразованной матрицы B
print('Кол-во значений матрицы A по столбцам, больших среднего арифм. соответствующего столбца матрицы B: ', *counter_list)
print('Преобразованная матрица B: ')
for i in range(length_b):
    formatted_line = ['{:6}'.format(member) for member in matrix_b[i]]
    print(*formatted_line)
