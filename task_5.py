# Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки связанные с рандомом)

import datetime

rand = 0


def get_random():
    return datetime.datetime.now().microsecond % 100


rand = get_random()

print(rand)
