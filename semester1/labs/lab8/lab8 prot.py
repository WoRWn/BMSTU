# Защита лабораторной работы №8

# Назначение программы: транспонировать среднюю часть квадратной матрицы (квадрат с отступами N//4 
# от каждой границы матрицы, где N - её порядок)

matrix = []
length = int(input('Введите порядок матрицы (минимум 1): '))
while length < 1:
    length = int(input('Неверный ввод. Введите порядок матрицы (минимум 1): '))
width = 0
for i in range(length):
    line = []
    while width != length or len(line) < 1:
        line = list(map(int, input('Введите {:} строку матрицы: '.format(i+1)).split()))
        width = len(line)
    matrix += [line]

# matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
#           [9, 10, 11, 12, 13, 14, 15, 16, 17],
#           [18, 19, 20, 21, 22, 23, 24, 25, 26],
#           [27, 28, 29, 30, 31, 32, 33, 34, 35],
#           [36, 37, 38, 39, 40, 41, 42, 43, 44],
#           [45, 46, 47, 48, 49, 50, 52, 52, 53],
#           [54, 55, 56, 57, 58, 59, 60, 61, 62],
#           [63, 64, 65, 66, 67, 68, 69, 70, 71],
#           [72, 73, 64, 75, 76, 77, 78, 79, 80]]
# length = 9

print('Исходная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)

if length % 2 == 0:
    center_1 = length // 4
    center_2 = length // 4 * 3
else:
    center_1 = length // 4
    center_2 = length // 4 * 3 + 1

for i in range(center_1, center_2):
    for j in range(i + 1, center_2):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print('Измененная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)
