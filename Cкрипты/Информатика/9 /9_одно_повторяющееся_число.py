import random
from openpyxl import Workbook

# work with first condition
first_conditions = [
    [1, 2], [1, 3], [1, 4]
]
first_condition_int = random.choice(first_conditions)
first_condition_str = f'- в строке есть одно число, которое повторяется {first_condition_int[1]} раза, остальные три числа различны;'


# work with second condition
second_conditions = [
'- сумма наибольшего и наименьшего чисел меньше суммы четырёх других',
'- удвоенная сумма наибольшего и наименьшего чисел больше суммы четырёх других',
'- повторяющееся число строки больше, чем среднее арифметическое её неповторяющихся чисел',
'- повторяющееся число строки меньше, чем среднее арифметическое её неповторяющихся чисел',
'- количество чётных чисел превышает количество нечётных чисел',
'- количество чётных чисел не превышает количество нечётных чисел'
]

second_condition = random.choice(second_conditions)

text = f"""
Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел. 
Определите наибольший номер строки таблицы, для чисел которой выполнены оба условия:

{first_condition_str}
{second_condition}.

В ответе запишите только число.
""".strip()

count_of_right_strings = 0


# generator
wb = Workbook()
ws = wb.active

for _ in range(5000):
    tf = random.choice([True, False, False, False])
    while True:
        if tf:
            repeat_num = random.randint(10, 99)
            array = [repeat_num] * first_condition_int[1]
            for _ in range(6 - first_condition_int[1]):
                while True:
                    num = random.randint(10, 99)
                    if num != repeat_num:
                        break
                array.append(num)
            random.shuffle(array)

            if second_condition == '- сумма наибольшего и наименьшего чисел меньше суммы четырёх других' and max(
                    array) + min(array) < sum(array) - max(array) - min(array):
                check = True
            elif second_condition == '- удвоенная сумма наибольшего и наименьшего чисел больше суммы четырёх других' and 2 * (
                    max(array) + min(array)) < sum(array) - max(array) - min(array):
                check = True
            elif second_condition == '- повторяющееся число строки больше, чем среднее арифметическое её неповторяющихся чисел' and repeat_num > (
                    sum(array) - repeat_num * first_condition_int[1]) / (6 - first_condition_int[1]):
                check = True
            elif second_condition == '- повторяющееся число строки меньше, чем среднее арифметическое её неповторяющихся чисел' and repeat_num < (
                    sum(array) - repeat_num * first_condition_int[1]) / (6 - first_condition_int[1]):
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
            array = []
            choice = random.choice([True, False])
            if choice:
                for _ in range(6):
                    while True:
                        num = random.randint(10, 99)
                        if num not in array:
                            array.append(num)
                            break
            else:
                repeat_num = random.randint(10, 99)
                r = first_condition_int[1]
                while r == first_condition_int[1]:
                    r = random.randint(2, 5)
                array = [repeat_num] * r
                for _ in range(6 - r):
                    while True:
                        num = random.randint(0, 99)
                        if num not in array:
                            break
                    array.append(num)
                random.shuffle(array)

            ws.append(array)
            break

wb.save('9.xlsx')

print(text)
print(f'right answer = {count_of_right_strings}')
