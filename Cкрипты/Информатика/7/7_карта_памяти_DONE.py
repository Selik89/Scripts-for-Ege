import random

# функция для подсчёта правильного ответа
def count_of_photos_on_the_last_card(
        x, y, i, card_size, photos_cnt
):
    image = x * y * i
    cnt_of_pic_on_card =  card_size * 8 * 1024 * 1024 * 1024 // image
    result = photos_cnt % cnt_of_pic_on_card
    return result


# -- подбор размера

sizes = ['1280', '1920', '1080', '1440', '2560', '3840', '2160', '4320', '7680']

x = int(random.choice(sizes))
y = int(random.choice(sizes))
size = f'{max(int(x), int(y))}x{min(int(x), int(y))}'

# -- палитра цветов

colors = random.randint(65, 5000)

# -- количество снимков

count_of_photos = random.randint(3000, 5000)

# -- посчитаем весь объём снимков

i = 0
while 2 ** i < colors:
    i += 1

full_size = i * int(x) * int(y) * count_of_photos / 1024 / 1024 / 1024 / 8


# -- размер карты
card_size = random.randint(3, int(full_size) // 2 + 1)

# -- текст
text = f"""  
Фотограф делает цветные фотографии размером {size} пикселей, используя палитру из {colors} цветов. 
Для сохранения снимков фотограф использует сменные карты памяти, каждая из которых вмещает не более {card_size} Гбайт данных. 
Когда на карте памяти остаётся недостаточно места для записи новой фотографии, фотограф берёт следующую, свободную карту. 
Известно, что фотограф сделал {count_of_photos} снимков. 
Сколько снимков оказалось на последней карте памяти из использованных? 
В ответе запишите целое число.
"""

text_of_solve = f"""
Решение:
1. Для палитры из {colors} цветов требуется {i} бит на пиксель.
2. Размер одной фотографии: {x} × {y} × {i} бит = {x * y * i} бит.
3. Переведём размер одной фотографии в байты: {x * y * i} // 8 = {x * y * i // 8} байт.
4. Размер карты памяти: {card_size} × 1024^3 = {card_size * 1024 ** 3} байт.
5. Количество фотографий на одной карте: {card_size * 1024 ** 3} // {x * y * i // 8} = {(card_size * 1024 ** 3) // (x * y * i // 8)}.
6. Количество снимков на последней карте: {count_of_photos} % {(card_size * 1024 ** 3) // (x * y * i // 8)} = {count_of_photos % ((card_size * 1024 ** 3) // (x * y * i // 8)) if count_of_photos % ((card_size * 1024 ** 3) // (x * y * i // 8)) != 0 else (card_size * 1024 ** 3) // (x * y * i // 8)}.
"""


right_answer = count_of_photos_on_the_last_card(int(x), int(y), i, card_size, count_of_photos)



# выводы
print(text)

print(f'Answer = {right_answer}')
print('_______________________________')
print(text_of_solve)


