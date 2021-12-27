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
<<<<<<< HEAD
=======
  
>>>>>>> 248c513089097aefe964b760a5c19e4a6d1e6603
