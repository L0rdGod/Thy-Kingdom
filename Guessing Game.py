guess = ""

secret_number = 25

print("GUESS THE NUMBER!")
print('Guess the secret number ranging from 1 to 100.')
print('Guess limit is five (5)')

guess_count = 1
for guess_count in range(5):
    guess = int(input('Enter your guess here: '))
    guess_count += 1
    if guess > 100:
      print('Number must be from 1 to 100.')
    elif guess > secret_number:
      print('Try a lower value.')
    elif guess < secret_number:
      print('Try a higher value.')
    elif guess == secret_number:
      print('You got it right!')
      break 
else:
    print('Oh snap! \nYou ran out of guesses! \nGame Over')