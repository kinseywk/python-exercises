#!/usr/bin/python3
"""Unit tests"""

from library import prompt
import unittest
import fcntl, termios
import os

def writeToStdin(bytes):
  path = f"/proc/{os.getpid()}/fd/0"
  with open(path, "w") as fd:
    for byte in f"{bytes}\n":
      fcntl.ioctl(fd, termios.TIOCSTI, byte)

class PromptTest(unittest.TestCase):
  def test_str(self):
    writeToStdin("foo")
    self.assertEqual(prompt("str: ", str), "foo")

  def test_int(self):
    writeToStdin("100")
    self.assertEqual(prompt("int: ", int), 100)

  def test_float(self):
    writeToStdin("1.0")
    self.assertEqual(prompt("float: ", float), 1.0)

  def test_bool(self):
    writeToStdin("False")
    self.assertEqual(prompt("bool: ", bool), False)

if __name__ == "__main__":
  unittest.main()