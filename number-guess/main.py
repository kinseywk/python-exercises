#!/usr/bin/python3.10
"""Number guess application"""

if __name__ == "__main__":
  import pathlib
  import importlib.util
  
  spec = importlib.util.spec_from_file_location("library",f"{pathlib.Path(__file__).parent.parent.absolute()}/library-package/library.py")
  lib = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(lib)
  prompt = lib.prompt

  import random

  MIN = 1
  MAX = 100
  num = random.randrange(MIN, MAX)

  print(f"I'm thinking of a number between {MIN} and {MAX}. Can you guess it?")

  guesses = 0
  guess = None

  while True:
    guess = prompt(f"Guess #{guesses + 1}: ", int)
    guesses += 1

    if guess > num:
      print("Lower")
    elif guess < num:
      print("Higher")
    else:
      print(f"That's it! It only took you {guesses} guesses.")
      break
    
