num = input('Введите первое число: ')
num_1 = input('Введите второе число: ')

if num.isdecimal() and num_1.isdecimal():
    num = int(num)
    num_1 = int(num_1)
    if num_1 == 0:
        print('Ошибка, на ноль делить нельзя')

    # СДЕЛАТЬ: подумайте и перепишите нижеследующую часть кода так, чтобы обойтись только одним блоком if

    # КОММЕНТАРИЙ: скобки не нужны, следует опустить
    else:
        remainder_modulo = num % num_1       
        result = (f'{num} делится на {num_1} нацело\n'
                  f'частное: {num // num_1}\n')
        if remainder_modulo:
            result = (f'{num} не делится на {num_1} нацело\n'
                      f'неполное частное: {num // num_1}\n'
                      # ИСПРАВИТЬ: вы уже вычисляли остаток, а здесь повторно выполняете ту же операцию — неоптимально
                      f'остаток:{remainder_modulo}')
        
        print(result) 
        
   
else:
    print('Ошибка, ввод')

  




# Введите первое число: 40
# Введите второе число: 4
# 40 делится на 4 нацело
# частное: 10

# Введите первое число: 40
# Введите второе число: 6
# 40 не делится на 6 нацело
# неполное частное: 6
# остаток: 4


# ИТОГ: хорошо — 2/3
