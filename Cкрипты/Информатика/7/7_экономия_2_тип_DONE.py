import random


# функция для посчёта сохранённых килобайт
def calc_saved_kbytes(
    width_before, height_before, bits_before,
    width_after, height_after, bits_after,
    num_photos
):
    size_before = width_before * height_before * bits_before
    size_after = width_after * height_after * bits_after
    saved_per_photo = size_before - size_after
    total_saved_bits = saved_per_photo * num_photos
    if total_saved_bits % 8192 != 0:
        return None
    total_saved_bytes = total_saved_bits // 8
    total_saved_kbytes = total_saved_bytes // 1024
    return total_saved_kbytes

# функция для вычисления алфавита
def count_of_colors(bits, max_min_choice):
    if max_min_choice == 'минимальное':
        return 2 ** (bits - 1) + 1
    else:
        return 2 ** bits


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

    saved_kbytes = calc_saved_kbytes(
        int(xs), int(ys), start_resolution,
        int(xf), int(yf), final_resolution,
        cnt_photo
    )
    if saved_kbytes != None:
        break



# -- выбор между максимальным и минимальным в ответе

max_min_choice = random.choice(['минимальное', 'максимальное'])


body_md = f"""
Маша делает цветные фотографии на телефон, который сохраняет снимки с размером {start_size} пикселей и разрешением {start_resolution} бит. 
После сохранения снимков в памяти телефона Маша отправляет фотографию через мессенджер, 
который сжимает снимок до размера {final_size} пикселей. 
При отправке {cnt_photo} фотографий удалось сэкономить {saved_kbytes} Кбайт. 
Какое {max_min_choice} количество цветов может быть в сжатой картинке?
В ответе запишите целое число.
""".strip()

text_of_solve = f"""
Решение:
1. Размер одной исходной фотографии: {xs} × {ys} × {start_resolution} бит = {xs * ys * start_resolution} бит.
2. Переведём размер одной исходной фотографии в байты: {xs * ys * start_resolution} / 8 = {(xs * ys * start_resolution) // 8} байт.
3. Переведём размер одной исходной фотографии в Кбайты: {(xs * ys * start_resolution) // 8} / 1024 = {((xs * ys * start_resolution) // 8) // 1024} Кбайт.
4. Размер одной сжатой фотографии: {xf} × {yf} × {final_resolution} бит = {xf * yf * final_resolution} бит.
5. Переведём размер одной сжатой фотографии в байты: {xf * yf * final_resolution} / 8 = {(xf * yf * final_resolution) // 8} байт.
6. Переведём размер одной сжатой фотографии в Кбайты: {(xf * yf * final_resolution) // 8} / 1024 = {((xf * yf * final_resolution) // 8) // 1024} Кбайт.
7. Экономия на одной фотографии: ({xs * ys * start_resolution} - {xf * yf * final_resolution}) / 8 = {(xs * ys * start_resolution - xf * yf * final_resolution) // 8} байт.
8. Экономия на {cnt_photo} фотографиях: (({xs * ys * start_resolution} - {xf * yf * final_resolution}) / 8) × {cnt_photo} = {((xs * ys * start_resolution - xf * yf * final_resolution) // 8) * cnt_photo} байт.
9. Переведём экономию в Кбайты: {((xs * ys * start_resolution - xf * yf * final_resolution) // 8) * cnt_photo} / 1024 = {saved_kbytes} Кбайт.
10. В сжатой картинке {final_resolution} бит на пиксель.
11. {max_min_choice.capitalize()} количество цветов: 
    {f"2^{final_resolution - 1} + 1 = {2 ** (final_resolution - 1) + 1}" if max_min_choice == "минимальное" else f"2^{final_resolution} = {2 ** final_resolution}"}

Ответ: {f"2^{final_resolution - 1} + 1 = {2 ** (final_resolution - 1) + 1}" if max_min_choice == "минимальное" else f"2^{final_resolution} = {2 ** final_resolution}"}

""".strip()

result = count_of_colors(final_resolution, max_min_choice)

print(body_md)
print()
print(f'Answer = {result}')
print('__________________________________')
print(text_of_solve)


















