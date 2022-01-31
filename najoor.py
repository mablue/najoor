# Play Najoor and practice new words!

from random import choice

reset = "\u001b[0m"
green = "\u001b[0;32m"
red = "\u001b[0;31m"
yellow = "\u001b[1;33m"

word_list=[
  "cat",
  "class",
  "pen",
  "vajoor",
  "masoud",
  "car",
  "python",
]

random_word = list(choice(word_list))
rwlen=len(random_word)
player_guess  = ["_"]*rwlen
colored_player_guess = ["_"]*rwlen
print("".join(colored_player_guess))

while True:
  for i in range(rwlen):
    guess = input()
    for j in range(min(rwlen,len(guess))):
      character_color = red
      if random_word[j] == guess[j]:
        character_color = green
      elif guess[j] in random_word:
        character_color = yellow
      player_guess[j] = guess[j]
      colored_player_guess[j] = character_color+player_guess[j]+reset
     
    print("".join(colored_player_guess))
    if player_guess==random_word:
      exit()

    