coor_1 = input('Введите координаты первой клетки: ')
coor_2 = input('Введите координаты второй клетки: ')


# ИСПОЛЬЗОВАТЬ: сложносоставные выражения лучше записывать на нескольких строчках — так проще, а значит быстрее читается
if ('a' <= coor_1[0] <= 'h'
		and '1' <= coor_1[1] <= '8'
		and 'a' <= coor_2[0] <= 'h'
		and '1' <= coor_2[1] <= '8'):
	if (ord(coor_1[0]) + int(coor_1[1])) % 2 == (ord(coor_2[0]) + int(coor_2[1])) % 2:
		print('да')
	else:
		# ИСПРАВИТЬ: отступ поплыл
        print('нет')
else:
    print('Ошибка, ввод')


# ведите координаты первой клетки: c5
# Введите координаты второй клетки: f2
# да


# ИТОГ: очень хорошо — 4/5
