# import random
#
#
# def random_people():
#     famous_people = {'Натальи Русских': '08.03.1977', 'Алексея Русских': '29.07.1973'}
#     name, date = random.choice(list(famous_people.items()))
#     return name, date
#
#
# def date_and_que():
#     name, date = random_people()
#     answer = input(f'Укажите  дату рождения {name}: ')
#     if answer == date:
#         print('Поздравляю, вы выиграли квартиру!')
#     else:
#         print('не верно')
#
# if __name__ == '__main__':
#     print(__name__)
bill_sum = 0
history = []

def buy(bill_sum):
    cost = int(input('Введите сумму покупки: '))
    if cost > bill_sum:
        print('Недостаточно средств ! ')
    else:
        bill_sum -= cost
        name = input('Введите название покупки: ')
        history.append((name, cost))
    return bill_sum


def separator(symbol, count):
    return symbol * count

print(separator('*', 20))

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счет {bill_sum}: ')
    print(separator('*', 20))
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        cost = int(input('Введите сумму: '))
        bill_sum += cost
    elif choice == '2':
        bill_sum = buy(bill_sum)
    elif choice == '3':
        print(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
