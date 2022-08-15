# создаем списки
list_1 = input('Введите элементы 1-го списка через запятую: ').split(',')
list_2 = input('Введите элементы 2-го списка через запятую: ').split(',')
print(list_1, list_2)
for el in list_1[:]:
    if el in list_2:
        list_1.remove(el)
print(list_1, list_2)


