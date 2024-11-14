# Лабораторная работа №9 защита

# Назначение программы: заполнить змейкой, которая скручивается спиралью, прямоугольную матрицу
# по заданным размерам матрицы и списку значений

# Блок 1: ввод значений размеров матрицы и список значений для заполнения матрицы
m = int(input('Введите количество строк матрицы (не меньше 1): '))
while m < 1:
    m = int(input('Недопустимое количество строк. Введите количество строк матрицы (не меньше 1): '))
n = int(input('Введите количество столбцов матрицы (не меньше 1): '))
while n < 1:
    n = int(input('Недопустимое количество столбцов. Введите количество строк матрицы (не меньше 1): '))
size_of_matrix = m * n  # размер матрицы
arr = list(map(int, input('Введите массив длинной {:}: '.format(size_of_matrix)).split()))
while len(arr) != size_of_matrix:
    arr = list(map(int, input('Неверная длина массива. Введите массив длинной {:}: '.format(size_of_matrix)).split()))

# Блок 2: заполнение матрицы
matrix = [[0 for _ in range(n)] for _ in range(m)]
curr_index = 0  # текущий индекс в списке
top_index, left_index, bottom_index, right_index = 0, 0, m - 1, n - 1  # индексы верха, левого бока, низа и правого
# бока, незаполненных спиралями змейки
while top_index <= bottom_index and left_index <= right_index:
    for j in range(left_index, right_index + 1):
        if curr_index < size_of_matrix:
            matrix[top_index][j] = arr[curr_index]
            curr_index += 1
    top_index += 1
    for i in range(top_index, bottom_index + 1):
        if curr_index < size_of_matrix:
            matrix[i][right_index] = arr[curr_index]
            curr_index += 1
    right_index -= 1
    for j in range(right_index, left_index - 1, -1):
        if curr_index < size_of_matrix:
            matrix[bottom_index][j] = arr[curr_index]
            curr_index += 1
    bottom_index -= 1
    for i in range(bottom_index, top_index - 1, -1):
        if curr_index < size_of_matrix:
            matrix[i][left_index] = arr[curr_index]
            curr_index += 1
    left_index += 1

# Блок 3: вывод матрицы
print('Матрица: ')
for i in range(m):
    formatted_line = ['{:6}'.format(member) for member in matrix[i]]
    print(*formatted_line)
