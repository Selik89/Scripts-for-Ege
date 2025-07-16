import random
import math


n_flips = random.randint(3, 5)
k_req = random.randint(2, n_flips - 1)


condition = random.choice(['at_least', 'exactly'])

p = 0.5

def binom(n, k):
    return math.comb(n, k)

if condition == 'at_least':
    prob = sum(binom(n_flips, k) * (p ** k) * ((1 - p) ** (n_flips - k)) for k in range(k_req, n_flips + 1))
    cond_text = f"хотя бы {k_req} решк{'а' if k_req == 1 else 'и'}"
    terms = []
    for k in range(k_req, n_flips + 1):
        term = f"C({n_flips},{k})*0.5^{k}*0.5^{n_flips-k} = {binom(n_flips, k)}*{0.5**k}*{0.5**(n_flips-k)} = {binom(n_flips, k) * (0.5**k) * (0.5**(n_flips-k))}"
        terms.append(term)
    terms_str = ' +\n'.join(terms)
    solve_text = f"""
P = сумма по k от {k_req} до {n_flips} C(n, k) * p^k * (1-p)^(n-k)
P = 
{terms_str}
P = {prob}
"""
else:
    prob = binom(n_flips, k_req) * (p ** k_req) * ((1 - p) ** (n_flips - k_req))
    cond_text = f"ровно {k_req} решк{'а' if k_req == 1 else 'и'}"
    solve_text = f"""
P = C({n_flips},{k_req}) * 0.5^{k_req} * 0.5^{n_flips-k_req}
P = {binom(n_flips, k_req)} * {0.5**k_req} * {0.5**(n_flips-k_req)} = {prob}
"""

text = f"""
В случайном эксперименте симметричную монету бросают {n_flips} раз(а).
Найдите вероятность того, что выпадет {cond_text}.
"""

text_of_solve = f"""
Возможные числа решек: {cond_text}

{solve_text}
Ответ: {prob}
"""

print(text)
print(prob)
print('__________________________')
print(text_of_solve)