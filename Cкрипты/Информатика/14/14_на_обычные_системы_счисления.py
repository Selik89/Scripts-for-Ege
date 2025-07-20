from random import *

math_expression_str = f'{randint(11, 50)} * {randint(100, 200)}**{randint(400, 1500)} + {randint(100, 200)} * {randint(11, 50)}**{randint(400, 1500)} - {randint(3, 10)} * {randint(5, 11)}**{randint(11, 20)} + {randint(2000, 500000)}'
math_expression_value = eval(math_expression_str)
system = randint(16, 30)
find = randint(0, 9)

questions = [
    'Определите сумму цифр в записи этого числа.', f'Определите количество цифр {find} в записи этого числа.'
]

question = choice(questions)

text = f"""
Значение арифметического выражения
{math_expression_str}
записали в системе счисления с основанием {system}. {question} 
"""

sum_of_digits = 0
cnt_of_main_digits = 0

while math_expression_value != 0:
    if math_expression_value % system == find:
        cnt_of_main_digits += 1
    sum_of_digits += math_expression_value % system
    math_expression_value //= system

if 'сумму' in text:
    right_answer = sum_of_digits
else:
    right_answer = cnt_of_main_digits

# решения
if 'количество' in text:
    text_of_solve = f"""
n = {math_expression_str}
cnt = 0

while n != 0:
    if n % {system} == {find}:
        cnt += 1
    n //= {system}

print(cnt)
"""
else:
    text_of_solve = f"""
n = {math_expression_str}
cnt = 0

while n != 0:
    summa += n % {system}
    n //= {system}

print(summa)
"""

print(text)
print(f'Answer = {right_answer}')
print('_____________________________________')
print(text_of_solve)