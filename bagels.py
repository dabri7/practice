import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagles, logical deduction game.
          I have in my mind {} - digit numer, each digit is unique. Try to guess this number.
          Here are the hints:
          When i say:
          Piko: It means one digit is correct but in wrong position.
          Fermi: One digit is correct and in correct position.
          Bagels: All digits are wrong. 
          
          For example, if secret number is 248, and you say 843, the hint will be: Fermi Piko'''.format(NUM_DIGITS))

    while True:
        secret_num = get_secret_num()
        print(f'I have {NUM_DIGITS}-digit number in my head.'
              f'You have {MAX_GUESSES} guesses to find this number')
        number_of_guesses = 1
        while number_of_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Attempt #{number_of_guesses}')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            number_of_guesses += 1

            if guess == secret_num:
                break

            if number_of_guesses > MAX_GUESSES:
                print(f'You are out of guesses :('
                      f'The right number is: {secret_num}')
        print("Do you want to play again? (yes or no)")

        if not input('> ').lower().startswith('y'):
            break
    print('Thank you for playing :)')


def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'Congrats, you guessed right number'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Piko')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()
