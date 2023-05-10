inp = input("Введите числа через пробел: ").split()
inp_1 = input("Введите числа через пробел: ").split()

print_out = 'Нет'
list_int, list_int_1 = [int(i) for i in inp], [int(i) for i in inp_1]

if not list_int_1:
    print_out = 'Да'
    
else:
    for i in range(len(list_int)):

        for k in list_int:

            if list_int[i] == k and list_int_1 == list_int[i:i + len(list_int_1)]:
                print_out = 'Да'
                break

print(print_out)


# Введите числа через пробел: 1 2 3 4
# Введите числа через пробел: 1 2
# Да

# Введите числа через пробел: 1 2 3 4
# Введите числа через пробел: 2 4
# Нет