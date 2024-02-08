number = 10
cap = 5

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? ")
    cap -= 1
    if guess == 'q' or cap == 0:
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
    print(f"You have {cap} guesses left")