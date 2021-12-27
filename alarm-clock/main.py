#!/usr/bin/python3
"""Alarm clock application"""

if __name__ == "__main__":
  import time
  print("How many seconds to wait?")
  wait = int(input())
  time.sleep(wait)
  print("Time's up!")
  