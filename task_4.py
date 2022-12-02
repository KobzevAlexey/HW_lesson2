# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Введите значение N: '))
lst = []
for i in range(-num, num + 1):
    lst.append(i)

print(lst)

multy = 1
with open('file.txt', 'r') as data:
    for line in data:
        multy *= lst[int(line)]
print(multy)
