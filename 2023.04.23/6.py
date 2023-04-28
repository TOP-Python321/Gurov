num = input('Введите шестизначное число: ')

num_1, num_2 = 0, 0

for i in range(3):
    num_1 += int(num[i])
    
for i in range(3, 6):
    num_2 += int(num[i])
    
if num_1 == num_2:
    print('Да')
    
else:
    print('Нет
    
# Введите шестизначное число: 183534
# Да

# Введите шестизначное число: 401367
# Нет