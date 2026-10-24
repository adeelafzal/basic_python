import random
playing = True
number_to_guess = random.randint(1, 100)
while playing:
    try:
        guess = int(input("Guess number between 1 to 100: "))
        if guess < number_to_guess:
              print("too low")
        elif guess > number_to_guess:
            print("too high")
        else:
            print("Well done")
            playing = False
    except ValueError:
        print("Please enter a valid number")