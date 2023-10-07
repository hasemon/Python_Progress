print('Guessing game')
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop,
# then print to the input box

# Modification 1: tell user if guess is too high/low.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop,
# print to the input box (This is specific to this platform)
# Three Loop Questions:
# 1. What do I want to repeat?
#  ->
# 2. What do I want to change each time?
#  ->
# 3. How long should we repeat?
#  ->


o_number = 10
guessed = 1
g_number = int(input('Guess a number between 1 and 10: '))
while guessed <= 3:
    if g_number != o_number:
        guessed += 1
        if g_number > o_number:
            g_number = int(input('Guess is too high! guess again: '))
        else:
            g_number = int(input('Guess is too low! guess again: '))

    if g_number == o_number:
        print('Congratulations! You guessed the number!')
        break
    if guessed == 3:
        print(f'You are failed to guess the number was #{o_number}!')








