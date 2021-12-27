#!/usr/bin/python3
"""Key logger application"""

if __name__ == "__main__":
  import signal

  FILE = None

  def signalHandler(sig, frame):
    if file is not None:
      keystroke = ""
      if sig == signal.SIGINT:
        keystroke = "^C"
      elif sig == signal.SIGQUIT:
        keystroke = "^\\"
      elif sig == signal.SIGTSTP:
        keystroke = "^Z"
      file.write(keystroke)

  signal.signal(signal.SIGINT, signalHandler)
  signal.signal(signal.SIGQUIT, signalHandler)
  signal.signal(signal.SIGTSTP, signalHandler)

  try:
    file = open("keylog.txt", "a")
    #For each keystroke, append to file
    while True:
      file.write(f"{input()}\n")
  finally:
    file.close()
