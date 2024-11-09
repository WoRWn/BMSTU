# Лабораторная работа №9 задание 6
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: заменить все согласные латинские буквы в матрице символов на заглавные, а все гласные латинские
# буквы на строчные

# Блок 1: ввод исходной матрицы
matrix = []
length = int(input('Введите количество строк матрицы (минимум 1): '))  # количество строк матрицы
while length < 1:  # проверка на длину матрицы
    length = int(input('Неверный ввод. Введите количество строк матрицы (минимум 1): '))
width = 0  # ширина матрицы
for i in range(length):
    line = []
    symbols = []
    while (i != 0 and len(line) != len(matrix[i-1])) or len(line) < 1 or max(symbols) > 1:
        line = list(map(str, input('Введите {:} строку матрицы: '.format(i+1)).split()))
        symbols = [len(x) for x in line]  # количество символов в каждом элементе строки
        width = len(line)  # ширина матрицы
    matrix += [line]  # добавление в матрицу новой строки

# Блок 2: вывод исходной матрицы
print('Исходная матрица: ')
for i in range(length):
    formatted_line = ['{:6}'.format(member) for member in matrix[i]]
    print(*formatted_line)

# Блок 3: изменение матрицы
ids_vowels = 'AEIOUY'  # список порядковых номеров заглавных гласных букв английского языка в Unicode
ids_consonants = 'bcdfghjklmnpqrstvwxz'  # список порядковых номеров строчных согласных букв
# английского языка в Unicode
for i in range(length):
    for j in range(width):
        if matrix[i][j] in ids_consonants:
            matrix[i][j] = matrix[i][j].upper()  # замена согласных
        elif matrix[i][j] in ids_vowels:
            matrix[i][j] = matrix[i][j].lower()  # замена гласных

# Блок 4: вывод измененной матрицы
print('Измененная матрица: ')
for i in range(length):
    formatted_line = ['{:6}'.format(member) for member in matrix[i]]
    print(*formatted_line)
