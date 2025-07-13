import random

# Генерируем вероятность попадания (увеличиваем диапазон)
prob_hit = random.randint(75, 90)  # 0.75 - 0.90 (более высокие значения)
fl_prob_hit = float(f'0.{prob_hit}')

# Генерируем случайную последовательность попаданий и промахов (5 выстрелов)
# Ограничиваем количество промахов, чтобы вероятность не была слишком маленькой
hits_count = random.randint(2, 4)  # минимум 2 попадания
misses_count = 5 - hits_count

# Создаем список с нужным количеством попаданий и промахов
shots = ['попал'] * hits_count + ['промахнулся'] * misses_count
# Перемешиваем порядок
random.shuffle(shots)

# Создаем описание последовательности
sequence_description = []
for i, shot in enumerate(shots, 1):
    if shot == 'попал':
        sequence_description.append(f"{i}-й раз попал")
    else:
        sequence_description.append(f"{i}-й раз промахнулся")

sequence_text = ", ".join(sequence_description)

# Вычисляем вероятность
prob_miss = round(1 - fl_prob_hit, 2)
probability = 1.0

for shot in shots:
    if shot == 'попал':
        probability *= fl_prob_hit
    else:
        probability *= prob_miss

right_answer = round(probability, 2)

# Проверяем, что результат не равен 0.00
if right_answer == 0.0:
    # Если результат 0.00, пересчитываем с другими параметрами
    prob_hit = random.randint(80, 95)  # еще более высокие значения
    fl_prob_hit = float(f'0.{prob_hit}')
    prob_miss = round(1 - fl_prob_hit, 2)

    # Увеличиваем количество попаданий
    hits_count = random.randint(3, 4)
    misses_count = 5 - hits_count

    shots = ['попал'] * hits_count + ['промахнулся'] * misses_count
    random.shuffle(shots)

    # Пересчитываем описание и вероятность
    sequence_description = []
    for i, shot in enumerate(shots, 1):
        if shot == 'попал':
            sequence_description.append(f"{i}-й раз попал")
        else:
            sequence_description.append(f"{i}-й раз промахнулся")

    sequence_text = ", ".join(sequence_description)

    probability = 1.0
    for shot in shots:
        if shot == 'попал':
            probability *= fl_prob_hit
        else:
            probability *= prob_miss

    right_answer = round(probability, 2)

text = f"""
Биатлонист пять раз стреляет по мишеням. Вероятность попадания в мишень при одном выстреле равна {fl_prob_hit}. 
Найдите вероятность того, что биатлонист {sequence_text}. 
Результат округлите до сотых.
"""

text_of_solve = f"""
Обозначим:
p = {fl_prob_hit} — вероятность попадания в мишень
q = {prob_miss} — вероятность промаха (q = 1 - p)

Последовательность выстрелов: {sequence_text}

Для каждого выстрела:
"""

# Добавляем пошаговое объяснение
for i, shot in enumerate(shots, 1):
    if shot == 'попал':
        text_of_solve += f"{i}-й выстрел: попал с вероятностью {fl_prob_hit}\n"
    else:
        text_of_solve += f"{i}-й выстрел: промахнулся с вероятностью {prob_miss}\n"

text_of_solve += f"""
Поскольку выстрелы независимы, вероятность всей последовательности равна произведению вероятностей:
P = {fl_prob_hit if shots[0] == 'попал' else prob_miss}"""

for shot in shots[1:]:
    if shot == 'попал':
        text_of_solve += f" × {fl_prob_hit}"
    else:
        text_of_solve += f" × {prob_miss}"

text_of_solve += f" = {right_answer}"

text_of_solve += f"""

Ответ: {right_answer}
"""

# выводы
print(text)
print(right_answer)
print('__________________________')
print(text_of_solve)