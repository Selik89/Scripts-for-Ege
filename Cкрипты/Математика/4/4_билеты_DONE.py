import random
import math


possible_totals = [10, 20, 40, 50, 80, 100, 200]

def has_only_2_5(n):
    if n == 1:
        return True
    for p in [2, 5]:
        while n % p == 0 and n > 1:
            n //= p
    return n == 1

while True:
    total = random.choice(possible_totals)
    possible_wars = []
    for war in range(1, total):
        g = math.gcd(war, total)
        denom = total // g
        if has_only_2_5(denom):
            possible_wars.append(war)
    if possible_wars:
        war = random.choice(possible_wars)
        break

text = f"""
В сборнике билетов по истории всего {total} билетов, в {war} из них встречается вопрос о Великой Отечественной войне.
Найдите вероятность того, что в случайно выбранном на экзамене билете школьнику достанется вопрос о Великой Отечественной войне.
"""

prob = war / total

text_of_solve = f"""
Всего билетов: {total}
Билетов с вопросом о Великой Отечественной войне: {war}

Вероятность того, что школьнику достанется такой билет:
P = {war}/{total} = {prob}

Ответ: {prob}
"""

print(text)
print(prob)
print('__________________________')
print(text_of_solve)