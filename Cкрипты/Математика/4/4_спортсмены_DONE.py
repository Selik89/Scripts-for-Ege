import random

# Возможные суммы (делители 100000, только 2 и/или 5 в разложении, не слишком большие)
possible_totals = [20, 40, 50, 80, 100, 200]

# 1. Выбираем сумму
total = random.choice(possible_totals)

# 2. Генерируем разбиение на 4 положительных целых (каждое >= 2)
def random_partition(n, k, min_value=2):
    assert n >= k * min_value
    n -= k * min_value
    cuts = sorted(random.sample(range(n + k), k - 1))
    parts = []
    last = 0
    for cut in cuts:
        parts.append(cut - last)
        last = cut
    parts.append(n + k - last)
    return [x + min_value for x in parts]

# 3. Назначаем страны
countries_list = ['Финляндии', 'Дании', 'Швеции', 'Норвегии']
random.shuffle(countries_list)
parts = random_partition(total, 4, min_value=2)
countries = dict(zip(countries_list, parts))

# 4. Случайно выбираем страну, для которой ищем вероятность
target_country = random.choice(countries_list)
target_count = countries[target_country]

text = f"""
В соревнованиях по толканию ядра участвуют {countries['Финляндии']} спортсмена из Финляндии, {countries['Дании']} спортсменов из Дании, {countries['Швеции']} спортсменов из Швеции и {countries['Норвегии']} из Норвегии.
Порядок, в котором выступают спортсмены, определяется жребием.
Найдите вероятность того, что спортсмен, который выступает последним, окажется из {target_country}.
"""

prob = target_count / total

text_of_solve = f"""
Всего спортсменов: {total}
Из {target_country}: {target_count}

Порядок определяется жребием, значит, каждый спортсмен с равной вероятностью может оказаться последним.

Вероятность того, что последним выступит спортсмен из {target_country}:
P = {target_count}/{total} = {prob}

Ответ: {prob}
"""

print(text)
print(prob)
print('__________________________')
print(text_of_solve)