import random

print("This is game called GUESS THE NUMBER")

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Give me your guess: "))
        break
    except ValueError:
        print("Your guess must be integer")


while guess != number:
    if guess > number:
        print("My number is smaller. Try again.")
        while True:
            try:
                guess = int(input("Give me your next guess: "))
                break
            except ValueError:
                print("Your guess must be integer")
    if guess < number:
        print("My number is bigger. Try again.")
        while True:
            try:
                guess = int(input("Give me your next guess: "))
                break
            except ValueError:
                print("Your guess must be integer")

print("CONGRATULATIONS ! YOU WIN !")
exit = input("Press ENTER to exit")
