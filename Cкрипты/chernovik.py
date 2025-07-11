def solve_task(x, y):
    if x == 9:
        return 0  # Если попали в запрещённое число — путь не подходит
    elif x == y:
        return 1  # Если дошли до нужного числа — это один из подходящих путей
    elif x > y:
        return 0  # Если превысили целевое число — путь не подходит
    else:
        return solve_task(x + 4, y) + solve_task(x + 3, y) + solve_task(x * 4, y)


print(solve_task(8, 15) * solve_task(15, 32))