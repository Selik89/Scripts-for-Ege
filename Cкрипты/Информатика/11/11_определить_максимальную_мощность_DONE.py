import random
from math import ceil


def solve(symbols, count_of_identifier, memory_mb, find_min=True):
    # Переводим память в байты
    memory_bytes = memory_mb * 1024 * 1024

    # Находим размер одного серийного номера в байтах
    bytes_per_identifier = memory_bytes / count_of_identifier

    # Находим количество бит на символ
    bits_per_symbol = bytes_per_identifier * 8 / symbols

    if find_min:
        # Минимальная мощность: находим минимальную мощность, при которой потребуется ceil(bits_per_symbol) бит
        min_bits = ceil(bits_per_symbol)
        alphabet_power = 2 ** (min_bits - 1) + 1
    else:
        # Максимальная мощность: находим максимальную мощность, при которой объем памяти будет не менее указанного
        max_bits = int(bits_per_symbol)
        alphabet_power = 2 ** max_bits

    return alphabet_power


def generate_task():
    while True:
        # Генерируем случайные параметры
        symbols = random.randint(50, 200)
        count_of_identifier = random.randint(100000, 1000000)
        memory_mb = random.randint(20, 100)
        find_min = random.choice([True, False])

        # Проверяем корректность задачи
        memory_bytes = memory_mb * 1024 * 1024
        bytes_per_identifier = memory_bytes / count_of_identifier
        bits_per_symbol = bytes_per_identifier * 8 / symbols

        if 3 <= bits_per_symbol <= 12:
            break

    return symbols, count_of_identifier, memory_mb, find_min


# Генерируем задачу
symbols, count_of_identifier, memory_mb, find_min = generate_task()

# Находим размер одного серийного номера в байтах
memory_bytes = memory_mb * 1024 * 1024
bytes_per_identifier = memory_bytes / count_of_identifier
bits_per_symbol = bytes_per_identifier * 8 / symbols

# Находим мощность алфавита
if find_min:
    min_bits = ceil(bits_per_symbol)
    alphabet_power = 2 ** (min_bits - 1) + 1
    task_type = "минимально возможную"
else:
    max_bits = int(bits_per_symbol)
    alphabet_power = 2 ** max_bits
    task_type = "максимально возможную"

text = f"""
На предприятии каждой изготовленной детали присваивают серийный номер, состоящий из {symbols} символов. 
В базе данных каждый серийный номер занимает одинаковое и минимально возможное число байт. 
При этом используется посимвольное кодирование серийных номеров, все символы кодируются одинаковым и минимально возможным числом бит. 
Известно, что для хранения {count_of_identifier} серийных номеров потребовалось не менее {memory_mb} Мбайт памяти. 
Определите {task_type} мощность алфавита, используемого для записи серийных номеров. В ответе запишите только целое число.
"""

text_of_solve = f"""
1. Анализ условия задачи
Известно, что для хранения {count_of_identifier} серийных номеров потребовалось не менее {memory_mb} Мбайт памяти.
{memory_mb} Мбайт = {memory_mb} × 1024 × 1024 = {memory_mb * 1024 * 1024} байт

2. Расчет размера одного серийного номера
Размер одного серийного номера в байтах: {memory_mb * 1024 * 1024} ÷ {count_of_identifier} = {bytes_per_identifier} байт
Размер в битах: {bytes_per_identifier} × 8 = {bytes_per_identifier * 8} бит

3. Расчет количества бит на символ
Количество символов в номере: {symbols}
Количество бит на символ: {bytes_per_identifier * 8} ÷ {symbols} = {bits_per_symbol} бит

4. Определение мощности алфавита
"""

if find_min:
    text_of_solve += f"""
Для кодирования символов используется минимально возможное количество бит.
Поскольку на символ приходится {bits_per_symbol} бит, минимальное количество бит равно ceil({bits_per_symbol}) = {min_bits} бит.
Минимальная мощность алфавита: 2^{min_bits - 1} + 1 = {2 ** (min_bits - 1)} + 1 = {alphabet_power}

Проверка: при мощности алфавита {alphabet_power} потребуется {min_bits} бит на символ.
Размер одного номера: {symbols} × {min_bits} = {symbols * min_bits} бит = {symbols * min_bits / 8} байт
Общий объем: {count_of_identifier} × {ceil(symbols * min_bits / 8)} = {count_of_identifier * ceil(symbols * min_bits / 8)} байт = {count_of_identifier * ceil(symbols * min_bits / 8) / (1024 * 1024)} Мбайт ≥ {memory_mb} Мбайт

Ответ: минимально возможная мощность алфавита равна {alphabet_power}.
"""
else:
    text_of_solve += f"""
Для кодирования символов используется минимально возможное количество бит.
Поскольку на символ приходится {bits_per_symbol} бит, максимальное количество бит равно int({bits_per_symbol}) = {max_bits} бит.
Максимальная мощность алфавита: 2^{max_bits} = {alphabet_power}

Проверка: при мощности алфавита {alphabet_power} потребуется {max_bits} бит на символ.
Размер одного номера: {symbols} × {max_bits} = {symbols * max_bits} бит = {symbols * max_bits / 8} байт
Общий объем: {count_of_identifier} × {ceil(symbols * max_bits / 8)} = {count_of_identifier * ceil(symbols * max_bits / 8)} байт = {count_of_identifier * ceil(symbols * max_bits / 8) / (1024 * 1024)} Мбайт ≤ {memory_mb} Мбайт

Ответ: максимально возможная мощность алфавита равна {alphabet_power}.
"""

print(text)
print(f'Answer = {solve(symbols, count_of_identifier, memory_mb, find_min)}')
print('____________________________')
print(text_of_solve)