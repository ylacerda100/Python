from random import randint

number = randint(1, 100)
print('Welcome to the guessing game!!')
print('Now, we are generating a number...')
print('Done!!')

while True:
    op = input("Let's go? (y/n)").lower()
    if op == "y":
        guess = int(input("What's your guess? "))
        if guess == number:
            print("That's Correct!!! Congratulations my friend.")
            break
        elif guess < number:
            print("That's too bad =/ your guess is too low. Please, try again!")
        elif guess > number:
            print("That's too bad =/ your guess is too high. Please, try again!")
        else:
            print("Please, type a valid number!!")
    elif op == "n":
        print("Leaving... =/")
        break
    else: 
        print("Enter a valid option!")


