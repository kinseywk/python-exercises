#!/usr/bin/python3
import io

file = None

try:
  file = open("keylog.txt", "a")
  #For each keystroke, append to file
  while True:
    file.write(f"{input()}\n")
except:
  pass
finally:
  file.close()