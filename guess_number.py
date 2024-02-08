number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? ")
    if guess == 'q':
        print(f'The number was {number}')
        break
    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        else:
            print("Not quite!")
    except ValueError:
        print("ERROR Must enter an integer")