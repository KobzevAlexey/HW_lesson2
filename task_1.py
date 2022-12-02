# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Введите вещественное число: ')

summa = 0

for digit in num:
    if digit.isdigit():
        summa += int(digit)

print(summa)
