from random import *


system = randint(60, 200)
condition = choice(
['превышающим', 'не превышающим']
)
num_condition = randint(system - 50, system - 20)

math_expression_str = f'{randint(11, 50)} * {randint(100, 200)} ** {randint(400, 1500)} + {randint(100, 200)} * {randint(11, 50)} ** {randint(400, 1500)} - {randint(3, 10)} * {randint(5, 11)} ** {randint(11, 20)} + {randint(2000, 500000)}'
math_expression_value = eval(math_expression_str)

text = f"""
Определите в {system}-ричной записи числа количество цифр с числовым значением, {condition} {num_condition}:
{math_expression_str}
"""

# решение
result = 0
while math_expression_value != 0:
    if 'не' in condition:
        if math_expression_value % system <= num_condition:
            result += 1
    else:
        if math_expression_value % system > num_condition:
            result += 1
    math_expression_value //= system

if 'не' in condition:
    string_condition = '<='
else:
    string_condition = '>'

text_of_solve = f"""
n = {math_expression_str}
cnt = 0
while n != 0:
    if n % {system} {string_condition} {num_condition}:
        cnt += 1
    n //= system
print(cnt)
"""

print(text)
print(f'Answer = {result}')
print('________________________________')
print(text_of_solve)
