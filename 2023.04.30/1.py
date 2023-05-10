gmail_inp = input('Введите электронную почту: ')

for i in gmail_inp:

    if i == '@' and '.' in gmail_inp[gmail_inp.index('@'):]:
        print('Да')
        break

else:
    print('Нет')

# Введите электронную почту: sgd@ya.ru
# Да

# Введите электронную почту: sgd@ya
# Нет