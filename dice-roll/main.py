#!/usr/bin/python3
"""Dice roll application"""

if __name__ == "__main__":
  import random

  print("How many dice?")

  while True:
    try:
      dice = int(input())
      break
    except ValueError:
      print("Input must be an integer")

  print("How many faces per die?")

  while True:
    try:
      faces = int(input())
      break
    except ValueError:
      print("Input must be an integer")

  for i in range(dice):
    print(f"Die #{i + 1}: {random.randrange(0, faces) + 1}")
