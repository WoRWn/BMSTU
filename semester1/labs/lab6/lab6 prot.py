# Защита лабораторной работы №6

# Назначение программы: в заданном списке поменять местами первые вхождения самых часто встречающихся элементов

length = int(input('Введите длину списка (минимум 2): '))
while length < 2:
    length = int(input('Неверный ввод. Введите длину списка (минимум 2): '))
numbers = []
max_num = 0
for i in range(length):
    num = int(input('Введите {:} элемент списка: '.format(i+1)))
    numbers.append(num)
    if num > max_num:
        max_num = num

arr = [0] * (max_num + 1) * 2
max_count_1 = max_count_2 = 0
num1 = num2 = None
for i in range(length):
    arr[numbers[i]] += 1
    if arr[numbers[i]] > max_count_1 and num2 != numbers[i]:
        max_count_1, num1 = arr[numbers[i]], numbers[i]
    elif arr[numbers[i]] > max_count_2:
        max_count_2, num2 = arr[numbers[i]], numbers[i]
    if arr[numbers[i]] == 1:
        arr[numbers[i] + max_num + 1] = i
first_index_1, first_index_2 = arr[num1 + max_num + 1], arr[num2 + max_num + 1]
numbers[first_index_1], numbers[first_index_2] = numbers[first_index_2], numbers[first_index_1]

for i in range(length):
    print('{:} элемент списка: {:}'.format(i+1, numbers[i]))
