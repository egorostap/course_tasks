# Viselica

# рандом
import random

word_list = ['карусель', 'стул', 'стол', 'карандаш', 'арбуз', 'лимон', 'автобус', 'машина', 'окно']
guessed_letters = []  # список уже названных букв
guessed_words = []  # список уже названных слов

# выбо слова
def get_word():
    word = random.choice(word_list)
    return word.upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

# основная угадать слово
def play(word):
    word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
    s = ''.join(word_completion)
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print('Загаданное слово: ', s)
    print('Допускается 6 ошибок')
    answer = input('Введите пожалуйста букву или слово целиком: ')
    # основной цикл
    while tries > 0:
        if answer.isalpha():
            answer = answer.upper()
            flag = False
            # проверка слова
            if answer == word:
                guessed_words.append(answer)
                s = word
                print('Поздравлям, вы угадали слово!')
                print(s)
                break
            # проверка буквы
            elif answer not in guessed_letters:
                for i in range(len(word)):
                    if answer == word[i]:
                        word_completion.pop(i)
                        word_completion.insert(i, word[i])
                        flag = True
                        s = ''.join(word_completion)
                if s == word:
                    print('Поздравлям, вы угадали слово!')
                    print(s)
                    guessed_words.append(s)
                    break
                elif flag == True:
                    guessed_letters.append(answer)
                    print(s)
                    answer = input('Введите пожалуйста букву или слово целиком: ')
                elif flag == False:
                    tries -= 1
                    guessed_letters.append(answer)
                    if tries > 0:
                        print(display_hangman(tries))
                        print(s)
                        answer = input('Введите пожалуйста букву или слово целиком: ')
                    else:
                        print(display_hangman(tries))
                        print('Загаданное слово: ', word)
                        print('Игра закончена')
            else:
                answer = input('Эту букву уже называли, попробуйте снова: ')
        else:
            answer = input('Некорректное значение, попробуйте снова: ')

# основной цикл программы
game = 'да'
while game == 'да':
    word = get_word()
    play(word)
    game = input('Хотите сыграть еще раз? да / нет: ')
    guessed_letters.clear()