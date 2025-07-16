import random
import math

possible_totals = [1000, 1200, 1500, 1600, 2000, 2500, 3000, 4000, 5000, 10000]

def has_only_2_5(n):

    if n == 1:
        return True
    for p in [2, 5]:
        while n % p == 0 and n > 1:
            n //= p
    return n == 1

while True:
    total = random.choice(possible_totals)

    possible_bads = []
    for bad in range(1, total):
        g = math.gcd(bad, total)
        denom = total // g
        if has_only_2_5(denom):
            possible_bads.append(bad)
    if possible_bads:
        bad = random.choice(possible_bads)
        good = total - bad
        break

text = f"""
При производстве в среднем на каждые {good} исправных насоса приходится {bad} неисправных.
Найдите вероятность того, что случайно выбранный насос окажется неисправным.
"""

prob = bad / total

text_of_solve = f"""
Всего насосов: {total}
Исправных: {good}
Неисправных: {bad}

Вероятность того, что случайно выбранный насос окажется неисправным:
P = {bad}/{total} = {prob}

Ответ: {prob}
"""

print(text)
print(prob)
print('__________________________')
print(text_of_solve)