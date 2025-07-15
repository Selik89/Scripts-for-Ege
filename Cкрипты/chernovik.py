def f(s, n):
    if s <= 74 and (n == 5 or n == 3):
        return 1
    elif s > 74 and n == 5:
        return 0
    elif s <= 74 and n < 5:
        return 0
    else:
        if n % 2 == 0:
            return f(s - 3, n + 1) or f(s - 6, n + 1) or f(s // 2, n + 1)
        else:
            return f(s - 3, n + 1) and f(s - 6, n + 1) and f(s // 2, n + 1)

results = []
for s in range(75, 2000):
    if f(s, 1):
        results.append(s)

print(results)