import random

def solve_task(
         x, y, out, coms, cnt_of_com
               ):
    if x == out:
        return 0
    elif x == y:
        return 1
    elif x > y:
        return 0
    else:
        if cnt_of_com == 2:
            return solve_task(eval(str(x) + coms[0]), y, out, coms, cnt_of_com) + solve_task(eval(str(x) + coms[1]), y, out, coms, cnt_of_com)
        elif cnt_of_com == 3:
            return solve_task(eval(str(x) + coms[0]), y, out, coms, cnt_of_com) + solve_task(eval(str(x) + coms[1]), y, out, coms, cnt_of_com) + solve_task(eval(str(x) + coms[2]), y, out, coms, cnt_of_com)





while True:
            # -- Исходное число и результат

    start_num = random.randint(6, 15)
    final_num = random.randint(start_num * 2 + 1, 50)

    # -- возможные команды
    possible_commands = ['Прибавить', 'Умножить на']
    # -- количество команд
    cnt_of_command = random.randint(2, 3)

    # -- распределение команд
    while True:
        commands = []
        for _ in range(cnt_of_command):
            commands.append(random.choice(possible_commands))

        if cnt_of_command == 2 and commands.count(possible_commands[0]) == 1:
            break
        elif cnt_of_command == 3 and final_num / start_num >= 3 and commands.count(possible_commands[1]) != 3:
            break
        elif cnt_of_command == 3 and commands.count(possible_commands[1]) < 2:
            break


    # -- подбор номеров для команд
    numbers_for_plus  = [int(x) for x in range(2, 6)]
    if int(final_num/start_num) + 1 >= 6:
        numbers_for_multiplying = [int(x) for x in range(2, 6)]
    else:
        numbers_for_multiplying = [int(x) for x in range(2, int(final_num/start_num) + 1)]

    numbers = []

    for i in range(len(commands)):
        if commands[i] == possible_commands[0]:
            n = random.choice(numbers_for_plus)
            numbers.append(n)
            commands[i] = commands[i] + f' {n}'
            numbers_for_plus.remove(n)
        elif commands[i] == possible_commands[1]:
            n = random.choice(numbers_for_multiplying)
            numbers.append(n)
            commands[i] = commands[i] + f' {n}'
            numbers_for_multiplying.remove(n)

    # -- строчки для условия

    alphabet = 'ABC'
    string_of_commands = ''
    for i in range(len(commands)):
        string_of_commands += alphabet[i] +'. ' + commands[i] + '\n'

    coms = []
    for s in commands:
        if 'Прибавить' in s:
            s = s.replace('Прибавить', '+')
        else:
            s = s.replace('Умножить на', '*')
        coms.append(s)


    # -- числа "Седержит" и "Не содержит"

    while True:
        in_trajectory = random.randint(start_num + 1, final_num - 1)
        out_trajectory = random.randint(start_num + 1, final_num - 1)
        if in_trajectory != out_trajectory:
            break

    # -- Текст
    text = f"""
Исполнитель преобразует число на экране.
У исполнителя есть {cnt_of_command} команды, которые обозначены латинскими буквами:
{string_of_commands}
Программа для исполнителя - это последовательность команд.
Сколько существует программ, для которых при исходном числе {start_num} результатом является число {final_num}, 
при этом траектория вычислений содержит число {in_trajectory} и не содержит {out_trajectory}?

Траектория вычислений программы - это последовательность результатов выполнения всех команд программы.
"""

    right_answer = solve_task(start_num, in_trajectory, out_trajectory, coms, cnt_of_command) * solve_task(in_trajectory, final_num, out_trajectory, coms, cnt_of_command)

    if right_answer != 0:
        break

print(text)
print("Answer = ", right_answer)





