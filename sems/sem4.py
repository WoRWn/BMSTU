# Семинар 4. Матрицы

def z1():
    """
    Даны точки на плоскости. Найти наиболее удаленную и наиболее близкую точку к (0, 0) из верхней полуплоскости
    """
    max_distance, min_distance = False, False
    max_point, min_point = None, None
    while string := input():
        x, y = tuple(map(int, string.split()))
        if y > 0:
            distance = (x ** 2 + y ** 2) ** 0.5
            if max_distance == False or distance > max_distance:
                max_distance = distance
                max_point = (x, y)
            elif min_distance == False or distance < min_distance:
                min_distance = distance
                min_point = (x, y)
    print(f'min_point - {min_point}\nmax_point - {max_point}')


def z2():
    """
    Транспонирование матрицы
    """
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
    n = len(m)  # размер квадратной матрицы
    for i in range(n):
        for j in range(i+1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    print(m)


def z3():
    """
    Найти максимальный элемент:
     1) над главной диагональю.
     2) под главной диагональю.
     3) над побочной диагональю.
     4) под побочной диагональю.
     5) над главной и побочной диагональю.
    """
    # Ввод квадратной матрицы
    matrix = []
    line = input('> ').split()
    matrix.append([int(j) for j in line])
    for _ in range(len(line) - 1):
        matrix.append([int(j) for j in input().split()])
    n = len(matrix)

    # # 1.
    # max_up_normal = False
    # for i in range(n - 1):
    #     for j in range(i + 1, n):
    #         if max_up_normal is False or matrix[i][j] > max_up_normal:
    #             max_up_normal = matrix[i][j]

    # # 2.
    # max_down_normal = False
    # for i in range(1, n):
    #     for j in range(i):
    #         if max_down_normal is False or matrix[i][j] > max_down_normal:
    #             max_down_normal = matrix[i][j]

    # # 3.
    # max_up_alt = False
    # for i in range(n - 1):
    #     for j in range(n - i - 1):
    #         if max_up_alt is False or matrix[i][j] > max_up_alt:
    #             max_up_alt = matrix[i][j]

    # # 4.
    # max_down_alt = False
    # for i in range(1, n):
    #     for j in range(n - i - 1, n):
    #         if max_down_alt is False or matrix[i][j] > max_down_alt:
    #             max_down_alt = matrix[i][j]

    # 5.
    # max_up_normal_down_alt = False
    #
    # # по строкам
    # for i in range(1, n - 1):
    #     for j in range(max(i, n - i - 1), n):
    #         if max_up_normal_down_alt is False or matrix[i][j] > max_up_normal_down_alt:
    #             max_up_normal_down_alt = matrix[i][j]
    #
    # по столбцам
    # for j in range(1, n - 1):
    #     for i in range(j, n - j - 1):
    #         if max_up_normal_down_alt is False or matrix[i][j] > max_up_normal_down_alt:
    #             max_up_normal_down_alt = matrix[i][j]

    # for i in range(len(matrix)):
    #     print(matrix[i])
    # print(max_up_normal_down_alt)


def z4():
    """ Из квадратной матрицы A получить матрицу B
    вычеркиванием всех элементов, принадлежащих главной диагонали
    A(N, N) -> B(N, N-1) """

    # Ввод квадратной матрицы
    matrix_a = []
    line = input('> ').split()
    matrix_a.append([int(j) for j in line])
    for _ in range(len(line) - 1):
        matrix_a.append([int(j) for j in input('> ').split()])

    n = len(matrix_a)

    #.
    matrix_b = [[0 for _ in range(n - 1)] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            matrix_b[i][j] = matrix_a[i][j]
            print('1', matrix_b[i][j])
        for j in range(i + 1, n):
            matrix_b[i][j - 1] = matrix_a[i][j]
            print('2', matrix_b[i][j-1])

    print(*matrix_b, sep='\n')

z4()