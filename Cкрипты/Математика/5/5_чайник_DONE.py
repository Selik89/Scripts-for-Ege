import random

# Генерируем вероятности для чайника
prob_more_than_one_year = random.randint(95, 99)  # 0.95 - 0.99
prob_more_than_two_years = random.randint(85, prob_more_than_one_year - 5)  # меньше чем prob_more_than_one_year

fl_prob_more_than_one_year = float(f'0.{prob_more_than_one_year}')
fl_prob_more_than_two_years = float(f'0.{prob_more_than_two_years}')

text = f"""
Вероятность того, что новый электрический чайник прослужит больше года, равна {fl_prob_more_than_one_year}. 
Вероятность того, что он прослужит больше двух лет, равна {fl_prob_more_than_two_years}. 
Найдите вероятность того, что он прослужит меньше двух лет, но больше года.
"""

right_answer = round(fl_prob_more_than_one_year - fl_prob_more_than_two_years, 2)

text_of_solve = f"""
Обозначим события:
A — чайник прослужит больше года,
B — чайник прослужит больше двух лет.

Дано:
P(A) = {fl_prob_more_than_one_year}
P(B) = {fl_prob_more_than_two_years}

Найти: вероятность того, что чайник прослужит меньше двух лет, но больше года.

Событие «чайник прослужит меньше двух лет, но больше года» — это разность событий A и B.
Вероятность этого события равна:
P(A \\ B) = P(A) - P(B) = {fl_prob_more_than_one_year} - {fl_prob_more_than_two_years} = {right_answer}

Ответ: {right_answer}
"""

# выводы
print(text)
print(right_answer)
print('__________________________')
print(text_of_solve)