import random

def ask_for_guess():
    while True:
        guess = input('> ')

        if guess.isdecimal():
            return int(guess)
        print('Please enter a number between 1 and 100.')

print('Guess the Number')
print()
secret_number = random.randint(1, 100)
print('I am thinking of a number between 1 and 100')

for i in range(10):
    print('You have {} guesses left. Take a guess.'.format(10-i))

    guess = ask_for_guess()
    if guess == secret_number:
        break    # Break out of the for loop if the guess is correct.

    # Offer a hint:
    if guess < secret_number:
        print('Your guess is too low.')
    if guess > secret_number: 
        print('Your guess is too high')

# Reveal the results:
if guess == secret_number:
    print('Yay! You guessed my number!')
else:
    print('Game over. The number I was thinking of was {secret_number}')