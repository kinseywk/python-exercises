#!/usr/bin/python3
"""Dice roll application"""

if __name__ == "__main__":
  import random

  print("How many dice?")
  dice = int(input())
  print("How many faces per die?")
  faces = int(input())
  for i in range(dice):
    print(f"Die #{i}: {random.randrange(1, faces)}")
