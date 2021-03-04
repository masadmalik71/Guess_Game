from replit import clear
import random




def game(number, attempts):
  game_countine = False
  while not game_countine:
    guessed_number = int(input(f"You have {attempts} remaining to guess the number.\nMake a guess: "))
    if guessed_number == number:
      print(f"You got it! The answer was :{number}")
      game_countine = True
    elif guessed_number > number:
      print("Too high.")
      attempts -= 1
      if attempts == 0:
          print("You lose.")
          game_countine = True
    elif guessed_number < number:
      print("Too Low.")
      attempts -= 1
      if attempts == 0:
          print("You lose.")
          game_countine = True





gamey = False
while not gamey:
  actual_number = random.randint(1,100)
  print("I'm thinking of a number between 1 and 100.")
  is_input_right = False
  while not is_input_right:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy' or level == 'e' or level == 'hard' or level == 'h':
      is_input_right = True
    elif level != 'easy' and level != 'e' and level != 'hard' and level != 'h':
      print("You enter the wrong input please type again.")


  if level == 'easy' or level == 'e':
    attempts = 10
    game(actual_number, attempts)
  elif level == 'hard' or level == 'h':
    attempts = 5
    game(actual_number, attempts)
  play_agai1 = False
  while not play_agai1:
    play_again = input("Want to play again? Type 'y' or 'n': ")
    if play_again == 'y':
      play_agai1 = True
      clear()
    elif play_again == 'n':
      clear()
      play_agai1 = True
      gamey = True
    elif play_again != 'y' and play_again != 'n':
      print("You entered the wrong key.")
    