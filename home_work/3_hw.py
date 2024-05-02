def task_1(a, b):
    if a > b:
        print(a)
    else:
        print(b)


task_1(35, 17)


def task_2(c, d):
    if c - d == 135 or c - d == -135:
        print('Yes')
    else:
        print('No')


task_2(25, 140)


def task_3(month: int):
    if month in range(3, 6):
        print('весна')
    elif month in range(6, 9):
        print('лето')
    elif month in range(9, 12):
        print('осень')
    elif month == 11 or month == 12 or month == 1:
        print('зима')
    else:
        print('Введите корректный номер месяца')


task_3(1)


def task_4(e, f, g):
    if e > 10 and f > 10 and g > 10:
        print('Yes')
    else:
        print('No')


task_4(11, 12,13)


def task_5(var: list):
    count = 0
    for elem in var:
        if elem > 0:
            count = count + 1
    print('в этом списке столько положительных чисел -', count)


task_5([3, -6, 1, 0, -9])


def task_6(years: int, months: int):
    count = (years * 12 + months) * 29
    print('В укзанном периоде столько дней -', count)


task_6(6, 3)