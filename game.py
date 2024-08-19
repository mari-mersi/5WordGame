from random import *


def random_word():  # случайное слово из списка
    r = randint(0, len(words))  # случайный индекс массива слов
    return words[r]


def find_word(attempt):  # функция проверки слова
    def vvod(at):
        global my_word
        print('Осталось попыток: ', at)
        # print(flag_word)
        print('Введите слово из ', k, ' букв: ', end='')
        my_word = input()
        my_word.encode(encoding='utf-8')

    global flag_word, my_word, flag_game, sost
    if flag_word == 0:  # слово не из k б.
        # print("len =", len(my_word), "; k=",k)
        # print("mw= ",my_word)
        vvod(attempt)
        if len(my_word) == k:
            flag_word = 1
        else:
            print('Вы ввели не верное количество букв.')
        find_word(attempt)

    elif flag_word == 1:  # слово из k б, но его нет в списке
        flag = False
        for i in range(0, len(words)):
            # print('hi')
            # print(i,'. mw=',my_word,'; wi=',words[i])
            # print(my_word==words[i])
            # print(len(my_word), len(words[i]))
            # for j in range(0, len(words[i])):
            # print(words[i][j], end='!')
            if my_word == words[i]:
                flag = True
                # print(i,flag)
        if flag:
            flag_word = 2
        else:
            print('Вы ввели не существительное.')
            vvod(attempt)
        find_word(attempt)

    elif flag_word == 2:  # слово из k б, оно есть в списке
        f = [False] * k
        l_mw = list(my_word)
        for i in range(0, k):
            if my_word[i] == game_word[i]:  # правильная буква и ее место
                sost[i] = 1  ################################
                f[i] = True
                # flag_game=True
            else:
                f[i] = False
                # flag_game=False
                f2 = False
                for j in range(0, k):
                    if my_word[i] == game_word[j]:
                        f2 = True
                if f2:  # правильная буква, не правильное место
                    sost[i] = 2  #############################
                else:  # не правильная буква
                    sost[i] = 3  ########################3###
            # print(f[i])
        for i in range(0, k):  # Вывод побуквенно
            print(l_mw[i], end=' ')
        print()
        for i in range(0, k):
            print(sost[i], end=' ')
        print()
        # print(l_mw)
        # print(sost)
        for i in range(0, len(f)):
            # print(i, f[i])
            if f[i] == False:
                flag_game = False
        # print(flag_game)
        if flag_game:
            flag_word = 3
            find_word(attempt)
        else:
            flag_game = True
            if attempt - 1 == 0:
                flag_word = 4
                find_word(attempt)
            else:
                vvod(attempt - 1)
                find_word(attempt - 1)

    elif flag_word == 3:  # слово правильное, игра выйграна
        print("Вы выйграли!")
    else:  # игра пойграна
        print("Вы проиграли.")

    '''if flag_game:
        print("Вы выйграли")
    else:
        print("Вы проиграли")'''


k = 5  # количество букв в слове
p = 6  # количество попыток
sost = [0] * k  # флаги букв слова
flag_game = True  # флаг игры
flag_word = 0  # флаг слова, где    0- слово не из k б.,
# 1- слово из k б, но его нет в списке,
# 2- слово из k б, оно есть в списке
words = []  # список слов
# w=['']*k

# получение списка слов из файла
f = open('word5b.txt', 'r', encoding='utf-8')
for word in f:
    temp = ''
    for j in range(0, k):
        temp = temp + word[j]
    words.append(temp)

game_word = random_word()  # загаданое слово
my_word = ''
print("Загаданное слово:", game_word)
print("Возможные состояния букв:\n"
      "1 - правильная буква, правильное место\n"
      "2 - правильная буква, не правильное место\n"
      "3 - не правильная буква\n")

find_word(p)
