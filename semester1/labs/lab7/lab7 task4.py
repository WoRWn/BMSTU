# Лабораторная работа №7 задание 4 вариант 4
# Гаев Дмитрий ИУ7-14Б
# все сдал
# Назначение программы: замена всех заглавных гласных английских букв на строчные в каждой строке списка

# Блок 1: ввод исходного списка
length = int(input('Введите длину исходного списка: '))  # ввод длины списка
while length < 1:  # исключение ошибок ввода длины
    length = int(input('Неверный ввод. Введите длину исходного списка: '))
lines = []  # создание списка
for i in range(length):
    line = str(input('Введите {:} строку списка: '.format(i+1)))  # поочередный ввод пользователем строк
    # списка
    lines.append(line)

# Блок 2: изменение списка
ids = (65, 69, 73, 79, 85, 89)  # множество порядковых номеров заглавных гласных букв английского языка в Unicode
for i in range(length):
    line = lines[i]  # текущая строка
    new_line = ''  # новая строка
    for symbol in line:
        if ord(symbol) in ids:
            new_line += chr(ord(symbol) + 32)  # добавляем в новую строку строчную гласную
        else:
            new_line += symbol  # добавляем в новую строку символ, если это не заглавная гласная
    lines[i] = new_line  # перезаписываем текущую строку списка на новую

# Блок 3: вывод списка
for i in range(length):
    print('{0:} элемент списка: {1:}'.format(i + 1, lines[i]))


