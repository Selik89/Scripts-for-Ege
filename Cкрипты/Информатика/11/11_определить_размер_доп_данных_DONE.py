import random
from math import ceil


def solve(symbols, special_alphabet, count_of_identifier, memory_kb, condition_type):
    # Общее количество символов в алфавите
    total_alphabet = 10 + 26 + 26 + special_alphabet  # цифры + строчные + заглавные + специальные

    # Находим минимальное количество бит для кодирования символа
    i = 0
    while 2 ** i < total_alphabet:
        i += 1

    # Размер серийного номера в байтах
    serial_number_bytes = ceil(symbols * i / 8)

    # Общий объем памяти в байтах
    total_memory_bytes = memory_kb * 1024

    if condition_type == "не более":
        # Общий объем = количество_деталей × (размер_номера + дополнительные_сведения)
        # total_memory_bytes >= count_of_identifier × (serial_number_bytes + additional_bytes)
        # additional_bytes <= (total_memory_bytes / count_of_identifier) - serial_number_bytes
        max_additional_bytes = int((total_memory_bytes / count_of_identifier) - serial_number_bytes)
    else:  # "не менее"
        # total_memory_bytes <= count_of_identifier × (serial_number_bytes + additional_bytes)
        # additional_bytes >= (total_memory_bytes / count_of_identifier) - serial_number_bytes
        max_additional_bytes = ceil((total_memory_bytes / count_of_identifier) - serial_number_bytes)

    return max_additional_bytes


def generate_task():
    while True:
        # Генерируем случайные параметры
        symbols = random.randint(10, 50)  # количество символов в номере
        special_alphabet = random.randint(100, 1000)  # размер специального алфавита
        count_of_identifier = random.randint(500, 5000)  # количество деталей
        memory_kb = random.randint(50, 200)  # объем памяти в Кбайт
        condition_type = random.choice(["не более", "не менее"])

        # Общее количество символов в алфавите
        total_alphabet = 10 + 26 + 26 + special_alphabet

        # Находим минимальное количество бит для кодирования символа
        i = 0
        while 2 ** i < total_alphabet:
            i += 1

        # Размер серийного номера в байтах
        serial_number_bytes = ceil(symbols * i / 8)

        # Общий объем памяти в байтах
        total_memory_bytes = memory_kb * 1024

        # Проверяем корректность задачи
        if condition_type == "не более":
            max_additional_bytes = int((total_memory_bytes / count_of_identifier) - serial_number_bytes)
        else:
            max_additional_bytes = ceil((total_memory_bytes / count_of_identifier) - serial_number_bytes)

        # Убеждаемся, что результат разумный
        if 1 <= max_additional_bytes <= 100:
            break

    return symbols, special_alphabet, count_of_identifier, memory_kb, condition_type


# Генерируем задачу
symbols, special_alphabet, count_of_identifier, memory_kb, condition_type = generate_task()

# Общее количество символов в алфавите
total_alphabet = 10 + 26 + 26 + special_alphabet

# Находим минимальное количество бит для кодирования символа
i = 0
while 2 ** i < total_alphabet:
    i += 1

# Размер серийного номера в байтах
serial_number_bytes = ceil(symbols * i / 8)

# Общий объем памяти в байтах
total_memory_bytes = memory_kb * 1024

# Находим максимальное количество байт для дополнительных сведений
if condition_type == "не более":
    max_additional_bytes = int((total_memory_bytes / count_of_identifier) - serial_number_bytes)
else:
    max_additional_bytes = ceil((total_memory_bytes / count_of_identifier) - serial_number_bytes)

# Для строк
if 2 ** i == total_alphabet:
    string = f'2^{i} == {2 ** i}'
else:
    string = f"""
2^{i - 1} = {2 ** (i - 1)} < {total_alphabet}
2^{i} = {2 ** i} > {total_alphabet}
""".strip()

text = f"""
На предприятии каждой изготовленной детали присваивают серийный номер, 
состоящий из {symbols} символов и содержащий только десятичные цифры, 
строчные и заглавные латинские буквы и символы из {special_alphabet}-символьного специального алфавита. 
В базе данных для хранения данных о каждом серийном номере отведено одинаковое и минимально возможное число байт. 
При этом используется посимвольное кодирование серийных номеров, все символы кодируются одинаковым и минимально возможным числом бит. 
Кроме серийного номера, для каждой детали в системе хранятся дополнительные сведения, для чего выделено целое число байт. 
Известно, что для хранения сведений о {count_of_identifier} деталях отведено {condition_type} {memory_kb} Кбайт памяти. 
Какое наибольшее количество байт выделено для хранения дополнительных сведений об одной детали? 
В ответе запишите только целое число – количество байт.
"""

