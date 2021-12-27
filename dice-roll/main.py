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
      print
    print("How many faces per die?")

  while True:
    faces = int(input())

  for i in range(dice):
    print(f"Die #{i}: {random.randrange(1, faces)}")
