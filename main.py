import random

def user_mode():
  ###

def computer_mode():
  ###

mode = input("Choose the mode (user/computer): ").lower()

if mode == "user":
    user_mode()
elif mode == "computer":
    computer_mode()
else:
    print("Invalid mode. Please enter 'user' or 'computer'.")
