# создаем списки
list_1 = input('Введите элементы 1-го списка через запятую: ').split(',')
list_2 = input('Введите элементы 2-го списка через запятую: ').split(',')
print(list_1, list_2)
res = []
for el in list_1:
    if el not in list_2:
        res.append(el)
list_1 = res
print(list_1, list_2)


#Вариант
# создаем списки
list_1 = input('Введите элементы 1-го списка через запятую: ').split(',')
list_2 = input('Введите элементы 2-го списка через запятую: ').split(',')
print(list_1, list_2)
#копия list_1, но не понял  зачем, для наглядности?
res = list_1[:]
for el in list_1[:]:
    if el in list_2:
        res.remove(el)
print(list_1, list_2, res)