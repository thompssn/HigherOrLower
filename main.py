import random
import time

def user_mode():
  print("Welcome to user mode! You will guess a randomized number.")

  lower_limit=int(input("Enter the lower limit of the range: "))
  upper_limit=int(input("Enter the upper limit of the range: "))

  secret_number=random.randint(lower_limit,upper_limit)

  user_guess=""
  guesses_count=0

  while user_guesses != secret_number:
    user_guess=int(input(f"Guess the number between {lower_limit}  and {upper_limit}: "))
    guesses_count += 1

    if user_guess < secret_number:
      print("Too Low! Try Again.")
    elif user_guess > secret_number:
      print("Too High! Try Again.")
  print( f"Congratulations! You Guessed the correct number {secret_number} in {guesses_count} guesses.")
  
  

def computer_mode():
    print("Welcome to computer mode! The computer will guess your number.")  
    
    # get the range and the secret number from the user
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))
    secret_number = int(input(f"Enter your secret number between {lower_limit} and {upper_limit}: "))
    
    # initialize variables
    computer_guess = ''
    guesses_count = 0
    
    # computer guesses until correct
    while computer_guess != secret_number:
        computer_guess = random.randint(lower_limit, upper_limit)
        guesses_count += 1
        
        print(f"Computer's guess: {computer_guess}")
        
        if computer_guess < secret_number:
            print("Too low! Try again.")
            lower_limit = computer_guess + 1  # adjust limit for the next guess
        elif computer_guess > secret_number:
            print("Too high! Try again.")
            upper_limit = computer_guess - 1  # adjust limit for the next guess
        
        time.sleep(1)  # adds a delay between computer guesses
    
    # win
    print(f"Computer guessed the correct number {secret_number} in {guesses_count} guesses.")

mode = input("Choose the mode (user/computer): ").lower()

if mode == "user":
    user_mode()
elif mode == "computer":
    computer_mode()
else:
    print("Invalid mode. Please enter 'user' or 'computer'.")
