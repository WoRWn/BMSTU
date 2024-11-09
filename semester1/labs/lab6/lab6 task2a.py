# Лабораторная работа №6 задание 2a
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: удаление элемента в заданном месте исходного списка

# Блок 1: ввод исходного списка и индекса, по которому надо удалить элемент
length = int(input('Введите длину исходного списка: '))  # ввод длины списка
while length < 1:  # исключение ошибок ввода длины
    length = int(input('Неверный ввод. Введите длину исходного списка: '))
numbers = []  # создание списка
for i in range(length):
    number = int(input('Введите {:} элемент списка: '.format(i+1)))  # поочередный ввод пользователем элементов
    # списка
    numbers.append(number)
index_of_delete_number = int(input('Введите индекс списка, по которому надо удалить элемент (от 0 до {:}): '
                                   .format(length - 1)))
while index_of_delete_number < 0 or index_of_delete_number > length - 1:
    index_of_delete_number = int(input('Неправильный ввод. Введите индекс списка,  по которому надо удалить элемент'
                                       '(от 0 до {:}): '.format(length - 1)))

# Блок 2: изменение списка
numbers.pop(index_of_delete_number)

# Блок 3: вывод измененного списка
for i in range(length-1):
    print('{0:} элемент списка: {1:}'.format(i+1, numbers[i]))

