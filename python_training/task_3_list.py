a = [5, 10, 15, 29, 25, 30, 35,40]

print("a[2] = ", a[2])  # a[2] = 15

print("a[0:3] = ", a[0:3])  # a[0:3] = [5, 10, 15] - срез списка

b = [11, 12, 13]
b[2] = 4  # изменение элемента
print(b)

test_list = ['один', 'два', 'три', 'четыре', 'пять']

for elem in test_list:  # цикл, который печатает каждый элемент списка
    print(elem)

print(len(test_list))

test_list.append('шесть')  # добавление элемента в конец списка
print(test_list)