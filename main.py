#Первая задача
def funcia():
    for i, n in zip(id, number):
        print(f'id : {i},  номер : {n}')


def sort(sampl, convert):
    n = len(sampl)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sampl[j] > sampl[j + 1]:
                sampl[j], sampl[j + 1] = sampl[j + 1], sampl[j]
                convert[j], convert[j + 1] = convert[j + 1], convert[j]


id = [3, 5, 1, 6, 2, 4]
number = [11, 65, 34, 24, 76, 87]

while 1:
    print(f'1. Отсортировать по идентификационным кодам\n'
          f'2. Отсортировать по номерам телефона\n'
          f'3. Вывести список пользователей с кодами и телефонами\n'
          f'4 .Выход')
    a = int(input())
    if a == 1:
        sort(id, number)
        funcia()
    elif a == 2:
        sort(number, id)
        funcia()
    elif a == 3:
        funcia()
    elif a == 4:
        break

#Вторая задача

def funcia():
    for i, n in zip(id, number):
        print(f'Название книги : {i},  Год выпуска : {n}')


def sort(sampl, convert):
    n = len(sampl)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sampl[j] > sampl[j + 1]:
                sampl[j], sampl[j + 1] = sampl[j + 1], sampl[j]
                convert[j], convert[j + 1] = convert[j + 1], convert[j]


id = ['Грокаем алгоритмы', 'Война и Мир',  'Звёздные войны']
number = [1900, 2010, 1890]

while 1:
    print(f'1. Отсортировать по названию книг\n'
          f'2. Отсортировать по годам выпуска\n'
          f'3. Вывести список книг с названиями и годами выпуска\n'
          f'4 .Выход')
    a = int(input())
    if a == 1:
        sort(id, number)
        funcia()
    elif a == 2:
        sort(number, id)
        funcia()
    elif a == 3:
        funcia()
    elif a == 4:
        break
