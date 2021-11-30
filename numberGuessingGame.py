
import random
import os
clear = lambda: os.system('clear')
clear()

#Function to play guessing game
def play_guessing_game():
  print("WELCOME TO THE NUMBER GUESSING GAMES!!! \n\nI'm thinking of a number between 1-100. \nPlease select a difficulty level for guessing the number")
  user_guess_difficulty = input("Choose a difficulty, type 'easy' or 'hard': \n")
  random_number = random.randrange(1,101,1)
  user_attempts_left = 0
  user_guess = 0
  number_guessed = False

  #print(f"Random number: {random_number}")

  if user_guess_difficulty == 'easy':
    user_attempts_left = 10
  elif user_guess_difficulty == 'hard':
    user_attempts_left = 5
  else:
    print("You didn't choose a proper answer.\n\n\n")
    play_guessing_game()

  while not number_guessed and user_attempts_left > 0:
    user_guess = int(input("Pick a number between 1 and 100: \n"))
    if user_guess == random_number:
      number_guessed = True
    elif user_guess < random_number:
      print("Too low")
      user_attempts_left -= 1
      print(f"You have {user_attempts_left} guesses left.")
    elif user_guess > random_number:
      print("Too high")
      user_attempts_left -= 1
      print(f"You have {user_attempts_left} guesses left.")


  if number_guessed == False:
    try_again = input("Sorry, you lost, try again? 'yes' or 'no' \n")
    if try_again == 'yes':
      clear()
      play_guessing_game()
    elif try_again == 'no':
      print("Better luck next time, Good Bye")
  elif number_guessed == True:
    print(f"Congratulations!!!!! You guessed the number {random_number}, you win!")

play_guessing_game()