text_of_solve = f"""
1. Определение минимального количества бит для кодирования символа
Общее количество различных символов: 10 (цифры) + 26 (строчные буквы) + 26 (заглавные буквы) + {special_alphabet} (специальный алфавит) = {total_alphabet} символов
Для кодирования {total_alphabet} различных символов нужно найти минимальную степень двойки, которая больше или равна {total_alphabet}:
{string}
Следовательно, для кодирования одного символа требуется {i} бит.

2. Расчет размера серийного номера
Количество символов в номере: {symbols}
Размер в битах: {symbols} × {i} = {symbols * i} бит
Размер в байтах: {symbols * i} ÷ 8 = {symbols * i / 8} байт
Поскольку отводится целое число байт, размер равен ceil({symbols * i / 8}) = {serial_number_bytes} байт

3. Анализ условия задачи
Известно, что для хранения сведений о {count_of_identifier} деталях отведено {condition_type} {memory_kb} Кбайт памяти.
{memory_kb} Кбайт = {memory_kb} × 1024 = {total_memory_bytes} байт

4. Расчет максимального количества байт для дополнительных сведений
Пусть x - количество байт для дополнительных сведений об одной детали.
Общий объем памяти: {count_of_identifier} × ({serial_number_bytes} + x) байт

По условию: {count_of_identifier} × ({serial_number_bytes} + x) {condition_type} {total_memory_bytes}
"""

if condition_type == "не более":
    text_of_solve += f"""
{count_of_identifier} × ({serial_number_bytes} + x) ≤ {total_memory_bytes}
{serial_number_bytes} + x ≤ {total_memory_bytes} ÷ {count_of_identifier}
{serial_number_bytes} + x ≤ {total_memory_bytes / count_of_identifier:.2f}
x ≤ {total_memory_bytes / count_of_identifier:.2f} - {serial_number_bytes}
x ≤ {total_memory_bytes / count_of_identifier - serial_number_bytes:.2f}

Поскольку x должно быть целым числом, наибольшее количество байт равно {max_additional_bytes}.

5. Проверка
При {max_additional_bytes} байт на дополнительные сведения:
Размер одной записи: {serial_number_bytes} + {max_additional_bytes} = {serial_number_bytes + max_additional_bytes} байт
Общий объем: {count_of_identifier} × {serial_number_bytes + max_additional_bytes} = {count_of_identifier * (serial_number_bytes + max_additional_bytes)} байт = {count_of_identifier * (serial_number_bytes + max_additional_bytes) / 1024:.2f} Кбайт ≤ {memory_kb} Кбайт

Ответ: наибольшее количество байт для дополнительных сведений равно {max_additional_bytes}.
"""
else:
    text_of_solve += f"""
{count_of_identifier} × ({serial_number_bytes} + x) ≥ {total_memory_bytes}
{serial_number_bytes} + x ≥ {total_memory_bytes} ÷ {count_of_identifier}
{serial_number_bytes} + x ≥ {total_memory_bytes / count_of_identifier:.2f}
x ≥ {total_memory_bytes / count_of_identifier:.2f} - {serial_number_bytes}
x ≥ {total_memory_bytes / count_of_identifier - serial_number_bytes:.2f}

Поскольку x должно быть целым числом, наибольшее количество байт равно {max_additional_bytes}.

5. Проверка
При {max_additional_bytes} байт на дополнительные сведения:
Размер одной записи: {serial_number_bytes} + {max_additional_bytes} = {serial_number_bytes + max_additional_bytes} байт
Общий объем: {count_of_identifier} × {serial_number_bytes + max_additional_bytes} = {count_of_identifier * (serial_number_bytes + max_additional_bytes)} байт = {count_of_identifier * (serial_number_bytes + max_additional_bytes) / 1024:.2f} Кбайт ≥ {memory_kb} Кбайт

Ответ: наибольшее количество байт для дополнительных сведений равно {max_additional_bytes}.
"""

print(text)
print(f'Answer = {solve(symbols, special_alphabet, count_of_identifier, memory_kb, condition_type)}')
print('____________________________')
print(text_of_solve)