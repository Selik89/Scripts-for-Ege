import random

pairs = [
    (100, 2),   # 0.02
    (100, 4),   # 0.04
    (200, 4),   # 0.02
    (200, 10),  # 0.05
    (250, 5),   # 0.02
    (250, 25),  # 0.10
    (400, 8),   # 0.02
    (400, 20),  # 0.05
    (500, 10),  # 0.02
    (500, 25),  # 0.05
    (500, 50),  # 0.10
    (120, 3),   # 0.025
    (160, 8),   # 0.05
    (320, 16),  # 0.05
    (240, 12),  # 0.05
    (400, 40),  # 0.10
    (200, 25),  # 0.125
    (160, 20),  # 0.125
    (80, 10),   # 0.125
]

bags_count, defective_bags = random.choice(pairs)
good_bags = bags_count - defective_bags

prob_defective = defective_bags / bags_count
prob_not_defective = good_bags / bags_count

text = f"""
Фабрика выпускает {bags_count} сумок, из которых {defective_bags} имеют скрытые дефекты.
Найдите вероятность того, что купленная наугад сумка окажется без дефектов.
"""

text_of_solve = f"""
Обозначим:
P(дефектная) = {defective_bags}/{bags_count} = {prob_defective}
P(без дефектов) = {good_bags}/{bags_count} = {prob_not_defective}

Найти: вероятность того, что купленная сумка окажется без дефектов.

P(без дефектов) = {good_bags}/{bags_count} = {prob_not_defective}

Ответ: {good_bags}/{bags_count} = {prob_not_defective}
"""

print(text)
print(prob_not_defective)
print('__________________________')
print(text_of_solve)