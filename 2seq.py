import  re
num_str = input('Введите ряд чисел через запятую: ')
num_str_list = re.split('[,!?:/;]', num_str)
list_num = [int(n) for n in num_str_list]
result = list(set(list_num))
for el in  result:
    print(el, end=', ')



