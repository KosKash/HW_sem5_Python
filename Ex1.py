# Игра с конфетами
import random
def bot_easy_bot_first(candy: int):
    player = True
    while candy > 0:
        while True:
            if candy > 0:
                if candy > 28:
                    bot = random.randint(1, 28)
                elif candy != 1:
                    bot = random.randint(1, candy)
                else:
                    bot = 1
                candy -= bot
                print(f'Бот забрал {bot}')
                print(candy)
                player = False
            else:
                break

            if candy > 0:
                pl = input("Введите число: ")
                if not pl.isnumeric():
                    print("Вы ввели не число. Попробуйте снова: ")
                elif not 0 < int(pl) < 29:
                    print("Ваше число не диапазоне. Попробуйте снова")
                elif int(pl) > candy:
                    print('incorrect')
                elif 0 < int(pl) < 29:
                    candy -= int(pl)
                    print(candy)
                    player = True
                else:
                    break
    if player == True:
        print("Вы выйграли")
    else:
        print('Вы проиграли')

def bot_easy_player_first(candy: int):
    player = True
    while candy > 0:
        while True:
            if candy > 0:
                pl = input("Введите число: ")
                if not pl.isnumeric():
                    print("Вы ввели не число. Попробуйте снова: ")
                elif not 0 < int(pl) < 29:
                    print("Ваше число не диапазоне. Попробуйте снова")
                elif int(pl) > candy:
                    print('incorrect')
                elif 0 < int(pl) < 29:
                    candy -= int(pl)
                    print(candy)
                    player = True
                else:
                    break
            if candy > 0:
                if candy > 28:
                    bot = random.randint(1, 28)
                elif candy != candy != 1:
                    bot = random.randint(1, candy)
                else:
                    bot = 1
                candy -= bot
                print(f'Бот забрал {bot}')
                print(candy)
                player = False
            else:
                break
    if player == True:
        print("Вы выйграли")
    else:
        print('Вы проиграли')

def bot_hard_player_first(candy: int):
    player = True
    while candy > 0:
        while True:
            if candy > 0:
                pl = input("Введите число: ")
                if not pl.isnumeric():
                    print("Вы ввели не число. Попробуйте снова: ")
                elif not 0 < int(pl) < 29:
                    print("Ваше число не диапазоне. Попробуйте снова")
                elif int(pl) > candy:
                    print('incorrect')
                elif 0 < int(pl) < 29:
                    candy -= int(pl)
                    print(candy)
                    player = True
                else:
                    break
            if candy > 0:
                if candy % 29 == 0:
                    bot = 29-int(pl)
                elif candy > 28:
                    bot = candy%29
                elif candy != 1 and candy < 28:
                    bot = candy
                else:
                    bot = 1
                candy -= bot
                print(f'Бот забрал {bot}')
                print(candy)
                player = False
            else:
                break
    if player == True:
        print("Вы выйграли")
    else:
        print('Вы проиграли')

def bot_hard_bot_first(candy: int):
    player = True
    pl = 1
    while candy > 0:
        while True:
            if candy > 0:

                if candy % 29 == 0:
                    bot = 29-int(pl)
                elif candy > 28:
                    bot = candy%29
                elif candy != 1 and candy < 28:
                    bot = candy
                else:
                    bot = 1
                candy -= bot
                print(f'Бот забрал {bot}')
                print(candy)
                player = False
            else:
                break

            if candy > 0:
                pl = input("Введите число: ")
                if not pl.isnumeric():
                    print("Вы ввели не число. Попробуйте снова: ")
                elif not 0 < int(pl) < 29:
                    print("Ваше число не диапазоне. Попробуйте снова")
                elif int(pl) > candy:
                    print('incorrect')
                elif 0 < int(pl) < 29:
                    candy -= int(pl)
                    print(candy)
                    player = True
                else:
                    break
    if player == True:
        print("Вы выйграли")
    else:
        print('Вы проиграли')

print("Выберете сложность? \n1. Легкий (первый игрок) \n2. Легкий (первый бот) \n3. Сложный (первый игрок) \n4. Сложный (первый бот)")
value = input('>>> ')
match value:
    case '1':
        bot_easy_player_first(261)
    case '2':
        bot_easy_bot_first(261)
    case '3':
        bot_hard_player_first(261)
    case '4':
        bot_hard_bot_first(261)
    case __:  
        print('Incorrect') 