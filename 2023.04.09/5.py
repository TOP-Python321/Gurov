# КОММЕНТАРИЙ: целая часть (числа) — integral part, дробная часть (числа) — fractional part
whole_part = int(input('Введите целую часть: '))
remains_part = int(input('Введите дробную часть: '))

miles = float(f'{whole_part}.{remains_part}')

# ИСПРАВИТЬ: если результат округления должен быть использован где-то ещё, тогда используете функцию round(); в данном случае выгоднее воспользоваться синтаксисом f-строк
print(f'{miles} миль = {round(miles*1.61,1)} км')


# Введите целую часть: 15
# Введите дробную часть: 7
# 15.7 миль = 25.3 км


# ИТОГ: отлично — 4/4
