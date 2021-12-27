#!/usr/bin/python3.10
"""Key logger application"""

if __name__ == "__main__":
  import signal

  file = None

  def signalHandler(sig, frame):
    if file is not None:
      match sig:
        case signal.SIGINT:
          file.write("^C")
          raise SystemExit
        case signal.SIGQUIT:
          file.write("^\\")
          raise SystemExit
        case signal.SIGTSTP:
          file.write("^Z")
          raise SystemExit

  signal.signal(signal.SIGINT, signalHandler)
  signal.signal(signal.SIGQUIT, signalHandler)
  signal.signal(signal.SIGTSTP, signalHandler)

  with open("keylog.txt", "a") as file:
    #For each keystroke, append to file
    while True:
      file.write(f"{input()}\n")
