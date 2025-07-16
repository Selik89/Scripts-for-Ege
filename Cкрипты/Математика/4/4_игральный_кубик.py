import random

# Количество костей
dice_count = 2
# Случайная сумма, которую ищем (от 2 до 12)
target_sum = random.randint(2, 12)

# Всего возможных исходов (6 граней на каждой кости)
total_outcomes = 6 ** dice_count

# Считаем количество благоприятных исходов для суммы target_sum
favorable = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == target_sum:
            favorable += 1

prob = favorable / total_outcomes

text = f"""
В случайном эксперименте бросают две игральные кости.
Найдите вероятность того, что в сумме выпадет {target_sum} очков.
Результат округлите до сотых.
"""

text_of_solve = f"""
Всего возможных исходов: {total_outcomes}
Благоприятных исходов (сумма {target_sum}): {favorable}

Вероятность:
P = {favorable}/{total_outcomes} = {prob}

Ответ (округлённо до сотых): {prob:.2f}
"""

print(text)
print(prob)
print('__________________________')
print(text_of_solve)