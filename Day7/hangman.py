import random
from words import word_list

print("***HANGMAN GAME***")

# getting random word from word list
chosen_word = random.choice(word_list)
print(f"chosen word is: {chosen_word}")

display = []

game_on =True
# creating a list of "_" to match number of open spaces
for _ in range(len(chosen_word)):
  display += "_"

guessed = []

lives = 6
while(game_on):
  guess = input("Please guess a letter: ").lower()
  if guess in guessed:
    lives -= 1
    print(f"already guessed that letter please try again: {lives} remaining")
    guess = input("Please guess a letter: ").lower()
    
  guessed.append(guess)
  if guess not in chosen_word:
    lives -= 1
    print(f"guessed letter not in chosen word: {lives} remaining")
  
  for pos in range(len(chosen_word)):
    letter = chosen_word[pos]
    if letter == guess:
      display[pos] = letter
  print(display)
    
  if(lives == 0):
    game_on = False
  elif lives > 0 and "_" not in display:
    print("You Win")
    game_on=False

print("Game over")
