whole_part = int(input('Введите целую часть: '))
remains_part = int(input('Введите дробную часть: '))




miles = float(f'{whole_part}.{remains_part}')

print(f'{miles} миль = {round(miles*1.61,1)} км')


# Введите целую часть: 15
# Введите дробную часть: 7
# 15.7 миль = 25.3 км

