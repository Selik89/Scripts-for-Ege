import random
import itertools


def solve(
        question, even_odd, second_condition,
        letters_for_first_condition, letter_for_second_condition, length, word,
        first_condition

):
    k = 0
    last = 0
    num = 1

    # Сортируем буквы для правильного алфавитного порядка
    sorted_word = sorted(word)

    for p in itertools.product(sorted_word, repeat=dict[length]):
        # Проверяем условие чётности номера
        even_odd_check = True
        if even_odd == " c чётным номером":
            even_odd_check = (num % 2 == 0)
        elif even_odd == " c нечётным номером":
            even_odd_check = (num % 2 != 0)

        # Проверяем первое условие (начинается на/не начинается на)
        first_condition_check = False
        if first_condition == 'начинается на' or first_condition == 'начинаются на':
            first_condition_check = (p[0] in letters_for_first_condition)
        elif first_condition == 'не начинается на' or first_condition == 'не начинаются на':
            first_condition_check = (p[0] not in letters_for_first_condition)

        # Проверяем второе условие (содержит/не содержит)
        second_condition_check = False
        sc = second_condition.split()

        if len(sc) == 4:  # "содержит ровно две О" или "не содержит ровно две О"
            if sc[0] == 'содержит' or sc[0] == 'содержат':
                count = p.count(letter_for_second_condition)
                if sc[1] == 'ровно':
                    if sc[2] == 'одну':
                        second_condition_check = (count == 1)
                    elif sc[2] == 'две':
                        second_condition_check = (count == 2)
                elif sc[1] == 'не' and sc[2] == 'менее':
                    if sc[3] == 'одной':
                        second_condition_check = (count >= 1)
                    elif sc[3] == 'двух':
                        second_condition_check = (count >= 2)
                elif sc[1] == 'не' and sc[2] == 'более':
                    if sc[3] == 'одной':
                        second_condition_check = (count <= 1)
                    elif sc[3] == 'двух':
                        second_condition_check = (count <= 2)
            else:  # "не содержит"
                count = p.count(letter_for_second_condition)
                if sc[1] == 'ровно':
                    if sc[2] == 'одну':
                        second_condition_check = (count != 1)
                    elif sc[2] == 'две':
                        second_condition_check = (count != 2)
        elif len(sc) == 3:  # "содержит ровно две" или "не содержит О"
            if sc[0] == 'содержит' or sc[0] == 'содержат':
                if sc[1] == 'ровно':
                    count = p.count(letter_for_second_condition)
                    if sc[2] == 'одну':
                        second_condition_check = (count == 1)
                    elif sc[2] == 'две':
                        second_condition_check = (count == 2)
            else:  # "не содержит"
                second_condition_check = (letter_for_second_condition not in p)
        else:  # "содержит О" или "не содержит О"
            if second_condition == 'содержит' or second_condition == 'содержат':
                second_condition_check = (letter_for_second_condition in p)
            else:
                second_condition_check = (letter_for_second_condition not in p)

        # Если все 1 условия выполняются
        if even_odd_check and first_condition_check and second_condition_check:
            k += 1
            last = num

        num += 1

    if question == 'под каким номером в этом списке стоит последнее слово':
        return last
    else:
        return k


dict = {
    'под каким номером в этом списке стоит последнее слово': 'которое',
    'количество слов':'которые',
    'пятибуквенные' : 5,
    'шестибуквенные': 6
}


# -- количество букв
length = random.choice(['пятибуквенные', 'шестибуквенные'])

# -- загружаем слова и выбираем рандомное

all_words = [s for s in open('8.txt')]
word = random.choice(all_words)[:-1]
letters_in_word = ', '.join(word)
letters = [s for s in word]


# -- чётное/нечётное
even_odd = random.choice([' c чётным номером', ' c нечётным номером', ""])

# -- вопрос

question = random.choice(['под каким номером в этом списке стоит последнее слово', 'количество слов'])
# подбор условий
if question == 'количество слов':
    possible_conditions = ['начинаются на', 'не начинаются на', 'содержат', "не содержат"]
else:
    possible_conditions = ['начинается на', 'не начинается на', 'содержит', "не содержит"]
while True:
    first_condition = random.choice(possible_conditions[:2])
    second_condition = random.choice(possible_conditions[2:])
    if first_condition != second_condition:
        break


