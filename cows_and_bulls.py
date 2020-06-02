import random


print("Welcome to the Cows and Bulls Game!")

number = list(str(random.randint(1000, 9999)))

while True:

    while True:
        try:
            guess = int(input("Enter a 4-digit number: "))
            if len(str(guess)) != 4:
                print("Your number should be 4-digit long.\n")
            else:
                break
        except ValueError:
            print("Your number must be integer.\n")

    cow = 0
    bull = 0
    guess = list(str(guess))

    for i in range(len(guess)):
        if number[i] == guess[i]:
            cow += 1
        elif number[i] in guess and number[i] != guess[i]:
            bull +=1

    print(cow, "cows", bull, "bulls")

    if cow == 4:
        print("Congratulations! You WIN.")
        break
