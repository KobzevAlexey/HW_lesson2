# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

n = int(input('Введите число n: '))
dictionary = {}

for i in range(1, n + 1):
    dictionary[i] = round((1 + (1 / i)) ** i, 2)

print(dictionary)
print(sum(dictionary))
