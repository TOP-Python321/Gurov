text = input('Введите текст: ')

text_1 = ''

for i in range(len(text)):

    if text[i] == ' ':
        text_1 += ''
        
    else:
        text_1 += text[i]
        
total = len(text_1) * 30

print(f'{total // 100} руб. {total % 100} коп.')