import random
import re
import json
import fileinput

valid_name_eng = re.compile(r'^([a-zA-Zа][\D]{3,15})$')
valid_name_rus = re.compile(r'^([а-яёА-ЯЁ][\D]{3,15})$')


class User:

    def __init__(self, name_user, surname_user):
        if not valid_name_rus.match(name_user):
            if not valid_name_eng.match(name_user):
                raise ValueError('Не правильный формат')
        if not valid_name_rus.match(surname_user):
            if not valid_name_eng.match(surname_user):
                raise ValueError('Не правильный формат')
        self.name_user = str(name_user)
        self.surname_user = str(surname_user)
        self.balance = 1000
        ord_name = [ord(n) for n in self.name_user.lower()]
        ord_surname = [ord(s) for s in self.surname_user.lower()]
        check_digit_name = 0
        check_digit_surname = 0
        for i in ord_name:
            check_digit_name = check_digit_name + i
        for z in ord_surname:
            check_digit_surname = check_digit_surname + z
        self.uniq_number_user = int(((check_digit_name * 10) + (check_digit_surname)))
        with open('users_id.csv', 'r') as r:
            for i in r:
                if f'{self.uniq_number_user}\n' == i:
                    msg = 'Пользователь уже существует'
                    raise ValueError(msg)
        print(
            f'Создан пользователь: {self.name_user.capitalize()} {self.surname_user.capitalize()}\nUser_id: {self.uniq_number_user}')
        with open('users_id.csv', 'a') as f, open('users_list.txt', 'a', encoding='utf-8') as n, open(
                'users_balance.csv', 'a') as q:
            f.write(f'{self.uniq_number_user}\n')
            n.write(f'{self.name_user} {self.surname_user} : {self.uniq_number_user}\n')
            q.write(f'{self.uniq_number_user}: {self.balance}\n')


class Transfer(User):
    @staticmethod
    def show_id():
        with open('users_list.txt', 'r', encoding='utf-8') as r:
            for i in r:
                print(i)

    @staticmethod
    def show_balance_id(user_id):
        with open('users_balance.csv', 'r', encoding='utf-8') as f:
            for i in f:
                id, bal = i.split(':')
                if str(user_id).replace(' ', '') == id.replace(' ', ''):
                    print(f'Пользователь {id}\nБаланс: {bal}')
                    bal = bal.replace('\n', '')
                    bal = bal.replace(' ', '')
                    return bal

    @staticmethod
    def show_all_balance():
        with open('users_balance.csv', 'r', encoding='utf-8') as f:
            for i in f:
                print(i)


class Insufficient_funds(Exception):
    def __init__(self, txt):
        self.txt = txt


class Game_Thumble():
    @staticmethod
    def replace_win(bet, user_id, stat_hard):
        with open('users_balance.csv', 'r+', encoding='utf-8') as f, open('help_log.txt', 'a',
                                                                          encoding='utf-8') as ts:
            for i in f:
                id, bal = i.split(':')
                bal = bal.replace('\n', '')
                if str(user_id) == id.replace(' ', ''):
                    if not stat_hard:
                        ts.write(f'{user_id} : {float(bal) + (bet * 1.5 - bet)}\n')
                    if stat_hard:
                        ts.write(f'{user_id} : {float(bal) + (bet * 3 - bet)}\n')
                else:
                    ts.write(i)
        with open('users_balance.csv', 'w', encoding='utf-8') as f, open('help_log.txt', 'r',
                                                                         encoding='utf-8') as ts:
            for i in ts:
                f.write(i)

    @staticmethod
    def replace_loss(bet, user_id):

        with open('users_balance.csv', 'r+', encoding='utf-8') as f, open('help_log.txt', 'a',
                                                                          encoding='utf-8') as ts:
            for i in f:
                id, bal = i.split(':')
                bal = bal.replace('\n', '')
                if str(user_id) == id.replace(' ', ''):
                    ts.write(f'{user_id} : {float(bal) - bet}\n')
                else:
                    ts.write(i)
        with open('users_balance.csv', 'w', encoding='utf-8') as f, open('help_log.txt', 'r',
                                                                         encoding='utf-8') as ts:
            for i in ts:
                f.write(i)

    @staticmethod
    def generate_thimble(number):
        for i in range(3):
            if i == 0 or i == 2:
                for j in range(4):
                    print('-', end='')
            else:
                print('|', end='')
                for j in range(1, 3):
                    if j == 2:
                        print(number, end='')
                    else:
                        print(' ', end='')
                print('|', end='')
            print()

    def __init__(self, user_id, bet, hard=False):
        self.user_id = user_id
        self.bet = bet
        self.hard = hard
        self.margin = 0.03
        check_user = False
        with open('users_id.csv', 'r', encoding='utf-8') as f:
            for i in f:
                if str(self.user_id) == i.replace('\n', ''):
                    check_user = True
            if not check_user:
                raise ValueError('Пользователь не существует')
        bal = Transfer.show_balance_id(self.user_id)
        if self.bet > float(bal):
            raise Insufficient_funds('недостаточно баланса')
        game_icon = [1, 2, 3]
        game_stat_win = False
        hard_game = {1: False, 2: False, 3: False}
        not_hard = {1: True, 2: True, 3: True}
        with open('help_log.txt', 'w') as f:
            pass
        if not hard:
            print('Легкий режим с двумя выигрышными шарами\nКоэффициент выигрыша х1.5')
            Game_Thumble.generate_thimble(1), Game_Thumble.generate_thimble(2), Game_Thumble.generate_thimble(3)
            loss_pos = random.choice(game_icon)
            not_hard[loss_pos] = False
            while True:
                user_choice = int(input('Сделай выбор ячейки от 1 до 3\n'))
                if 4 > user_choice > 0:
                    break
            game_stat_win = not_hard[user_choice]
            if game_stat_win:
                print(f'ты выиграл {(bet * 1.5)}')
                Game_Thumble.replace_win(self.bet, self.user_id, hard)
            else:
                print('Ты проиграл')
                Game_Thumble.replace_loss(self.bet, self.user_id)
                for k, v in not_hard.items():
                    if v:
                        print('Выигрыш был тут:')
                        Game_Thumble.generate_thimble(k)
        else:
            print('Сложный режим с 1 выигрышным шаром\nКоэффициент выигрыша х3')
            Game_Thumble.generate_thimble(1), Game_Thumble.generate_thimble(2), Game_Thumble.generate_thimble(3)
            win_pos = random.choice(game_icon)
            hard_game[win_pos] = True
            while True:
                user_choice = int(input('Сделай выбор ячейки от 1 до 3\n'))
                if 4 > user_choice > 0:
                    break
            game_stat_win = hard_game[user_choice]
            if game_stat_win:
                print(f'ты выиграл {bet * 3}')
                Game_Thumble.replace_win(self.bet, self.user_id, hard)
            else:
                print('Ты проиграл')
                Game_Thumble.replace_loss(self.bet, self.user_id)
                for k, v in hard_game.items():
                    if v:
                        print('Выигрыш был тут:')
                        Game_Thumble.generate_thimble(k)


admin_add = User('Diana', 'Blizzard')  # Добавление нового пользователя
# Transfer.show_balance_id(111299)  # Проверить баланс по ид пользователя
# Transfer.show_id() # Получить список всех ид
# Transfer.show_all_balance() #Получить балансы всех пользователей
# Game_Thumble(111299, 200, False)  # ид игрока, ставка, режим сложности , - игра наперстки нужно угадать где шар.