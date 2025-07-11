import random

broken_battery = round(float(f"0.0{random.randint(1, 9)}"), 2)
reject_broken_battery = round(float(f"0.{random.randint(95, 99)}"), 2)
reject_working_battery = round(float(f"0.0{random.randint(1, 5)}"), 2)

text = f"""
Автоматическая линия изготавливает батарейки. 
Вероятность того, что готовая батарейка неисправна, равна {broken_battery}. 
Перед упаковкой каждая батарейка проходит систему контроля. 
Вероятность того, что система забракует неисправную батарейку, равна {reject_broken_battery}. 
Вероятность того, что система по ошибке забракует исправную батарейку, равна {reject_working_battery}. 
Найдите вероятность того, что случайно выбранная изготовленная батарейка будет забракована системой контроля.
"""

right_answer = round((1 - broken_battery) * reject_working_battery + broken_battery * reject_broken_battery, 4)

text_of_solve = f"""
Обозначим события:
A — батарейка неисправна, P(A) = {broken_battery}
¬A — батарейка исправна, P(¬A) = 1 - {broken_battery} = {1 - broken_battery}
B — батарейка забракована системой контроля

Дано:
P(B|A) = {reject_broken_battery} — вероятность, что система забракует неисправную батарейку
P(B|¬A) = {reject_working_battery} — вероятность, что система по ошибке забракует исправную батарейку

Найти: P(B) — вероятность того, что случайно выбранная батарейка будет забракована системой контроля.

Используем формулу полной вероятности:
P(B) = P(B|A) * P(A) + P(B|¬A) * P(¬A)

Подставим значения:
P(B) = {reject_broken_battery} * {broken_battery} + {reject_working_battery} * {1 - broken_battery} = {round((1 - broken_battery) * reject_working_battery + broken_battery * reject_broken_battery, 4)}

Ответ: {round((1 - broken_battery) * reject_working_battery + broken_battery * reject_broken_battery, 4)}
"""

print(text)
print(f"Answer = {right_answer}")
print('_____________________________')
print(text_of_solve)


