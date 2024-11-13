# Рубежный контроль №2 номер 2

# Назначение программы: 1) повернуть квадраты с нечетным номером в квадратной матрице
#                       2) найти первый такой столбец, сумма его значений чаще всего встречается среди сумм столбцов
#                       матриц.

from math import inf


# Просто функция для отформатированного вывода матрицы
def print_matrix(m1, n):
    for i1 in range(n):
        formatted_line = ['{:6d}'.format(member) for member in m1[i1]]
        print(*formatted_line)


"""
# Просто функция для авто-создания квадратных матриц по заданному порядку (удобно для проверки поворота)
def auto_matrix(ln):
    m2 = []
    num = 0
    for x in range(ln):
        line = []
        for y in range(ln):
            line.append(num)
            num += 1
        m2.append(line)
    return m2
"""

# Ввод порядка матрицы и самой матрицы
length = int(input('Введите порядок матрицы: '))  # ввод порядка матрицы

# matrix = auto_matrix(length)  # создание матрицы

matrix = []
while length < 1:  # проверка на длину матрицы
    length = int(input('Неверный ввод. Введите порядок матрицы (минимум 1): '))
width = 0  # ширина матрицы
for i in range(length):
    line = []
    while width != length or len(line) < 1:
        line = list(map(int, input('Введите {:} строку матрицы: '.format(i+1)).split()))
        width = len(line)
    matrix += [line]  # добавление в матрицу новой строки

# Вывод исходной матрицы
print('Исходная матрица: ')
print_matrix(matrix, length)
print()

# Поворот нечетных квадратов в матрице
for i in range(0, length // 2, 2):
    first = i
    last = length - 1 - i
    for j in range(i, length - i - 1):
        offset = j - first
        matrix[first][j], matrix[last-offset][first], matrix[last][last-offset], matrix[j][last] = \
            matrix[last-offset][first], matrix[last][last-offset], matrix[j][last], matrix[first][j]

# Вывод измененной матрицы
print('Измененная матрица: ')
print_matrix(matrix, length)
print()

# Поиск столбца, сложность O(n³)
max_count = 0
index_of_column = -inf
for j in range(length):
    column_sum = 0
    for i in range(length):
        column_sum += matrix[i][j]
    count = 0
    for k in range(j+1, length):
        sum_to_compare = 0
        for m in range(length):
            sum_to_compare += matrix[m][k]
        if sum_to_compare == column_sum:
            count += 1
    if count > max_count:
        max_count = count
        index_of_column = j

# Вывод столбца
if index_of_column != -inf:
    print('Подходящий столбец: ')
    for i in range(length):
        print(matrix[i][index_of_column])
else:
    print('Подходящего столбца не существует')
