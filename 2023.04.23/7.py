text = input('Введите текст: ')

char = '--.,:;!?–—\\\'\"()*/'

keys = [''.join(text[i]) for i in range(len(text)) if not text[i] in char ]

print(*keys, sep='')


# КОММЕНТАРИЙ: вас не смущает, что невооружённым взглядом видно, что это копия из текста задания (или другого текстового файла), а не результат собственноручного выполнения кода? вы попробуйте запустить-то, да скопировать этот текст без комментариев в консоль
# Введите текст: Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за
#  беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она
#  так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже
#  задавал доктору сегодня во время его утреннего визита.

# КОММЕНТАРИЙ: совсем не такой результат вы получите
# Было темно в гостиной Лаптев не садясь и держа шляпу в руках 
# стал извиняться за беспокойство он спросил что делать чтобы 
# сестра спала по ночам и отчего она так страшно худеет и его 
# смущала мысль что кажется эти самые вопросы он уже задавал 
# доктору сегодня во время его утреннего визита


# КОММЕНТАРИЙ: читайте комментарии там, где взяли код


# ИТОГ: было бы хорошо, если бы было написано самостоятельно — 1/3
