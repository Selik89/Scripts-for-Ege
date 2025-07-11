import random

ends_in_two_vm = random.randint(10, 20)
ends_in_one_vm = random.randint(ends_in_two_vm + 3, 30)

fl_ends_in_two_vm = float(f'0.{ends_in_two_vm}')
fl_ends_in_one_vm = float(f'0.{ends_in_one_vm}')

text = f"""
В торговом центре два одинаковых автомата продают кофе. Обслуживание автоматов происходит по вечерам после закрытия центра. 
Известно, что вероятность события «К вечеру в первом автомате закончится кофе» равна {fl_ends_in_one_vm}. 
Такая же вероятность события «К вечеру во втором автомате закончится кофе». 
Вероятность того, что кофе к вечеру закончится в обоих автоматах, равна {fl_ends_in_two_vm}. 
Найдите вероятность того, что к вечеру кофе останется в обоих автоматах.
"""

right_answer = round(1 - (fl_ends_in_one_vm - fl_ends_in_two_vm) * 2 - fl_ends_in_two_vm, 2)

text_of_solve = f"""

Обозначим события:
A — к вечеру в первом автомате закончится кофе,
B — к вечеру во втором автомате закончится кофе.

Дано:
P(A) = {fl_ends_in_one_vm}
P(B) = {fl_ends_in_one_vm}
P(A ∩ B) = {fl_ends_in_two_vm}

Найти: вероятность того, что к вечеру кофе останется в обоих автоматах.

Событие «кофе останется в обоих автоматах» — это противоположное событие к «хотя бы в одном автомате кофе закончится». 
Вероятность того, что хотя бы в одном автомате кофе закончится:
P(A ∪ B) = P(A) + P(B) – P(A ∩ B) = {fl_ends_in_one_vm} + {fl_ends_in_one_vm} - {fl_ends_in_two_vm} = {round(fl_ends_in_one_vm + fl_ends_in_one_vm - fl_ends_in_two_vm, 2)} 

Тогда вероятность того, что кофе останется в обоих автоматах:
P(¬A ∩ ¬B) = 1 – P(A ∪ B) = 1 – {round(fl_ends_in_one_vm + fl_ends_in_one_vm - fl_ends_in_two_vm, 2)}  = {round(1 - round(fl_ends_in_one_vm + fl_ends_in_one_vm - fl_ends_in_two_vm, 2), 2)}

Ответ: {round(1 - round(fl_ends_in_one_vm + fl_ends_in_one_vm - fl_ends_in_two_vm, 2), 2)}

"""


# выводы
print(text)
print(right_answer)
print('__________________________')
print(text_of_solve)
