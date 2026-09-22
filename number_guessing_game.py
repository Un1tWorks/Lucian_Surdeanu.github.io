import random

def display():
    print("welcome to the number guessing game, your goal is to guess a random number between 1 to 100")
    print("type a number and see if you chose right, or if the right answer is higher or lower than your guess, you have 7 guesses to get the right answer, good luck!")

def playgame():
    number = random.randint(1, 100)
    guesses = 7
    
    guess = input("Enter a number:")
    
    try:
        guess = int(guess)
    except ValueError:
        print("Enter a valid number")
        guess = input("Enter a number:")

    #if guesses <= 0 and guess != number:
        #print("you have no guesses left, you lost!")
        #return
    
    if guess > 100 or guess < 1:
        print("your number must be between 1-100, try again")
        guess = input("Enter a number:")
    while number != guess and guesses > 0:
        try:
            guess = int(guess)
        except ValueError:
            print("Enter a valid number")
            guess = input("Enter a number:")
        
        guesses -= 1
        
        if guess == number:
            print(f"the number way {number}, you won!")
            print(f"you have guessed the number in {guesses}/7 guesses")
            break
        if guesses == 0 and guess != number:
            print(f"you have no guesses left, you lost! the number was {number}")
            break
        elif guess > number:
            print(f"the number is lower than {guess}, you have {guesses}/7 guesses left")
            print("guess again") 
            guess = input("Enter a number:")
        else:
            print(f"the number is higher than {guess}, you have {guesses}/7 guesses left")
            print("guess again") 
            guess = int(input("Enter a number:"))
display()
playgame()