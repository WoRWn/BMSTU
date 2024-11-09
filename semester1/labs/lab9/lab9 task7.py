# Лабораторная работа №9 задание 7
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: вывести срез трехмерного массива по большему измерению

# Блок 1: ввод трехмерного массива
arr = []  # трехмерный массив
count = 0  # количество матриц
while count < 1:
    count = int(input('Введите количество матриц, из которых будет состоять трехмерный массив (минимум 1): '))
length = 0  # длина матриц
while length < 1:  # проверка на длину матриц
    length = int(input('Введите количество строк матриц (минимум 1): '))  # количество строк матрицы
width = 0  # ширина матриц
for j in range(count):
    matrix = []  # матрица
    for i in range(length):
        line = []  # строка матрицы
        while (i != 0 and len(line) != len(matrix[i-1])) or len(line) < 1:
            line = list(map(int, input('Введите {:} строку {:} матрицы: '.format(i+1, j+1)).split()))
            width = len(line)  # ширина матрицы
        matrix += [line]  # добавление в матрицу новой строки
    arr.append(matrix)  # сохранение матрицы в массив

# Блок 2: определение среза массива
arr_sliced = []  # матрица среза
max_dim = max(count, length, width)  # поиск максимального измерения
if max_dim == count:  # максимальное измерение - количество матриц
    for ln in range(length):
        arr_sliced_line = []  # строка матрицы
        for w in range(width):
            arr_sliced_line.append(arr[(count - 1) // 2][ln][w])  # добавляем элементы в строку матрицы
        arr_sliced.append(arr_sliced_line)  # сохраняем строку матрицы в матрицу
elif max_dim == length:  # максимальное измерение - количество строк матриц
    for c in range(count):
        arr_sliced_line = []  # строка матрицы
        for w in range(width):
            arr_sliced_line.append(arr[c][(length - 1) // 2][w])  # добавляем элементы в строку матрицы
        arr_sliced.append(arr_sliced_line)  # сохраняем строку матрицы в матрицу
else:  # максимальное измерение - ширина матриц
    for c in range(count):
        arr_sliced_line = []  # строка матрицы
        for ln in range(length):
            arr_sliced_line.append(arr[c][ln][(width - 1) // 2])  # добавляем элементы в строку матрицы
        arr_sliced.append(arr_sliced_line)  # сохраняем строку матрицы в матрицу

# Блок 3: вывод среза
print('Срез по большему измерению: ')
for i in range(len(arr_sliced)):
    formatted_line = ['{:6}'.format(member) for member in arr_sliced[i]]
    print(*formatted_line)
