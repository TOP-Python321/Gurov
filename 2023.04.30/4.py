case = {}

while True:

    inp = input('Введите число и через пробел значение\n(для выхода - введите пустую строку): ')
    if not inp:
        break
    
    list_inp = inp.split()
    case[list_inp[0]] = list_inp[1]
    
inp_value = input('Введите значение из словаря: ')

for k, v in case.items():
    
    if v == inp_value:
        print(k)
        break

else:
    print('! value error !')    
    
# 123 манго
# 124 слива
# 125 груша
# 126 арбуз
# 127 ананас
# 128 апельсин

# Введите значение из словаря: слива
# 124