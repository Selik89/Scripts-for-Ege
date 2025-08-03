import random
import re
# исходник 21908 на кегэ

# подбор условий
system = random.randint(13, 25)
extra_condition = random.choice(['чётного', 'нечётного', ''])

alphabet = '0123456789'
alphabet_even = '0123456789'
alphabet_odd = '0123456789'

for s in range(65, 65 + system - 10):
    alphabet += chr(s)
    if s % 2 != 0:
        alphabet_even += chr(s)
    else:
        alphabet_odd += chr(s)

string_of_latins_in_system = ', '.join(alphabet[10:])

# генерация файла

file = open('24.txt', 'w')
string = ''
for i in range(1000):
    tf = random.choice([True, False])
    if tf:
        length = random.randint(100, 500)
        string += ''.join(random.choices(alphabet, k=length))
    else:
        length = random.randint(500, 3000)
        string += ''.join(random.choices('9845QWERTYUIOPLKJHGFDSAZXCVBNM'[system - 10:], k=length))

file.write(string)


# solve
reg_for_ordinary = rf'([{alphabet[1:]}][{alphabet}]*)'
array_for_ordinary = sorted([x.group() for x in re.finditer(reg_for_ordinary, string)], key = len)


reg_for_even = rf'([{alphabet[1:]}][{alphabet}]*[{alphabet_even}])'
array_for_even = sorted([x.group() for x in re.finditer(reg_for_even, string)], key = len)


reg_for_odd = rf'([{alphabet[1:]}][{alphabet}]*[{alphabet_odd}])'
array_for_odd = sorted([x.group() for x in re.finditer(reg_for_odd, string)], key = len)


if extra_condition == 'чётного':
    right_answer = len(array_for_even[-1])
    check = len(array_for_even[-2])
elif extra_condition == 'нечётного':
    right_answer = len(array_for_odd[-1])
    check = len(array_for_odd[-2])
else:
    right_answer = len(array_for_ordinary[-1])
    check = len(array_for_ordinary[-2])


text = f"""
Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита. 
Определите в этом файле последовательность идущих подряд символов, представляющих собой запись максимального {extra_condition} {system}-ричного числа. 
В ответе запишите количество символов (значащих цифр в записи числа) в этой последовательности.
Примечание. Латинские буквы {string_of_latins_in_system} означают цифры из алфавита {system}-ричной системы счисления.
""".strip()

if check == right_answer:
    print('ПЕРЕЗАПУСТИТЬ!')
    print('РЕДКАЯ ОШИБКА')
else:
    print(text)
    print(right_answer)






