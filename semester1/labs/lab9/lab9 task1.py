# Лабораторная работа №9 задание 1
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: сформировать матрицу M из списков A и B такую, что m[i][j] = a[i]*b[j] и определить количество
# полных квадратов в каждой строке матрицы

# Блок 1: ввод списка A
a = []  # список A
while len(a) < 1:
    a = list(map(int, input('Введите список A: ').split()))

# Блок 2: ввод списка B
b = []  # список B
while len(b) < 1:
    b = list(map(int, input('Введите список B: ').split()))

# Блок 3: формирование матрицы
m = []  # матрица
s = []  # список S
for i in range(len(a)):
    count = 0  # обнуляем счетчик полных квадратов
    m.append([])
    for j in range(len(b)):
        new_elem = a[i] * b[j]
        m[i].append(new_elem)  # добавляем значение
        if int(new_elem**0.5)**2 == new_elem:
            count += 1  # увеличиваем значение счетчика
    s.append(count)  # формируем столбец S

# Блок 4: вывод матрицы
print('Матрица M и столбец S: ')
for i in range(len(a)):
    formatted_line = ['{:6}'.format(member) for member in m[i]]  # отформатированная строка матрицы
    print(*formatted_line, '| {:}'.format(s[i]))
