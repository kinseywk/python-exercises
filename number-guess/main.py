#!/usr/bin/python3
"""Number guess application"""

if __name__ == "__main__":
  import random

  min = 1
  max = 100
  num = random.randrange(min, max)

  print(f"I'm thinking of a number between {min} and {max}. Can you guess it?")

  guesses = 0
  guess = None

  while True:
    guess = int(input())
    guesses += 1
    
    if guess > num:
      print("Lower")
    elif guess < num:
      print("Higher")
    else:
      print(f"That's it! It only took you {guesses} guesses.")
      break
    