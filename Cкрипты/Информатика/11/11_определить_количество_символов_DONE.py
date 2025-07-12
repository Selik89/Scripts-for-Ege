import random
from math import ceil


def solve(alphabet, count_of_identifier, memory_mb):
    # Находим минимальное количество бит для кодирования символа
    i = 0
    while 2 ** i < alphabet:
        i += 1

    # Переводим память в байты
    memory_bytes = memory_mb * 1024 * 1024

    # Находим минимальную длину серийного номера
    min_symbols = ceil((memory_bytes / count_of_identifier) * 8 / i)

    return min_symbols


def generate_task():
    while True:
        # Генерируем случайные параметры
        special_alphabet = random.randint(10, 100)  # размер специального алфавита
        alphabet = 10 + special_alphabet  # общее количество символов
        count_of_identifier = random.randint(1000000, 10000000)  # количество идентификаторов
        memory_mb = random.randint(20, 100)  # объем памяти в Мбайт

        # Находим минимальное количество бит для кодирования символа
        i = 0
        while 2 ** i < alphabet:
            i += 1

        # Проверяем, что задача имеет решение
        memory_bytes = memory_mb * 1024 * 1024
        min_symbols = ceil((memory_bytes / count_of_identifier) * 8 / i)

        # Убеждаемся, что минимальная длина разумная (не слишком маленькая и не слишком большая)
        if 5 <= min_symbols <= 100:
            break

    return special_alphabet, count_of_identifier, memory_mb, min_symbols


# Генерируем задачу
special_alphabet, count_of_identifier, memory_mb, min_symbols = generate_task()
alphabet = 10 + special_alphabet

# Находим минимальное количество бит для кодирования символа
i = 0
while 2 ** i < alphabet:
    i += 1

# Для строк
if 2 ** i == alphabet:
    string = f'2^{i} == {2 ** i}'
else:
    string = f"""
2^{i - 1} = {2 ** (i - 1)} < {alphabet}
2^{i} = {2 ** i} > {alphabet}
""".strip()

text = f"""
На предприятии каждой изготовленной детали присваивают серийный номер, 
содержащий десятичные цифры и символы из {special_alphabet}-символьного специального алфавита. 
В базе данных каждый серийный номер занимает одинаковое и минимально возможное число байт. 
При этом используется посимвольное кодирование серийных номеров, все символы кодируются одинаковым и минимально возможным числом бит. 
Известно, что для хранения {count_of_identifier} серийных номеров требуется более {memory_mb} Мбайт памяти. 
Определите минимально возможную длину серийного номера.
"""

text_of_solve = f"""
1. Определение минимального количества бит для кодирования символа
Общее количество различных символов: 10 (цифры) + {special_alphabet} (специальный алфавит) = {alphabet} символов
Для кодирования {alphabet} различных символов нужно найти минимальную степень двойки, которая больше или равна {alphabet}:
{string}
Следовательно, для кодирования одного символа требуется {i} бит.

2. Анализ условия задачи
Известно, что для хранения {count_of_identifier:,} серийных номеров требуется более {memory_mb} Мбайт памяти.
{memory_mb} Мбайт = {memory_mb} × 1024 × 1024 = {memory_mb * 1024 * 1024:,} байт

3. Расчет минимальной длины серийного номера
Пусть x - длина серийного номера в символах.
Размер одного серийного номера в битах: x × {i} = {i}x бит
Размер в байтах: {i}x ÷ 8 = {i}x/8 байт
Поскольку отводится целое число байт, размер равен ceil({i}x/8) байт

Общий объем памяти: {count_of_identifier:,} × ceil({i}x/8) байт
По условию: {count_of_identifier:,} × ceil({i}x/8) > {memory_mb * 1024 * 1024:,}

Находим минимальное x:
ceil({i}x/8) > {memory_mb * 1024 * 1024:,} ÷ {count_of_identifier:,}
ceil({i}x/8) > {memory_mb * 1024 * 1024 / count_of_identifier:.2f}
{i}x/8 > {memory_mb * 1024 * 1024 / count_of_identifier:.2f}
x > {memory_mb * 1024 * 1024 / count_of_identifier * 8 / i:.2f}
x > {memory_mb * 1024 * 1024 / count_of_identifier * 8 / i:.2f}

Поскольку x должно быть целым числом, минимальная длина серийного номера равна {min_symbols} символов.

4. Проверка
При длине {min_symbols} символов:
Размер одного номера: {ceil(min_symbols * i / 8)} байт
Общий объем: {count_of_identifier} × {ceil(min_symbols * i / 8)} = {count_of_identifier * ceil(min_symbols * i / 8):,} байт = {count_of_identifier * ceil(min_symbols * i / 8) / (1024 * 1024):.2f} Мбайт > {memory_mb} Мбайт

Ответ: минимально возможная длина серийного номера равна {min_symbols} символов.
"""

print(text)
print(f'Answer = {solve(alphabet, count_of_identifier, memory_mb)}')
print('____________________________')
print(text_of_solve)