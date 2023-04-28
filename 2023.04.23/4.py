digit = int(input('Введите числа: '))

range_1 = int('1' + '0' * (digit - 1))
count = 0


for num_1 in range(range_1, int('9' * digit) + 1):

    step = 0
    
    for num_2 in range(2, num_1):
    
    if num_1 % num_2 == 0:
        step += 1
        
    if step == 0:
        count += 1
        
print(count)

# Введите разряд числа: 3
# 143