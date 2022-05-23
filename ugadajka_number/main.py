# угадайка

print('Добро пожаловать в числовую угадайку')


# модуль рандом
def rndm_num(n):
    import random
    num_1 = random.randint(1, n)
    return num_1


# валидность
def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    else:
        return False


# ввод числа
def input_num():
    print('Введите число от 1 до ', right)
    num = input()
    b = False
    while b == False:
        b = is_valid(num)
        if b == False:
            print('А может быть все-таки введем целое число от 1 до ', right, '?')
            num = input()
    return int(num)


# угадайка
def ugadajka():
    c = input_num()
    d = 0
    while 1 == 1:
        d += 1
        if c < a:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            c = input_num()
        elif c > a:
            print('Ваше число больше загаданного, попробуйте еще разок')
            c = input_num()
        else:
            print('Вы угадали, поздравляем!')
            print('Количество попыток = ', d)
            break


# основной блок
again = 'да'
while again.lower() == 'да':
    right = int(input('Введите правую границу диапазона чисел '))
    a = rndm_num(right)
    ugadajka()
    again = input('Еще раз? да / нет: ')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')