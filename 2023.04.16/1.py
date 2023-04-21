num = input('Введите первое число: ')
num_1 = input('Введите второе число: ')
num_2 = input('Введите третье число: ')
summa_positiv = 0

if num.isdecimal():
    summa_positiv += int(num)
elif num.replace('.','',1).isdecimal():
    summa_positiv += float(num)

if num_1.isdecimal():
    summa_positiv += int(num_1)
elif num_1.replace('.','',1).isdecimal():
    summa_positiv += float(num_1)

if num_2.isdecimal():
    summa_positiv += int(num_2)
elif num_2.replace('.','',1).isdecimal():
    summa_positiv += float(num_2)
    
print(f'{summa_positiv:.1f}')


# Введите первое число: 4
# Введите второе число: -22
# Введите третье число: 1.5
# 5.5