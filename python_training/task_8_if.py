# программа проверяет является ли число положительным
# или отрицательным и выводит соответствующее сообщение

num = 3

if num >= 0:
    print('Число больше или равно 0')
else:
    print('Число отрицательное')


def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('Да')
    else:
        print('Нет')


task_yes_no(str_1='test', str_2='testing')


num_float = 3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('бакалавр')
    elif year_of_study in range(5, 7):
        print('магистр')
    elif year_of_study in range(7, 10):
        print('аспирант')
    else:
        print('Введите корректный год обучения')


number = 5

if number > 100 or number < -100:
    print('-')
else:
    print('+')
