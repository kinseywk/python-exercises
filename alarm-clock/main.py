#!/usr/bin/python3.10
"""Alarm clock application"""

if __name__ == "__main__":
  import pathlib
  import importlib.util
  
  spec = importlib.util.spec_from_file_location("library",f"{pathlib.Path(__file__).parent.parent.absolute()}/library-package/library.py")
  lib = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(lib)
  prompt = lib.prompt

  import time

  time.sleep(prompt("How many seconds to wait?", int))
  print("Time's up!")
