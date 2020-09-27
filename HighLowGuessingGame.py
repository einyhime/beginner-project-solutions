from random import randint

print("---------------------")
print("NUMBER GUESSING GAME")
print("---------------------")
print("\nI'm thinking of a number from 1 to 100...")
print("Try guessing it!")

name = input("\nWhat is your name? ")

while True:
    num = randint(1, 101)
    count = 0
    
    while True:
        guess = input("\nEnter your guess (press Q to quit) : ")
        if guess.isnumeric():
            guess = int(guess)
        elif guess == 'q':
            break
        else:
            print("Invalid input")
            break
        
        count += 1
        if guess == num:
            print(f"Congrats, {name}! You guessed it right!")
            print(f"Number of try: {count}.")
            break
        else:
            if guess > num:
                hilo = "high"
            else:
                hilo = "low"
            print(f"Your guess is too {hilo}.")

    again = input("\nPlay again? Press Q to quit! ")
    if again == "q":
        print(f"Thanks for playing. Bye, {name}!")
        break
