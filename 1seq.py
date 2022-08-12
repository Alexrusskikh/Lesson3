#Создание пустого списка
my_list = []
#Запуск отсчета элементов
index = 1
#Ввод  количества  элементов списка
length_list = int(input('Введите количество элементов списка: '))
#Цикл  ввода количества  элементов списка
while len(my_list) != length_list:
    num = int(input(f'Введите {index} элемент: '))
    my_list.append(num)
    index += 1
#вывод отсортированного списка
print(sorted(my_list)
