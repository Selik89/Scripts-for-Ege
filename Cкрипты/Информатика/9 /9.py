import random

patterns  = {
'удвоенная сумма минимального и максимального чисел строки равна утроенной сумме четырёх её оставшихся чисел' : '2 * (min(array) + max(array)) ==  3 * (sum(array) - max(array) - min(array))',
'сумма двух наибольших чисел строки не больше суммы четырёх её оставшихся чисел' : 'sorted(array, reverse = True)[0] + sorted(array, reverse = True)[1] <= sum(array) - sorted(array, reverse = True)[0] - sorted(array, reverse = True)[1]',
'сумма двух наибольших чисел строки не меньше суммы четырёх её оставшихся чисел' : 'sorted(array, reverse = True)[0] + sorted(array, reverse = True)[1] >= sum(array) - sorted(array, reverse = True)[0] - sorted(array, reverse = True)[1]',
'сумма наибольшего и наименьшего чисел меньше суммы четырёх других' : 'max(array) + min(array) < sum(array) - min(array) - max(array)',
'сумма наибольшего и наименьшего чисел больше суммы четырёх других' : 'max(array) + min(array) > sum(array) - min(array) - max(array)',
'количество чётных чисел превышает количество нечётных чисел' : "len([x for x in array if x % 2 == 0]) > len([x for x in array if x % 2 != 0])",
'количество чётных чисел не превышает количество нечётных чисел' : "len([x for x in array if x % 2 == 0]) <= len([x for x in array if x % 2 != 0])"

}

first_conditions = [x for x in open('1 условие.txt')]
first_condition = random.choice(first_conditions)

if first_condition == first_conditions[-1]:
    second_condition = random.choice([x for x in open('2 условие для строк без повторений.txt')])
elif 'одно' in first_conditions:
    second_condition = random.choice([x for x in open('2 условие для одного повторяющегося числа.txt')])




