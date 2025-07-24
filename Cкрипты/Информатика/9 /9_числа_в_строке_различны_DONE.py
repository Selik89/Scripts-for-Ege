import random
from openpyxl import Workbook

first_condition_str = f'- в строке все числа различны'


# work with second condition
second_conditions = [
'- сумма наибольшего и наименьшего чисел меньше суммы четырёх других',
'- удвоенная сумма наибольшего и наименьшего чисел больше суммы четырёх других',
'- количество чётных чисел превышает количество нечётных чисел',
'- количество чётных чисел не превышает количество нечётных чисел'
]

second_condition = random.choice(second_conditions)

text = f"""
Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел. 
Определите количество строк таблицы, для чисел которых выполнены оба условия:
{first_condition_str}
{second_condition}.
В ответе запишите только число.
""".strip()

count_of_right_strings = 0

tf_main = random.randint(1, 3)

# generator
wb = Workbook()
ws = wb.active

for _ in range(5000):
    if tf_main == 1:
        tf = random.choice([True, False, False, False])
    elif tf_main == 2:
        tf = random.choice([True, False, False])
    else:
        tf = random.choice([True, True, False, False, False, False, False])

    while True:
        if tf:
            array = []
            for _ in range(6):
                while True:
                    num = random.randint(10, 99)
                    if num not in array:
                        break
                array.append(num)
            random.shuffle(array)

            if second_condition == '- сумма наибольшего и наименьшего чисел меньше суммы четырёх других' and max(
                    array) + min(array) < sum(array) - max(array) - min(array):
                check = True
            elif second_condition == '- удвоенная сумма наибольшего и наименьшего чисел больше суммы четырёх других' and 2 * (
                    max(array) + min(array)) > sum(array) - max(array) - min(array):
                check = True
            elif second_condition == '- количество чётных чисел превышает количество нечётных чисел' and len(
                    [x for x in array if x % 2 == 0]) > len([x for x in array if x % 2 != 0]):
                check = True
            elif second_condition == '- количество чётных чисел не превышает количество нечётных чисел' and len(
                    [x for x in array if x % 2 == 0]) <= len([x for x in array if x % 2 != 0]):
                check = True
            else:
                check = False

            if check:
                count_of_right_strings += 1
                ws.append(array)
                
                break
        else:
            repeat_num = random.randint(10, 99)
            r = random.randint(1, 5)
            array = [repeat_num] * r
            for _ in range(6 - r):
                while True:
                    num = random.randint(10, 99)
                    if num not in array:
                        break
                array.append(num)
            random.shuffle(array)

            ws.append(array)
            break

wb.save('9.xlsx')

print(text)
print(f'right answer = {count_of_right_strings}')
