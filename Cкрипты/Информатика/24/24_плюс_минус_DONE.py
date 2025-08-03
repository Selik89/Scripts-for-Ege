import random
import re

text = f"""
Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения). 
Определите максимальное количество символов в непрерывной последовательности, являющейся корректным арифметическим выражением с целыми неотрицательными числами. 
В этом выражении никакие два знака арифметических операций не стоят рядом, порядок действий определяется по правилам математики. 
В записи чисел отсутствуют незначащие (ведущие) нули.
""".strip()

# генератор файла
file = open('24.txt', 'w')

string = ''

for _ in range(10000):
    tf = random.choice([True, False])
    right_str = ''
    if tf:
        count_of_nums = random.randint(2, 20)
        for _ in range(count_of_nums):
            count_of_figures = random.randint(1, 20)
            while True:
                num = ''.join(random.choices('1234567890', k = count_of_figures))
                if num[0] != '0':
                    break

            sign = random.choice(['+', '*'])

            right_str += num + sign

        string += right_str

    else:
        length = random.randint(200, 300)
        false_str = ''.join(random.choices('00123456789***+++', k = length))
        string += '0' + false_str


file.write(string)


# solve
num = r'([123456789][1234567890]*|0)'
reg = rf'{num}([+*]{num})+'

array_of_result = [x.group() for x in re.finditer(reg, string)]

result = len(sorted(array_of_result, key = len)[-1])


print(text)
print(f'Answer = {result}')



