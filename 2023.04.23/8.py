num = int(input('Введите натуральное число: '))

num_1 = 0
case = [1, 1]

if num == 1:
    print(case[1])
        
elif num == 2:
    print(*case)
        
else:
    for i in range(3, num + 1):
        
        case += [case[-1] + case[-2]]
        
    print(*case)
    
# Введите натуральное число: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597