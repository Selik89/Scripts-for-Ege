import random

# Генерируем количество ламп (2 или 3)
lamps_count = random.choice([2, 3])

# Генерируем вероятность перегорания лампы
prob_burnout = random.randint(20, 40)  # 0.20 - 0.40
fl_prob_burnout = float(f'0.{prob_burnout}')

# Вероятность того, что лампа НЕ перегорит
prob_not_burnout = round(1 - fl_prob_burnout, 2)

# Вероятность того, что хотя бы одна лампа не перегорит
# Это противоположное событие к "все лампы перегорят"
prob_all_burnout = round(fl_prob_burnout ** lamps_count, 10)
right_answer = 1 - prob_all_burnout

text = f"""
Помещение освещается фонарём с {lamps_count} ламп{'ами' if lamps_count == 2 else 'ами'}. 
Вероятность перегорания лампы в течение года равна {fl_prob_burnout}. 
Найдите вероятность того, что в течение года хотя бы одна лампа не перегорит.
"""

text_of_solve = f"""
Обозначим:
p = {fl_prob_burnout} — вероятность перегорания одной лампы
q = {prob_not_burnout} — вероятность того, что лампа не перегорит (q = 1 - p)

Найти: вероятность того, что хотя бы одна лампа не перегорит.

Событие «хотя бы одна лампа не перегорит» — это противоположное событие к «все лампы перегорят».

Вероятность того, что все {lamps_count} ламп{'ы' if lamps_count == 2 else 'ы'} перегорят:
P(все перегорят) = p^{lamps_count} = {fl_prob_burnout}^{lamps_count} = {prob_all_burnout}

Тогда вероятность того, что хотя бы одна лампа не перегорит:
P(хотя бы одна не перегорит) = 1 - P(все перегорят) = 1 - {prob_all_burnout} = {right_answer}

Ответ: {right_answer}
"""

# выводы
print(text)
print(right_answer)
print('__________________________')
print(text_of_solve)