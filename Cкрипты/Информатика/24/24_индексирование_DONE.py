import random

count_of_find = random.randrange(80, 120, 10)

count_of_figure = random.randrange(1, 4)
find_str = ''.join(random.choices('QWERTYUIOPASDFGHJKLZXCVBNM', k = count_of_figure))

conditions = ['максимальное', 'минимальное']
condition = random.choice(conditions)

if count_of_figure > 1:
    extra_string = ' (в указанном порядке)'
else:
    extra_string = ''.strip()

text = f"""
Текстовый файл состоит из заглавных букв латинского алфавита.
Определите в прилагаемом файле {condition} количество идущих подряд символов, 
среди которых {find_str}{extra_string} встречается ровно {count_of_find} раз.
Для выполнения этого задания следует написать программу.
""".strip()

# generator of file

file = open('24.txt', 'w')
string = ''

for _ in range(100000):
    tf = random.choice([True, True, True, False])
    if tf:
        string += find_str
    else:
        string += ''.join(random.choices('QWERTYUIOPASDFGHJKLZXCVBNM', k = random.randint(10, 100)))

string = find_str + string + find_str
file.write(string)


# solve

# indexes
idx = []
for i in range(len(string)):
    if count_of_figure == 1:
        if string[i] == find_str[0]:
            idx.append(i)
    elif count_of_figure == 2:
        if string[i] == find_str[0] and string[i + 1] == find_str[1]:
            idx.append(i)
    else:
        if string[i] == find_str[0] and string[i + 1] == find_str[1] and string[i + 2] == find_str[2]:
            idx.append(i)

max_len = 0
# max
for i in range(0, len(idx) - (count_of_find + 1)):
    if count_of_figure == 1:
        s = string[idx[i] + 1 : idx[i + count_of_find + 1]]
        max_len = max(max_len, len(s))

    elif count_of_figure == 2:
        s = string[idx[i] + 1 : idx[i + count_of_find + 1] + 1]
        max_len = max(max_len, len(s))

    else:
        s = string[idx[i] + 1: idx[i + count_of_find + 1] + 2]
        max_len = max(max_len, len(s))


# min
min_len = 10**10
for i in range(0, len(idx) - (count_of_find - 1)):
    if count_of_figure == 1:
        s = string[idx[i] : idx[i + count_of_find - 1] + 1]
        min_len = min(min_len, len(s))

    elif count_of_figure == 2:
        s = string[idx[i] : idx[i + count_of_find - 1] + 2]
        min_len = min(min_len, len(s))

    else:
        s = string[idx[i] : idx[i + count_of_find - 1] + 3]
        min_len = min(min_len, len(s))

if condition == conditions[0]:
    right_answer = max_len
else:
    right_answer = min_len

print(text)
print(f'Answer = {right_answer}')




