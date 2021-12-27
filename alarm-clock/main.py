#!/usr/bin/python3
"""Alarm clock application"""

if __name__ == "__main__":
  import time

  print("How many seconds to wait?")
  while True:
    try:
      wait = int(input())
      break
    except ValueError:
      print("Input must be an integer")

  time.sleep(wait)
  print("Time's up!")
