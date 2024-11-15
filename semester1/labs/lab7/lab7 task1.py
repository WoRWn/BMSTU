# Лабораторная работа №7 задание 1 вариант 3
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: удалить все нечетные элементы списка

# Блок 1: ввод исходного списка
length = int(input('Введите длину исходного списка: '))  # ввод длины списка
while length < 1:  # исключение ошибок ввода длины
    length = int(input('Неверный ввод. Введите длину исходного списка: '))
numbers = []  # создание списка
for i in range(length):
    number = int(input('Введите {:} элемент списка: '.format(i+1)))  # поочередный ввод пользователем элементов
    # списка
    numbers.append(number)

# Блок 2: изменение списка
current_index = 0  # переменная текущего индекса
for i in range(length):
    if abs(numbers[i]) % 2 == 0:
        numbers[current_index] = numbers[i]  # перезаписываем подходящие числа
        current_index += 1  # увеличиваем текущий индекс

# Блок 3: вывод списка
for i in range(current_index):
    print('{0:} элемент списка: {1:}'.format(i + 1, numbers[i]))
