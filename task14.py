print('Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.')
max_number = int(input('Введиче масимальное число: '))
i = 0
count = 0
# Перввый вариант while
while i**2 < max_number:
    print(i**2)
    i += 1
# Второйй вариант for
for i in range (max_number):
    count = i**2
    if count < max_number:
        print(count)

