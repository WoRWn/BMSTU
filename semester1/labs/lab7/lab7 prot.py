# Защита лабораторной работы №7

# Назначение программы: зеркально отобразить четные элементы в списке

length = int(input('Введите длину исходного списка: '))
while length < 1:
    length = int(input('Неверный ввод. Введите длину исходного списка: '))
numbers = []
for i in range(length):
    num = int(input('Введите {:} элемент списка: '.format(i+1)))
    numbers.append(num)

print(numbers)

left = 0
right = length - 1
while left < right:
    while left < right and numbers[left] % 2 != 0:
        left += 1
    while left < right and numbers[right] % 2 != 0:
        right -= 1
    if left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        right -= 1
        left += 1

print(numbers)
