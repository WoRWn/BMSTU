# Лабораторная работа №2 часть №2 задание №2 вариант №2
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: по заданному значениям координат точки (x, y) определить, принадлежит ли точка заданной
# замкнутой области, включая границы

# Блок 1: ввод пользователем координат точки
x = float(input('Введите координату x: '))  # значение аргумента x
y = float(input('Введите координату y: '))  # значение аргумента y

# Блок 2: проверка на принадлежность точки заданной области
flag = False  # создание переменной-флага для проверки на принадлежность области
if -6 <= x <= -2:
    if (y >= 2*x + 4) and (y <= -0.25 * x**2 + 1):
        flag = True  # изменение значения переменной-флага
elif -2 <= x <= 0:
    if (y <= 2*x + 4) and (y >= -0.25 * x**2 + 1):
        flag = True  # изменение значения переменной-флага
elif 0 <= x <= 2:
    if (y <= -2 * x + 4) and (y >= -0.25 * x ** 2 + 1):
        flag = True  # изменение значения переменной-флага
elif 2 <= x <= 6:
    if (y >= -2 * x + 4) and (y <= -0.25 * x ** 2 + 1):
        flag = True  # изменение значения переменной-флага

# Блок 3: вывод
if flag is True:
    print('Точка принадлежит заданной области')
else:
    print('Точка не принадлежит заданной области')

# Тесты:
# 0 4
# -2 0
# -6 -8
# 5 2
# 0 0
# 0 2