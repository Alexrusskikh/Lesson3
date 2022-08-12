'''тип  данных список (list), методы:
result_list.append(el) - Добавить элемент el в конец списка result_list
result_list.extend(my_list) - добавить в конец элементы списка my_list
result_list.remove(el) - Удалить из списка первый элемент со значением el
result_list.count(el) - Возвращает количество элементов списка со значением el
result_list.index(el) - Получить позицию (индекс) первого элемента со значением el'''

'''тип  данных строка (str), методы:
len(строка) - Возвращает длину строки
строка.split(<разделитель>) - Разбить строку по разделителю
<разделитель>.join(список) - Собрать строку из списка с указанным разделителем
строка.title() - Перевести первую букву каждого слова в верхний регистр, остальные - в нижний
строка.upper()  - Преобразовать строку к верхнему регистру
строка.lower() - Преобразовать строку к нижнему регистру'''

'''тип  данных множество (set), методы:
.add(el) - Добавить элемент в множество
.remove(el) - Удалить элемент из множества. Если элемент отсутствует — ошибка KeyError
len(s) - число элементов в множестве (размер множества)
x in s - принадлежит ли x множеству s
set & other & - пересечение '''

'''тип  данных словарь (dict), методы:
.keys() - Возвращает список ключей словаря
values() - Возвращает список значений
items() - Возвращает список кортежей (ключ, значение)
.setdefault(key)  - Возвращает значение, соответствующее ключу. Если ключ
отсутствует, создаётся элемент с указанным ключом и значением None
dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
'''