f = open('vars-.txt')

array = [int(x) for x in f]
first_add = array[0]
second_add = array[1]
multiply = array[2]
win_count = array[3]
array_of_19 = array[4:]
set_of_19 = array_of_19

text = f"""
Для игры, описанной в задании 19, найдите минимальное значение S, при котором одновременно выполняются два условия:
- у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
- у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
"""

def solve_for_all(s, y, n, f_add, s_add, multi):
    if s <= y and (n == 5 or n == 3):
        return 1
    elif s > y and n == 5:
        return 0
    elif s <= y and n < 5:
        return 0
    else:
        if n % 2 == 0:
            return solve_for_all(s - f_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s - s_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s // multi, y, n + 1, f_add, s_add, multi)
        else:
            return solve_for_all(s - f_add, y, n + 1, f_add, s_add, multi) and solve_for_all(s - s_add, y, n + 1, f_add, s_add, multi) and solve_for_all(s // multi, y, n + 1, f_add, s_add, multi)

results_of_func = []
for s in range(win_count + 1, 2000):
    if solve_for_all(s, win_count, 1, first_add, second_add, multiply):
        results_of_func.append(s)

i = 0
while results_of_func[i] in set_of_19:
    i += 1

result = results_of_func[i]

text_of_solve = f"""
def f(s, n):
    if s <= {win_count} and (n == 5 or n == 3):
        return 1
    elif s > {win_count} and n == 5:
        return 0
    elif s <= {win_count} and n < 5:
        return 0
    else:
        if n % 2 == 0:
            return f(s - {first_add}, n + 1) or f(s - {second_add}, n + 1) or f(s // {multiply}, n + 1)
        else:
            return f(s - {first_add}, n + 1) and f(s - {second_add}, n + 1) and f(s // {multiply}, n + 1)

results = []
for s in range({win_count + 1}, 2000):
    if f(s, 1):
        results.append(s)

print(results)

(Обязательно проверить, что результат не совпадает с числами которые получаются в 19 задании)
"""

print(text)
print(f"answer = {result}")
print('_______________________________________')
print(text_of_solve)


