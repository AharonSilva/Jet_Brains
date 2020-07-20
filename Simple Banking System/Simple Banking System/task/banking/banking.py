# Write your code here
import random
import math
import sqlite3

# todo: create do transfer option
#   exceptions to handle:
#   1) If the user tries to transfer more money than he/she has, output: "Not enough money!"
#   2) If the user tries to transfer money to the same account, output the following message:
#      “You can't transfer money to the same account!”
#   3) If the receiver's card number doesn’t pass the Luhn algorithm, you should output:
#      “Probably you made mistake in the card number. Please try again!”
#   4) If the receiver's card number doesn’t exist, you should output: “Such a card does not exist.”
#   5) If there is no error, ask the user how much money they want to transfer and make the transaction.


class Banking:

    # SQL QUERIES
    CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS card
             (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)'''
    INSERT_CARD = '''INSERT INTO card (number, pin) VALUES (?, ?);'''
    GET_BALANCE = '''SELECT balance FROM card WHERE number = ? AND pin = ?; '''
    LOOKUP_ACCOUNT = '''SELECT id FROM card WHERE number = ? AND pin = ?; '''
    DEL_ACCOUNT = '''DELETE FROM card WHERE number = ?;'''
    ADD_INCOME = '''UPDATE card SET balance = balance + (?) WHERE number = (?);'''
    SUBTRACT_INCOME = '''UPDATE card SET balance = balance - (?) WHERE number = (?);'''
    LOOKUP_CARD = '''SELECT number FROM card WHERE number = ?;'''

    # CLASS FUNCTIONS
    def __init__(self):
        self.user_log = []
        self.loaded_records = []
        self.conn = self.connect()
        self.create_tables(self.conn)
        self.card = ''
        self.pin = ''

    # ALL SQL FUNCTIONS HERE:
    @staticmethod
    def connect():
        connection = sqlite3.connect('card.s3db')
        return connection

    def create_tables(self, connection):
        with connection:
            connection.execute(self.CREATE_TABLE)

    def delete_account(self, connection, number):
        with connection:
            connection.execute(self.DEL_ACCOUNT, (number,))

    def lookup_card(self, connection, number):
        with connection:
            return connection.execute(self.LOOKUP_CARD, (number,)).fetchone()

    def add_income(self, connection, income, number):
        with connection:
            connection.execute(self.ADD_INCOME, (income, number))

    def subtract_income(self, connection, income, number):
        with connection:
            connection.execute(self.SUBTRACT_INCOME, (income, number))

    def create_credit_card(self, connection, number, pin):
        with connection:
            return connection.execute(self.INSERT_CARD, (number, pin)).fetchall()

    def show_card_balance(self, connection, card, pin):
        with connection:
            return connection.execute(self.GET_BALANCE, (card, pin)).fetchone()[0]

    def login_to_account(self, connection, card, pin):
        with connection:
            return connection.execute(self.LOOKUP_ACCOUNT, (card, pin)).fetchone()

    # ALL MAIN FUNCTIONS HERE:
    def main_menu(self):
        print('1. Create an account\n2. Log into account\n0. Exit')
        m_menu_opt = int(input())
        print('')
        if m_menu_opt == 1:
            self.create_account()
        elif m_menu_opt == 2:
            self.log_to_account()
        elif m_menu_opt == 0:
            exit()
        else:
            print('Incorrect Value')
            self.main_menu()

    def card_menu(self):
        print('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit')
        c_menu_opt = int(input())
        print('')
        if c_menu_opt == 0:
            print('Bye!')
            exit()
        elif c_menu_opt == 1:
            print(f'Balance: {self.show_card_balance(self.conn, self.card, self.pin)}')
            self.card_menu()
        elif c_menu_opt == 2:
            income = int(input('\nEnter income:\n'))
            self.add_income(self.conn, income, self.card)
            print('\nIncome was added!\n')
            self.card_menu()
        elif c_menu_opt == 3:
            destined_account = str(input('Transfer\nEnter card number:\n'))
            try:
                if self.check_luhn(destined_account) != 0:
                    print('Probably you made mistake in the card number. Please try again!\n')
                elif self.lookup_card(self.conn, destined_account)[0] != destined_account:
                    print('Such a card does not exist.\n')
                elif destined_account == self.card:
                    print('You can\'t transfer money to the same account!\n')
                else:
                    deposit = int(input('Enter how much money you want to transfer:'))
                    if deposit > self.show_card_balance(self.conn, self.card, self.pin):
                        print('Not enough money!\n')
                    else:
                        self.add_income(self.conn, deposit, destined_account)
                        self.subtract_income(self.conn, deposit, self.card)
                        print('Success!\n')
            except TypeError:
                print('Such a card does not exist.\n')
            self.card_menu()
        elif c_menu_opt == 4:
            self.delete_account(self.conn, self.card)
            print('\nThe account has been closed!\n')
            self.main_menu()
        elif c_menu_opt == 5:
            print('You have successfully logged out!')
            print('')
            self.main_menu()
        else:
            print('Error')
            self.main_menu()

    @staticmethod
    def luhn_algorithm(card_n):
        card_incomplete = str(card_n)
        first_step = [int(x) for x in card_incomplete]
        second_step = []
        third_step = []
        fourth_step = 0
        for x in range(0, len(first_step)):
            if (x + 1) % 2 == 0:
                second_step.append(int(first_step[x]))
            else:
                second_step.append(int(first_step[x]) * 2)
        for x in range(0, len(second_step)):
            if second_step[x] > 9:
                third_step.append(second_step[x] - 9)
            else:
                third_step.append(second_step[x])
        for x in third_step:
            fourth_step += x
        card_sum = fourth_step / 10
        luhn = math.ceil(card_sum)
        diff = (float(luhn) - float(card_sum))
        diff = int(round(diff * 10, 2))
        final_step = [x for x in card_incomplete]
        final_step.append(str(diff))
        card_number = ''.join(final_step)
        return card_number

    @staticmethod
    def check_luhn(card):
        check_dig = [int(x) for x in card]
        sum_dig = 0
        last_dig = check_dig[-1]
        check_dig.pop(-1)
        for i in range(0, len(check_dig)):
            if i % 2 == 0:
                check_dig[i] *= 2
        for i in range(0, len(check_dig)):
            if check_dig[i] > 9:
                check_dig[i] -= 9
        for i in range(0, len(check_dig)):
            sum_dig += check_dig[i]
        if ((sum_dig + last_dig) % 10) != 0:
            status = 1
        else:
            status = 0
        return status

    def create_account(self):
        pin = format(random.randint(0000, 9999), '04d')
        account_number = random.randint(000000000, 999999999)
        card_inc = 400000000000000 + account_number
        card = self.luhn_algorithm(card_inc)
        self.create_credit_card(self.conn, card, pin)
        print('Your card has been created')
        print('Your card number:')
        print(card)
        print('Your card PIN:')
        print(pin)
        print('')
        self.main_menu()

    def log_to_account(self):
        card = str(input('Enter your card number:\n'))
        pin = str(input('Enter your PIN:\n'))
        self.card = card
        self.pin = pin

        try:
            if int(self.login_to_account(self.conn, card, pin)[0]) > 0:
                print('You have successfully logged in!')
                print('')
                self.card_menu()
        except TypeError:
            print('Wrong card number or PIN!')
            print('')
            self.main_menu()


if __name__ == '__main__':
    Banking().main_menu()
