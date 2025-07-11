import random

smaller_then_810 = random.randint(85, 97)
higher_then_790 = random.randint(78, smaller_then_810 - 5)

prob_of_smaller = float(f'0.{smaller_then_810}')
prob_of_higher = float(f'0.{higher_then_790}')

right_answer = round(prob_of_smaller - (1 - prob_of_higher), 2)
print(right_answer)

text = f"""
При выпечке хлеба производится контрольное взвешивание свежей буханки. 
Известно, что вероятность того, что масса окажется меньше, чем 810 г, равна {prob_of_smaller}. 
Вероятность того, что масса окажется больше, чем 790 г, равна {prob_of_higher}. 
Найдите вероятность того, что масса буханки больше, чем 790 г, но меньше, чем 810 г.
"""

text_of_solve = f"""
Обозначим события:
A — масса буханки меньше 810 г,
B — масса буханки больше 790 г.

Дано:
P(A) = P(m < 810) = {prob_of_smaller}
P(B) = P(m > 790) = {prob_of_higher}

Найти: вероятность того, что масса буханки больше 790 г, но меньше 810 г, то есть P(790 < m < 810).

Рассмотрим:
P(790 < m < 810) = P(m < 810) - P(m ≤ 790)

Из условия:
P(m ≤ 790) = 1 - P(m > 790) = 1 - {prob_of_higher} = {round(1 - prob_of_higher, 2)}

Тогда:
P(790 < m < 810) = {prob_of_smaller} - {1 - prob_of_higher}  = {round(prob_of_smaller - (1 - prob_of_higher), 2)}

Ответ: {prob_of_smaller - (1 - prob_of_higher)}

"""

# выводы
print(text)
print(f'Answer = {right_answer}')
print('___________________________')
print(text_of_solve)