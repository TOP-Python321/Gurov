inp = int(input('Введите натуральное число: '))
sum_num = 0

while inp > 0:
    num = input('Введите целое число: ')
    
    if num.isdecimal():
        sum_num += int(num)
    inp -= 1

print(sum_num)


# Введите натуральное число: 7
# Введите целое число: 6
# Введите целое число: 3
# Введите целое число: -5
# Введите целое число: 1
# Введите целое число: 10
# Введите целое число: -1
# Введите целое число: 8
# 28


# КОММЕНТАРИЙ: читайте комментарии там, где взяли код


# ИТОГ: было бы отлично, если бы было написано самостоятельно — 1/3

