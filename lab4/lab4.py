# Лабораторная работа №4
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: вычисление суммы ряда с точностью до члена ряда ε

# Блок 1: ввод пользователем значения аргумента x, точности, максимального количества итераций и шага печати
x = float(input('Введите значение аргумента x: '))  # аргумент x
eps = float(input('Введите значение точности: '))  # точность вычислений
maximum = int(input('Введите максимальное количество итераций: '))  # максимальное количество итераций
step_of_output = int(input('Введите шаг печати: '))  # шаг печати

# Блок 2: вычисление значений и вывод
iteration = 1  # номер итерации
member_of_sequence_1 = 1  # первая часть члена последовательности
member_of_sequence_2 = x  # вторая часть члена последовательности
sum_of_sequence = member_of_sequence_1 * member_of_sequence_2  # сумма членов последовательности
print('--------------------------------------\n'
      '| № итерации |     t     |     s     |\n'
      '|------------------------------------|')  # создание заголовка таблицы промежуточных значений
while iteration <= maximum:
    if (iteration - 1) % step_of_output == 0:
        print('| {0:<10g} | {1:<9.7f} | {2:<9.7f} |'.format(iteration, member_of_sequence_1 * member_of_sequence_2,
                                                            sum_of_sequence))  # вывод промежуточных значений по
        # заданному пользователем шагу
    iteration += 1
    member_of_sequence_1 *= (iteration * 2 - 3) / (iteration * 2 - 2)  # вычисление первой части члена
    # последовательности
    member_of_sequence_2 *= x**2 * (iteration * 2 - 3) / (iteration * 2 - 1)  # вычисление второй части члена
    # последовательности
    if abs(member_of_sequence_1 * member_of_sequence_2) > eps:
        sum_of_sequence += member_of_sequence_1 * member_of_sequence_2  # подсчет суммы членов последовательности
    else:
        if (iteration - 1) % step_of_output == 0:
            print('| {0:<10g} | {1:<9.7f} | {2:<9.7f} |'.format(iteration, member_of_sequence_1 * member_of_sequence_2,
                                                                sum_of_sequence))
        print('--------------------------------------')
        print('Сумма бесконечного ряда: {0:.7f}, вычислена за количество итераций: {1:g}'.format(sum_of_sequence,
                                                                                                 iteration))
        break
else:
    print('--------------------------------------')
    print('За указанное количество итераций достичь необходимой точности не удалось')
