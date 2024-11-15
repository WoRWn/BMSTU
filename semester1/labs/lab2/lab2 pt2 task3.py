# Лабораторная работа №2 часть №2 задание №3
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: по заданному значениям координат точки (x, y) определить, принадлежит ли точка заданной
# замкнутой области, включая границы

# Блок 1: ввод пользователем координат точки
x = float(input('Введите координату x: '))  # значение аргумента x
y = float(input('Введите координату y: '))  # значение аргумента y

# Блок 2: проверка на принадлежность точки заданной области
flag = False  # создание переменной-флага для проверки на принадлежность области
if x > 0:
    x = -x  # задаем все положительные значения x, как отрицательные для упрощения вычислительной работы программы
    # (так как область, образованная функциями симметрична относительно оси Oy)
if x < -9:
    flag = False  # изменение значения переменной-флага
elif -9 <= x < -8:
    if (y >= 7 * (x + 8)**2 + 1) and (y <= -1 / 8 * (x + 9)**2 + 8):
        flag = True  # изменение значения переменной-флага
elif -8 <= x < -2:
    if ((y >= 1 / 49 * (x + 1)**2) and (y <= -1 / 8 * (x + 9)**2 + 8)) \
            or ((y >= 1 / 3 * (x + 5)**2 - 7) and (y <= -1 / 16 * x**2)):
        flag = True  # изменение значения переменной-флага
elif -2 <= x < -1:
    if ((y >= 1 / 49 * (x + 1)**2) and (y <= -1 / 8 * (x + 9)**2 + 8)) \
            or ((y >= -2 * (x + 1)**2 - 2) and (y <= -1 / 16 * x**2)) or (y == -1.5 * x + 2):
        flag = True  # изменение значения переменной-флага
elif x == -1:
    if -2 <= y <= 0 or y == -1.5 * x + 2:
        flag = True  # изменение значения переменной-флага
elif -1 < x <= 0:
    if (y == -1.5 * x + 2) or ((y >= 4 * x**2 - 6) and (y <= -4 * x**2 + 2)):
        flag = True  # изменение значения переменной-флага

# Блок 3: вывод
if flag is True:
    print('Точка принадлежит заданной области')
else:
    print('Точка не принадлежит заданной области')

# Тесты:
# 9 8
# 1 1
# -8 -4
