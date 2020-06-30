# Write your code here
import random
import os.path


class GameRPS:

    def __init__(self):
        self.default = ['rock', 'paper', 'scissors']
        self.custom = []
        self.players = []
        self.index = 0
        self.names = []

    def open_rating_file(self):
        try:
            if os.path.isfile('rating.txt'):
                pass
            else:
                with open('rating.txt', 'w') as r_file:
                    print('test', '150', file=r_file, flush=True)
        finally:
            with open('rating.txt', 'r') as r_file:
                for lines in r_file.readlines():
                    self.players.append(lines.strip().split(' '))
            self.names = [x[0] for x in self.players]

    def close_rating_file(self):
        with open('rating.txt', 'w') as r_file:
            for lines in self.players:
                print(lines[0], lines[1], file=r_file, flush=True)

    @staticmethod
    def player_name():
        name = str(input('Enter your name: '))
        return name

    @staticmethod
    def player_choice():
        entry = str(input())
        return entry

    def game_options(self):
        input_options = str(input())
        self.custom = [x for x in input_options.split(',')]
        if self.custom == ['']:
            self.custom = self.default
        print('Okay, Let\'s start')

    def check_player(self):
        name_player = self.player_name()
        if name_player in self.names:
            self.index = self.names.index(name_player)
        else:
            new_player = [name_player, '0']
            self.players.append(new_player)
            self.index = -1
        print(f'Hello, {name_player}')

    def computer_choice(self):
        choice = random.randint(0, len(self.default) - 1)
        computer = self.default[choice]
        return computer

    def play_rps(self, entry):
        pc_choice = self.computer_choice()
        rate = len(self.custom) // 2
        x = self.custom.index(pc_choice)
        try:
            y = self.custom.index(entry)
            if entry not in self.custom:
                print('Invalid input')
            elif entry == pc_choice:
                print(f'There is a draw ({pc_choice})')
                self.players[self.index][1] = int(self.players[self.index][1]) + 50
            elif (x < y and y - x <= rate) or (y < x and x - y > rate):
                print(f'Well done. Computer chose {pc_choice} and failed')
                self.players[self.index][1] = int(self.players[self.index][1]) + 100
            else:
                print(f'Sorry, but computer chose {pc_choice}')
        except ValueError:
            print('Invalid input')

    def select_options(self):
        option = self.player_choice()
        if option == '!exit':
            self.close_rating_file()
            exit()
        elif option == '!rating':
            rating = self.players[self.index][1]
            print(f'Your rating: {rating}')
        else:
            self.play_rps(option)

    def main(self):
        self.open_rating_file()
        self.check_player()
        self.game_options()
        while True:
            self.select_options()


if __name__ == "__main__":
    GameRPS().main()
