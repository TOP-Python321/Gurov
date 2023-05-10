num = int(input('Введите число: '))
sum_num = 0

for num1 in range(1, num + 1):

    if num1 * num1 == num:
        sum_num += num1
        break
        
    elif not num % num1:
        sum_num += num1 + num // num1
        
    elif num1 * num1 > num:
        break
        
print(sum_num)

# Введите число: 50
# 93