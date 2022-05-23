#Sifr_cesar

print('Программа шифровки / дешифровки текста по методу Цезаря')
txt = input('Введите пожалуйста текст ')
a = (input('Что необходимо сделать? шифровать / дешифровать '))
b = int(input('Введите шаг сдвига для шифровки или дешифровки '))
bb = str(b)
if bb.isdigit() == False:
    b = int(input('Введите пожалуйста целое число '))

eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ru_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


# шифровать
def sifr(txt, b):
    result = ''
    for i in txt:
        if i.isalpha() and i in eng_lower:
            c = eng_lower.find(i) + b
            if c > 24:
                c += - 26
                result += eng_lower[c]
            else:
                result += eng_lower[c]
        elif i.isalpha() and i in eng_upper:
            c = eng_upper.find(i) + b
            if c > 24:
                c += - 26
                result += eng_upper[c]
            else:
                result += eng_upper[c]
        elif i.isalpha() and i in ru_lower:
            c = ru_lower.find(i) + b
            if c > 31:
                c += - 32
                result += ru_lower[c]
            else:
                result += ru_lower[c]
        elif i.isalpha() and i in ru_upper:
            c = ru_upper.find(i) + b
            if c > 31:
                c += - 32
                result += ru_upper[c]
            else:
                result += ru_upper[c]
        else:
            result += i
    print(result)


# дешифровать
def desifr(txt, b):
    result = ''
    for i in txt:
        if i.isalpha() and i in eng_lower:
            c = eng_lower.find(i) - b
            result += eng_lower[c]
        elif i.isalpha() and i in eng_upper:
            c = eng_upper.find(i) - b
            result += eng_upper[c]
        elif i.isalpha() and i in ru_lower:
            c = ru_lower.find(i) - b
            result += ru_lower[c]
        elif i.isalpha() and i in ru_upper:
            c = ru_upper.find(i) - b
            result += ru_upper[c]
        else:
            result += i
    print(result)


t = False
y = 'да'
while t == False:
    if a == 'шифровать' or a == '':
        sifr(txt, b)
        t = True
    elif a == 'дешифровать' or a == ' ':
        desifr(txt, b)
        # b += 1
        # if b == 26:
        t = True
    else:
        a = (input('Необходимо ввести конкретнее? шифровать / дешифровать '))