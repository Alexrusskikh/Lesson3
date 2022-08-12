print('Примите участие в исторической викторине')
# общий список вопросов
all_question = []
# вопросы как элементы списка question в варианте мини списков с ответами
q1 = ['И.А.Крылова ', '13.02.1769']
q2 = ['П.И.Чайковского ', '07.05.1840']
q3 = ['Г.К.Жукова ', '01.12.1896']
q4 = ['Ю.А.Гагарина ', '09.03.1934']
q5 = ['В.И.Ленина ', '22.04.1870']
q6 = ['С.А.Есенина ', '03.10.1895']
q7 = ['Фридерика Шопена ', '01.03.1810']
q8 = ['Ф.М.Достоевского ', '11.11.1821']
q9 = ['В.С.Высоцкого ', '25.01.1938']
q10 = ['М.А.Булгакова ', '15.05.1891']
# добавление вопросов в список
all_question.append(q1)
all_question.append(q2)
all_question.append(q3)
all_question.append(q4)
all_question.append(q5)
all_question.append(q6)
all_question.append(q7)
all_question.append(q8)
all_question.append(q9)
all_question.append(q10)

import random
# 5 - количество случайных вопросов
use_question = random.sample(all_question, 5)
#Это подсказка

# верные ответы
right_answer = 0
# неверные ответы
wrong_answer = 0

newRound = "да"
while newRound == "да":
    for i in use_question:
        answer = input("Укажите дату рождения "+i[0]+"в формате 'dd.mm.yyyy'-"+i[1]+":\n")
        if answer == i[1]:
            print("Верно!!!")
            right_answer += 1
        else:
            print("Не верно... Правильный ответ - ", (i[1]))
            wrong_answer += 1

        percent_right = (right_answer * 100) / 5
        percent_wrong = (wrong_answer * 100) / 5
    print(f'Правильных ответов -  {right_answer},  это {percent_right} %')
    print(f'Неверных ответов -  {wrong_answer}, это {percent_wrong} %')
    newRound = input("Хотите начать заново? (Да-Нет): ")
    newRound = newRound.lower()
print("Викторина завершена")