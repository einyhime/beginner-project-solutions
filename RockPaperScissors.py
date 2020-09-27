from random import choice

comPoints = 0
userPoints = 0
choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
wins = ["pr", "sp", "rs"]

print("------------------------")
print("ROCK PAPER SCISSORS GAME")
print("------------------------")

while True:
    comChoice = choice('rps')
    while True:
        userChoice = input("Rock Paper Scissors? (r/p/s): ")
        if userChoice not in 'rps':
            print("Invalid input")
        else:
            break
    
    print()

    if userChoice == comChoice:
        print("Draw")
        print("Both player chose", choices[userChoice])
    elif userChoice in wins:
        print("User won!")
        userPoints += 1
    else:
        print("Computer won!")
        comPoints += 1

    print(f"User: {choices[userChoice]}, Com: {choices[comChoice]}")
    print(f"Current scores: User {userPoints} vs Computer {comPoints}.\n")

    check = input("Play again? Press Q to quit. ")
    if check == 'q':
        break

    print()