import random
from openpyxl import Workbook

# take 7 nums for string
# work with first condition
first_conditions = [
    [2, 2], [2, 3], [3, 2]
]
first_condition_int = random.choice(first_conditions)
first_condition_str = f'- в строке есть {first_condition_int[0]} числа, которые повторяются по {first_condition_int[1]} раза, остальные три числа различны;'


# work with second condition
second_conditions = [
'- сумма наибольшего и наименьшего чисел меньше суммы четырёх других',
'- удвоенная сумма наибольшего и наименьшего чисел больше суммы четырёх других',
'- количество чётных чисел превышает количество нечётных чисел',
'- количество чётных чисел не превышает количество нечётных чисел',
'- максимальное из всех повторяющихся чисел строки больше наибольшего из её неповторяющихся чисел',
'- максимальное из всех повторяющихся чисел строки меньше наибольшего из её неповторяющихся чисел',
'- cумма различных повторяющихся чисел меньше суммы неповторяющихся чисел',
'- cумма различных повторяющихся чисел больше суммы неповторяющихся чисел'
]

second_condition = random.choice(second_conditions)

text = f"""
Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел. 
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
            pov = []
            array = []
            for _ in range(first_condition_int[0]):
                while True:
                    repeat_num = random.randint(10, 99)
                    if repeat_num not in pov:
                        pov.append(repeat_num)
                        for _ in range(first_condition_int[1]):
                            array.append(repeat_num)
                        break

            nepov = []

            for _ in range(7 - first_condition_int[1] * first_condition_int[0]):
                while True:
                    num = random.randint(10, 99)
                    if num not in pov:
                        break
                array.append(num)
                nepov.append(num)

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
            elif second_condition == '- максимальное из всех повторяющихся чисел строки больше наибольшего из её неповторяющихся чисел' and max(pov) > max(nepov):
                check = True
            elif second_condition == '- максимальное из всех повторяющихся чисел строки меньше наибольшего из её неповторяющихся чисел' and max(pov) < max(nepov):
                check = True
            elif second_condition == '- cумма различных повторяющихся чисел меньше суммы неповторяющихся чисел' and sum(pov) < sum(nepov):
                check = True
            elif second_condition == '- cумма различных повторяющихся чисел больше суммы неповторяющихся чисел' and sum(pov) > sum(nepov):
                check = True
            else:
                check = False

            if check:
                count_of_right_strings += 1
                ws.append(array)
                break
        else:
            array = []

            repeat_num = random.randint(10, 99)
            array.extend([repeat_num] * random.randint(2, 5))

            while len(array) < 7:
                num = random.randint(10, 99)
                if num != repeat_num and num not in array:
                    array.append(num)

            random.shuffle(array)

            ws.append(array)
            break

wb.save('9.xlsx')

print(text)
print(f'right answer = {count_of_right_strings}')
