import random
import string

NUM_CHAR = 3
MAX_GUESSES = 2


def main():
    print('''Bagles abc, logical deduction game.
    I have in my mind {} - letters and numbers. Try to guess them.
     Here are the hints:
     When i say:
    Piko: Its means one char is correct but in wrong position.
    Fermi: One char is correct and in correct position.
    Bagles: All chars are wrong.
        
    For example, if secret chars is 23p, and you say p31, the hint will be: Fermi Piko'''.format(NUM_CHAR))

    while True:
        secret_char = get_secret_chars()
        print(f'I have {NUM_CHAR} chars(letters and/or numbers) in my head.'
              f'You have {MAX_GUESSES} guesses to find these chars')

        number_of_guesses = 1

        while number_of_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_CHAR:
                print(f'Attempt #{number_of_guesses}')
                guess = input('> ').lower()

            clues = get_clues(guess, secret_char)
            print(clues)
            number_of_guesses += 1

            if guess == secret_char:
                break

            if number_of_guesses > MAX_GUESSES:
                print('You are out of guesses :(. '
                      f'The right chars are: {secret_char}')

        if play_again() is False:
            print('Thank you for playing! bye!')
            break


def get_secret_chars():
    numbers = list('0123456789')
    letters = list(string.ascii_lowercase)
    chars = numbers + letters
    random.shuffle(chars)

    secret_chars = ''

    for i in range(NUM_CHAR):
        secret_chars += (chars[i])
    return secret_chars


def get_clues(guess, secret_chars):
    if guess == secret_chars:
        return 'Congrats, you guessed right chars!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_chars[i]:
            clues.append('Fermi')
        elif guess[i] in secret_chars:
            clues.append('Piko')

    if len(clues) == 0:
        return 'Bagles'
    else:
        clues.sort()
        return ' '.join(clues)


def play_again():
    print('Do you want to play again? (yes or no)')
    answer = input('> ').lower()
    if answer == 'yes':
        return True
    elif answer == 'no':
        return False
    else:
        play_again()


if __name__ == '__main__':
    main()
