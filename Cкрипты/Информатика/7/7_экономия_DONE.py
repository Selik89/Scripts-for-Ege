import random

# функция для посчёта результата
def calc_saved_kbytes(
    width_before, height_before, bits_before,
    width_after, height_after, bits_after,
    num_photos
):
    size_before = width_before * height_before * bits_before
    size_after = width_after * height_after * bits_after
    saved_per_photo = size_before - size_after
    total_saved_bits = saved_per_photo * num_photos
    if total_saved_bits % 8192 != 0:  # проверка на целое число
        return None
    total_saved_bytes = total_saved_bits // 8
    total_saved_kbytes = total_saved_bytes // 1024
    return total_saved_kbytes

while True:
    # --1 подбор стартового и сжатого размера

    min_sizes = ['1280', '720', '1920', '1080', '1440']
    max_sizes = ['2560', '3840', '2160', '4320', '7680']

    xs = int(random.choice(max_sizes))
    ys = int(random.choice(max_sizes))
    start_size = f'{max(int(xs), int(ys))}x{min(int(xs), int(ys))}'

    xf = int(random.choice(min_sizes))
    yf = int(random.choice(min_sizes))
    final_size = f'{max(int(xf), int(yf))}x{min(int(xf), int(yf))}'

    # --2 подбор стартового и сжатого разрешения

    start_resolution = random.randint(12, 20)
    final_resolution = random.randint(4, 11)


    # --3 количество фотографий

    cnt_photo = random.randint(50, 150)

    result = calc_saved_kbytes(
        int(xs), int(ys), start_resolution,
        int(xf), int(yf), final_resolution,
        cnt_photo
    )

    if result != None:
        break

# Текст задачи
body_md = f"""
Маша делает цветные фотографии на телефон, который сохраняет снимки с размером {start_size} пикселей и разрешением {start_resolution} бит. 
После сохранения снимков в памяти телефона Маша отправляет фотографию через мессенджер, 
который сжимает снимок до размера {final_size} пикселей, каждый разрешением {final_resolution} бит. 
Какое количество Кбайт удастся сэкономить при отправке {cnt_photo} фотографий?
В ответе запишите целое число.
""".strip()

text_of_solve = f"""
Решение:
1. Размер одной исходной фотографии: {ys} × {xs} × {start_resolution} бит = {ys * xs * start_resolution} бит.
2. Переведём размер одной исходной фотографии в байты: {ys * xs * start_resolution} / 8 = {(ys * xs * start_resolution) // 8} байт.
3. Размер одной сжатой фотографии: {yf} × {xf} × {final_resolution} бит = {yf * xf * final_resolution} бит.
4. Переведём размер одной сжатой фотографии в байты: {yf * xf * final_resolution} / 8 = {(yf * xf * final_resolution) // 8} байт.
5. Экономия на одной фотографии: {ys * xs * start_resolution} / 8 - {yf * xf * final_resolution} / 8 = {(ys * xs * start_resolution) // 8 - (yf * xf * final_resolution) // 8} байт.
6. Экономия на {cnt_photo} фотографиях: ({(ys * xs * start_resolution) // 8 - (yf * xf * final_resolution) // 8}) × {cnt_photo} = {((ys * xs * start_resolution) // 8 - (yf * xf * final_resolution) // 8) * cnt_photo} байт.
7. Переведём экономию в Кбайты: {((ys * xs * start_resolution) // 8 - (yf * xf * final_resolution) // 8) * cnt_photo} / 1024 = {(((ys * xs * start_resolution) // 8 - (yf * xf * final_resolution) // 8) * cnt_photo) // 1024} Кбайт.
"""

# Выводы
print(body_md)
print()
print(f'Answer = {result}')
print('_________________________________')
print(text_of_solve)


















