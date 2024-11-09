# Лабораторная работа №6 задание 1b
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: добавление элемента в заданное место исходного списка алгоритмически

# Блок 1: ввод исходного списка, ввод нового элемента списка и индекса, на который его надо вставить
length = int(input('Введите длину исходного списка: '))  # ввод длины списка
while length < 0:  # исключение ошибок ввода длины
    length = int(input('Неверный ввод. Введите длину исходного списка: '))
numbers = []  # создание списка
for i in range(length):
    number = int(input('Введите {:} элемент списка: '.format(i+1)))  # поочередный ввод пользователем элементов
    # списка
    numbers.append(number)
new_number = int(input('Введите элемент, который надо добавить в список: '))  # ввод нового элемента
index_of_new_number = int(input('Введите индекс списка, на который надо вставить элемент (от 0 до {:}): '
                                .format(length)))
while index_of_new_number < 0 or index_of_new_number > length:
    index_of_new_number = int(input('Неправильный ввод. Введите индекс списка, на который надо вставить элемент '
                                    '(от 0 до {:}): '.format(length)))

# Блок 2: изменение списка
numbers.append(None)
for i in range(length, index_of_new_number, -1):
    numbers[i] = numbers[i-1]
numbers[index_of_new_number] = new_number

# Блок 3: вывод измененного списка
for i in range(length+1):
    print('{0:} элемент списка: {1:}'.format(i+1, numbers[i]))
