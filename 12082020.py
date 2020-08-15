import random
num_gen = random.randint(1, 19)
Input = input('Enter guess here: ')
user_guess = int(Input)
if user_guess < num_gen:
    print('Your guess is too low...')
if user_guess > num_gen:
    print('Your guess is too high...')
if user_guess == num_gen:
    print('You are correct!')