# подбор 1 условия для второго 1 условия
if second_condition == "содержит" or second_condition == "содержат":
    flag = True
    condition_for_second_condition = random.choice(['ровно', 'не менее', 'не более'])
    if condition_for_second_condition == 'ровно':
        cnt_for_second_condition = random.choice(['одну', 'две'])
    else:
        cnt_for_second_condition = random.choice(['одной', 'двух'])

    second_condition =f'{second_condition} {condition_for_second_condition} {cnt_for_second_condition}'



# подбор букв для условий
# -- 1 условие.txt

if random.randint(1, 2) == 2:
    while True:
        first_letter_for_first_condition = random.choice(letters)
        second_letter_for_first_condition = random.choice(letters)
        letters_for_first_condition = [first_letter_for_first_condition, second_letter_for_first_condition]
        if first_letter_for_first_condition != second_letter_for_first_condition:
            break

    letters.remove(first_letter_for_first_condition)
    letters.remove(second_letter_for_first_condition)
    string_for_text = f'{first_letter_for_first_condition} или {second_letter_for_first_condition}'
else:
    first_letter_for_first_condition = random.choice(letters)
    letters.remove(first_letter_for_first_condition)
    string_for_text = first_letter_for_first_condition
    letters_for_first_condition = [first_letter_for_first_condition]
# -- 2 условие

letter_for_second_condition = random.choice(letters)

# -- начало списка
i = 1
string_for_dict = ''
for p in itertools.product(sorted(word), repeat = dict[length]):
    if i > len(word):
        string_for_dict += '...'
        break
    string_for_dict += str(i) + '. '
    for s in p:
        string_for_dict += s
    string_for_dict += '\n'
    i += 1

# текст 1 условия
text = f"""
Все {length} слова, составленные из букв {letters_in_word} записаны в алфавитном порядке и пронумерованы.
Вот начало списка:
{string_for_dict}
Определите, {question}{even_odd}, {dict[question]} {first_condition} {string_for_text} и {second_condition} {letter_for_second_condition}.
Примечание. Слово - последовательность идущих подряд букв, не обязательно осмысленная.
"""

result = solve(
    question, even_odd, second_condition,
    letters_for_first_condition, letter_for_second_condition,
    length, word, first_condition
)

# Формируем строку с буквами для первого 1 условия
if len(letters_for_first_condition) == 1:
    first_condition_text = f"начинается на букву '{letters_for_first_condition[0]}'"
else:
    first_condition_text = f"начинается на букву '{letters_for_first_condition[0]}' или '{letters_for_first_condition[1]}'"

# Формируем строку для второго 1 условия
if 'содержит' in second_condition:
    parts = second_condition.split()
    if len(parts) == 3:
        second_condition_text = f"{parts[0]} {parts[1]} {parts[2]} букву '{letter_for_second_condition}'"
    else:
        second_condition_text = f"содержит букву '{letter_for_second_condition}'"
else:
    second_condition_text = f"не содержит букву '{letter_for_second_condition}'"

# Формируем условие чётности
even_odd_text = ""
if even_odd == " c чётным номером":
    even_odd_text = "с чётным номером"
elif even_odd == " c нечётным номером":
    even_odd_text = "с нечётным номером"

# Определяем вопрос и ответ
if question == 'под каким номером в этом списке стоит последнее слово':
    question_text = "под каким номером в этом списке стоит последнее слово"
    answer_text = f"Последнее слово, удовлетворяющее условиям, стоит под номером {result}"
else:
    question_text = "количество слов"
    answer_text = f"Количество слов, удовлетворяющих условиям: {result}"

text_of_solve = f"""
Решение:
1. Всего букв в слове: {len(word)} ({', '.join(word)})
2. Длина слов: {dict[length]} букв
3. Общее количество возможных слов: {len(word)}^{dict[length]} = {len(word) ** dict[length]}
4. Условия для отбора слов:
   - {first_condition_text}
   - {second_condition_text}
   - {even_odd_text if even_odd_text else "без ограничений по номеру"}
5. Перебираем все возможные комбинации букв длиной {dict[length]} в алфавитном порядке
6. Для каждой комбинации проверяем:
   - Соответствие первому условию: {first_condition_text}
   - Соответствие второму условию: {second_condition_text}
   - Соответствие условию чётности номера: {even_odd_text if even_odd_text else "не важно"}
7. {answer_text}

Ответ: {result}
""".strip()

# выводы

print(text)
print(f'Answer = {result}')
print('________________________________')
print(text_of_solve)



