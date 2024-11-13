# Рубежный контроль №2 номер 1

# Назначение программы: 1) объединить два упорядоченных по неубыванию массива в новый упорядоченный по неубыванию;
#                       2) поменять местами максимальный нечетный элемент с минимальным четным

# Просто массивы для примера
arr_1 = [0, 1, 3, 5, 6, 8, 11, 15]
arr_2 = [-2, -1, 2, 3, 4, 7, 9]
len_1 = len(arr_1)
len_2 = len(arr_2)

# Заполнение нового списка по неубыванию элементами из первого и второго
index_1 = 0
index_2 = 0
new_arr = [0] * (len_1 + len_2)
while (index_1 + index_2) < (len_1 + len_2):
    if index_2 == len_2 or (index_1 < len_1 and arr_1[index_1] < arr_2[index_2]):
        new_arr[index_1 + index_2] = arr_1[index_1]
        index_1 += 1
    else:
        new_arr[index_1 + index_2] = arr_2[index_2]
        index_2 += 1

# Поиск индексов минимального четного и максимального нечетного элементов
min_ind = -1
max_ind = -1
for i in range(len_1 + len_2):
    if new_arr[i] % 2 != 0:
        max_ind = i
    else:
        if min_ind < 0:
            min_ind = i

# Перестановка элементов
if min_ind != -1 and max_ind != -1:
    new_arr[min_ind], new_arr[max_ind] = new_arr[max_ind], new_arr[min_ind]

print('Новый массив: ', *new_arr)
