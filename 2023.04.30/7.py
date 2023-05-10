list_of = [
    {
        'Липецк': 1,
        'Пермь': 9,
        'Ростов-на-Дону': 6,
        'Тула': 3,
        'Ульяновск': 7,
        'Ярославль': 9
    },
    {
        'Барнаул': 5,
        'Краснодар': 9,
        'Красноярск': 9,
        'Махачкала': 5,
        'Новосибирск': 7,
        'Пермь': 3,
        'Ростов-на-Дону': 5,
        'Самара': 2,
        'Санкт-Петербург': 6,
        'Хабаровск': 7
    },
    {
        'Краснодар': 4,
        'Красноярск': 1,
        'Москва': 1,
        'Санкт-Петербург': 4,
        'Тольятти': 9,
        'Тула': 2,
        'Тюмень': 5,
        'Ульяновск': 4
    },
]

list_out = {}

for i in list_of:

    for k, v in i.items():

        if k in list_out:
            list_out[k] = list_out[k] | {v}

        else:
            list_out[k] = {v}

print(*{f'{repr(k)}: {v}'
      for k, v in list_out.items()}, sep=',\n')

# 'Липецк': {1},
# 'Краснодар': {9, 4},
# 'Пермь': {9, 3},
# 'Тольятти': {9},
# 'Самара': {2},
# 'Ульяновск': {4, 7},
# 'Барнаул': {5},
# 'Новосибирск': {7},
# 'Махачкала': {5},
# 'Тюмень': {5},
# 'Хабаровск': {7},
# 'Санкт-Петербург': {4, 6},
# 'Москва': {1},
# 'Красноярск': {9, 1},
# 'Ростов-на-Дону': {5, 6},
# 'Ярославль': {9},
# 'Тула': {2, 3}