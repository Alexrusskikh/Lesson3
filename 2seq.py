import re
my_list = input("Введите ряд цифр через запятую: ")
#несколько разделителей не получается назначить re.split(',|,|/', str)
my_list = re.split("[,!?:/;]", my_list)
print(sorted(set(my_list)))

