# переменные
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_ '
hard = 'il1Lo0O'
chars = ''

# настройки пароля
kolich = int(input('Количество паролей для генерации: '))
lenght = int(input('Длина одного пароля: '))
have_digits = input('Включать ли цифры 0123456789?  да / нет: ')
have_uppercase = input('Включать ли прописные буквы: ABCDEFGHIJKLMNOPQRSTUVWXYZ? да / нет: ')
have_lowercase = input('Включать ли строчные буквы: abcdefghijklmnopqrstuvwxyz? да / нет: ')
have_punctuation = input('Включать ли символы !#$%&*+-=?@^_? да / нет: ')
exclude_hard = input('Исключать ли неоднозначные символы il1Lo0O? да / нет: ')

if  have_digits == 'да':
    chars += digits
if have_uppercase == 'да':
    chars += uppercase_letters
if have_lowercase == 'да':
    chars += lowercase_letters
if have_punctuation == 'да':
    chars += punctuation
#if exclude_hard == 'да':
    #chars.replace('i')
    #chars.replace('1')
    #chars.replace('l')
    #chars.replace('L')
    #chars.replace('o')
    #chars.replace('0')
    #chars.replace('O')

import random

# генератор паролей
def  generate_password(l, c):
    parol = ''
    for i in range(l):
        a = random.randrange(len(c))
        parol = parol + c[a]
    print(parol)
for i in range(kolich):
    generate_password(lenght, chars)