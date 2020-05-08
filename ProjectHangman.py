# Write your code here
import random

def menu():
    choice = input('''Type "play" to play the game, "exit" to quit: ''')
    if choice == 'exit':
        exit()
    elif choice == 'play':
        hangman_game()
    else:
        pass


def hangman_game():

    random.seed()

    languages = ['python', 'java', 'kotlin', 'javascript']

    answer = random.choice(languages)

    secret = []

    all_guesses = []

    lives = 0

    for _ in answer:
        secret.append('-')

    while lives < 8:
        print('\n', ''.join(secret))
        guess = input('Input a letter: ')
        counter = 0
        if guess == '':
            print('You should print a single letter')
        elif len(guess) != 1:
            print('You should print a single letter')
        elif not guess.isascii or not guess.islower():
            if guess == '':
                pass
            else:
                print('It is not an ASCII lowercase letter')
        elif guess in all_guesses:
            print('You already typed this letter')
        elif guess in answer:
            for i in answer:
                if i == guess:
                    secret[counter] = guess
                counter += 1
            all_guesses.append(guess)
        else:
            print('No such letter in the word.')
            all_guesses.append(guess)
            lives += 1
        if answer == ''.join(secret):
            print('\n', ''.join(secret))
            print('You guessed the word!\nYou survived!\n')
            break

    if answer != ''.join(secret):
        print('You are hanged!\n')

    return False

print('H A N G M A N')

while True:
    menu()
