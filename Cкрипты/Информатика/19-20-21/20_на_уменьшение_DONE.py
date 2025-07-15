f = open('vars-.txt')

array = [int(x) for x in f]
first_add = array[0]
second_add = array[1]
multiply = array[2]
win_count = array[3]
array_of_19 = array[4:]

text = f"""
Для игры, описанной в задании 19, найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
- Петя не может выиграть за один ход;
- Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
"""

def solve_for_all(s, y, n, f_add, s_add, multi):
    if s <= y and n == 4:
        return 1
    elif s > y and n == 4:
        return 0
    elif s <= y and n < 4:
        return 0
    else:
        if n % 2 != 0:
            return solve_for_all(s - f_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s - s_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s // multi, y, n + 1, f_add, s_add, multi)
        else:
            return solve_for_all(s - f_add, y, n + 1, f_add, s_add, multi) and solve_for_all(s - s_add, y, n + 1, f_add, s_add, multi) and solve_for_all(s // multi, y, n + 1, f_add, s_add, multi)

results_of_func = []
for s in range(win_count + 1, 2000):
    if solve_for_all(s, win_count, 1, first_add, second_add, multiply):
        results_of_func.append(s)

result = results_of_func[:2]

text_of_solve = f"""
def f(s, n):
    if s <= {win_count} and n == 4:
        return 1
    elif s > {win_count} and n == 4:
        return 0
    elif s <= {win_count} and n < 4:
        return 0
    else:
        if n % 2 != 0:
            return f(s - {first_add}, n + 1) or f(s - {second_add}, n + 1) or f(s // {multiply}, n + 1)
        else:
            return f(s - {first_add}, n + 1) and f(s - {second_add}, n + 1) and f(s // {multiply}, n + 1)

results = []
for s in range({win_count + 1}, 2000):
    if f(s, 1):
        results.append(s)

print(results[:2])
"""

print(text)
print(f'Answer = {result}')
print('_______________________________________________')
print(text_of_solve)