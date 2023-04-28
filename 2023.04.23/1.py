num = []
while True:
    inp = input('Введите целое число: ')
    
    if int(inp) % 7:
        break
        
    num += [inp]
    
num = (num[::-1])
# или
# case.reverse()

print(' '.join(num))




