# Лабораторная работа №1
# Гаев Дмитрий ИУ7-14Б

# Назначение программы: по заданной длине ребра додекаэдра определить площадь его поверхности, объем, радиусы
# вписанной и описанной сфер


from math import sqrt

# Блок 1: ввод пользователем значения ребра додекаэдра и проверка входного значения
a_dodecahedron = float(input('Введите длину ребра додекаэдра: '))  # ввод пользователем длины ребра додекаэдра
correctly_entered_value = 0  # переменная для проверки правильности введенного значения
if a_dodecahedron <= 0:
    correctly_entered_value = False  # введено недопустимое значение
else:
    correctly_entered_value = True  # введено допустимое значение

# Блок 2: вычисление значений
s_dodecahedron = 0  # создание переменной площади поверхности додекаэдра
v_dodecahedron = 0  # создание переменной объема додекаэдра
r_inscribed_circle = 0  # создание переменной радиуса вписанной в додекаэдр окружности
r_circumscribed_sircle = 0  # создание переменной радиуса описанной около додекаэдра окружности
if correctly_entered_value is True:
    root_of_5 = sqrt(5)  # оптимизация количества вызова функции sqrt() путем создания переменной корня из 5
    s_dodecahedron = 3 * sqrt(25 + 10 * root_of_5) * a_dodecahedron ** 2  # вычисление площади поверхности додекаэдра
    v_dodecahedron = (15 + 7 * root_of_5) / 4 * a_dodecahedron ** 3  # вычисление объема поверхности додекаэдра
    r_inscribed_circle = (sqrt(250 + 110 * root_of_5)) / 20 * a_dodecahedron  # вычисление радиуса вписанной в додекаэдр
    # сферы
    r_circumscribed_sircle = (sqrt(3) * (1 + root_of_5)) / 4 * a_dodecahedron  # вычисление радиуса описанной около
    # додекаэдра сферы

# Блок 3: вывод
if correctly_entered_value is True:
    print("Площадь поверхности додекаэдра: ", round(s_dodecahedron, 7))  # вывод площади поверхности додекаэдра
    print("Объем поверхности додекаэдра: ", round(v_dodecahedron, 7))  # вывод объема поверхности додекаэдра
    print("Радиус вписанной в додекаэдр сферы: ", round(r_inscribed_circle, 7))  # вывод радиуса вписанной в додекаэдр
    # сферы
    print("Радиус описанной около додекаэдра сферы: ", round(r_circumscribed_sircle, 7))  # вывод описанной около
    # додекаэдра сферы
else:
    print('Введено недопустимое значение (длина ребра додекаэдра - целое положительное число)')  # вывод при неправильно
    # введенном значении
