#Создание пустого списка
my_list = []
#Ввод  количества  элементов списка
length_list = int(input('Введите количество элементов списка: '))
#Цикл  ввода количества  элементов списка
for i in range(1, length_list+1):
    print (i)
    num = int(input(f'Введите {i} элемент: '))
    my_list.append(num)
    i+= 15
#вывод отсортированного списка
print(sorted(my_list))