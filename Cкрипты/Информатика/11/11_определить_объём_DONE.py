import random
from math import ceil


def solve(symb, alph, id):
    i = 0
    while 2 ** i < alph:
        i += 1
    right_answer = ceil(i * symb / 8) * count_of_identifier // 1024

    return right_answer


while True:
    count_of_symbols = random.randint(20, 100)
    alphabet = random.randint(10, 8192 - 1)
    count_of_identifier = random.randint(10000, 100000)
    i = 0
    while 2 ** i < alphabet:
        i += 1
    if ceil(i * count_of_symbols / 8) * count_of_identifier % 1024 == 0:
        break



# для строк
if 2 ** i == alphabet:
    string = f'2^{i} == {2**i}'
else:
    string = f"""
2^{i - 1} = {2**i} < {alphabet}
2^{i}= {2 ** i} > {alphabet}
""".strip()

text = f"""
При регистрации в компьютерной системе каждому объекту присваивается идентификатор, 
состоящий из {count_of_symbols} символов и содержащий только десятичные цифры и символы из {alphabet}-символьного специального алфавита.
В базе данных для хранения каждого идентификатора отведено одинаковое и минимально возможное целое число байт. 
При этом используется посимвольное кодирование идентификаторов, все символы кодируются одинаковым и минимально возможным количеством бит.
Определите объём памяти (в Кбайт), необходимый для хранения {count_of_identifier} идентификаторов.
В ответе запишите только целое число – количество Кбайт.
"""

text_of_solve = f"""
1. Определение минимального количества бит для кодирования символа
Для кодирования {alphabet} различных символов нужно найти минимальную степень двойки, которая больше или равна {alphabet}:
{string}
Следовательно, для кодирования одного символа требуется {i} бит.

2. Расчет размера одного идентификатора
Количество символов в идентификаторе: {count_of_symbols}
Размер в битах: {count_of_symbols} × {i} = {count_of_symbols * i} бит
Размер в байтах: {count_of_symbols * i} ÷ 8 = {count_of_symbols * i / 8} байт
Поскольку в базе данных отводится целое число байт, округляем вверх: {ceil(count_of_symbols * i / 8)} байт

3. Расчет общего объема памяти
Количество идентификаторов: {count_of_identifier}
Общий объем в байтах: {count_of_identifier} × {ceil(count_of_symbols * i / 8)} = {count_of_identifier * ceil(count_of_symbols * i / 8)} байт
Общий объем в килобайтах: {count_of_identifier * ceil(count_of_symbols * i / 8)} ÷ 1024 = {count_of_identifier * ceil(count_of_symbols * i / 8) //1024} Кбайт
Для хранения {count_of_identifier} идентификаторов потребуется  {count_of_identifier * ceil(count_of_symbols * i / 8) //1024} Кбайт памяти.
"""

print(text)
print(f'Answer = {solve(count_of_symbols, alphabet,count_of_identifier)}')
print('____________________________')
print(text_of_solve)
