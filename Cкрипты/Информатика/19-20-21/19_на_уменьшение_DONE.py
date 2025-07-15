import random

def solve_for_all(s, y, n, f_add, s_add, multi):
    if s <= y and n == 3:
        return 1
    elif s > y and n == 3:
        return 0
    elif s <= y and n < 3:
        return 0
    else:
        if n % 2 == 0:
            return solve_for_all(s - f_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s - s_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s // multi, y, n + 1, f_add, s_add, multi)
        else:
            return solve_for_all(s - f_add, y, n + 1, f_add, s_add, multi) and solve_for_all(s - s_add, y, n + 1, f_add, s_add, multi) and solve_for_all(s // multi, y, n + 1, f_add, s_add, multi)


def solve_for_unluck(s, y, n, f_add, s_add, multi):
    if s <= y and n == 3:
        return 1
    elif s > y and n == 3:
        return 0
    elif s <= y and n < 3:
        return 0
    else:
        if n % 2 == 0:
            return solve_for_all(s - f_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s - s_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s // multi, y, n + 1, f_add, s_add, multi)
        else:
            return solve_for_all(s - f_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s - s_add, y, n + 1, f_add, s_add, multi) or solve_for_all(s // multi, y, n + 1, f_add, s_add, multi)


first_add = random.randint(2, 3)
second_add = random.randint(4, 7)
multiply = random.randint(2, 3)
wins_count = random.randint(51, 299)
step_type = random.choice(['любом', 'неудачном'])


v = open('vars-.txt', 'w+')
v.write(str(first_add) + '\n')
v.write(str(second_add) + '\n')
v.write(str(multiply) + '\n')
v.write(str(wins_count) + '\n')

text = f"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может:
- убрать из кучи {first_add} камня;
- убрать из кучи {second_add} камней;
- уменьшить количество камней в куче в {multiply} раза (количество камней, полученное при делении, округляется до меньшего).
Например, из кучи в 20 камней за один ход можно получить кучу из {20 - first_add}, {20 - second_add} или {20 // multiply} камней.
Игра завершается, когда количество камней в куче становится не более {wins_count}. 
Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу из {wins_count} или менее камней. 
В начальный момент в куче было S камней, S ≥ {wins_count + 1}.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Укажите минимальное значение S, при котором Петя не может выиграть за один ход, но при {step_type} ходе Пети Ваня может выиграть своим первым ходом.
""".strip()

results_of_func = []
for s in range(wins_count + 1, 2000):
    if step_type == 'любом':
        if solve_for_all(s, wins_count, 1, first_add, second_add, multiply):
            results_of_func.append(s)
    else:
        if solve_for_unluck(s, wins_count, 1, first_add, second_add, multiply):
            results_of_func.append(s)

answer = results_of_func[0]

for x in results_of_func:
    v.write(str(x) + '\n')

if step_type == 'любом':
    text_of_solve = f"""
def f(s, n):
    if s <= {wins_count} and n == 3:
        return 1
    elif s > {wins_count} and n == 3:
        return 0
    elif s <= {wins_count} and n < 3:
        return 0
    else:
        if n % 2 == 0:
            return f(s - {first_add}, n + 1) or f(s - {second_add}, n + 1) or f(s // {multiply}, n + 1)
        else:
            return f(s - {first_add}, n + 1) and f(s - {second_add}, n + 1) and f(s // {multiply}, n + 1)

results = []
for s in range({wins_count + 1}, 2000):
    if f(s, 1):
        results.append(s)

print(results[0])
"""
else:
    text_of_solve = f"""
def f(s, n):
    if s <= {wins_count} and n == 3:
        return 1
    elif s > {wins_count} and n == 3:
        return 0
    elif s <= {wins_count} and n < 3:
        return 0
    else:
        if n % 2 == 0:
            return f(s - {first_add}, n + 1) or f(s - {second_add}, n + 1) or f(s // {multiply}, n + 1)
        else:
            return f(s - {first_add}, n + 1) or f(s - {second_add}, n + 1) or f(s // {multiply}, n + 1)

results = []
for s in range({wins_count + 1}, 2000):
    if f(s, 1):
        results.append(s)

print(results[0])
"""

print(text)
print(f'Answer = {answer}')
print('_______________________________________')
print(text_of_solve)
