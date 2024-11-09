# Лабораторная работа №9 задание 4
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: найти максимальные элементы в каждой из заданных списком I строк матрицы, среднее значение
# максимумов

from math import inf  # импорт функции inf модуля math

# Блок 1: ввод исходной матрицы
matrix = []
length = int(input('Введите количество строк матрицы (минимум 1): '))  # количество строк матрицы
while length < 1:  # проверка на длину матрицы
    length = int(input('Неверный ввод. Введите количество строк матрицы (минимум 1): '))
width = 0  # ширина матрицы
for i in range(length):
    line = []  # строка матрицы
    while (i != 0 and len(line) != len(matrix[i-1])) or len(line) < 1:
        line = list(map(int, input('Введите {:} строку матрицы: '.format(i+1)).split()))
        width = len(line)  # ширина матрицы
    matrix += [line]  # добавление в матрицу новой строки

# Блок 2: ввод исходного списка
length_i = int(input('Введите длину списка I: '))
list_i = []  # список I
for i in range(length_i):
    num = int(input('Введите {:} требуемый номер строки матрицы: '.format(i+1)))
    while num < 0 or num > length:
        num = int(input('Неверный ввод. Введите {:} требуемый номер строки матрицы: '.format(i+1)))
    list_i.append(num)

# Блок 3: вывод исходной матрицы
print('Исходная матрица: ')
for i in range(length):
    formatted_line = ['{:6d}'.format(member) for member in matrix[i]]
    print(*formatted_line)

# Блок 4: вывод списка I
formatted_list_i = ['{:6d}'.format(member) for member in list_i]
print('Список I: ', *formatted_list_i)

# Блок 5: поиск максимальных значений и их среднего арифметического
max_elem = -inf  # максимальный элемент в строке
list_r = []  # список R максимальных значений в строках матриц
sum_r = 0  # сумма значений списка максимумов
aver = 0  # среднее арифметическое максимумов
for i in list_i:
    for elem in matrix[i-1]:
        if elem > max_elem:
            max_elem = elem  # обновляем максимум для текущей строчки
    list_r.append(max_elem)  # добавляем максимум в список R
    sum_r += max_elem  # увеличиваем сумму значений списка R
    max_elem = 0  # обнуляем максимум для перехода к новой строке
aver = sum_r / len(list_i)  # расчет среднего арифметического максимумов

# Блок 6: вывод списка R и среднего максимумов
formatted_list_r = ['{:6d}'.format(member) for member in list_r]
print('Список R: ', *formatted_list_r)
print('Среднее арифметическое максимумов: {:g}'.format(aver))
