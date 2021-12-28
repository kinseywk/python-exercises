#!/usr/bin/python3.10
"""Dice roll application"""

if __name__ == "__main__":
  import pathlib
  import importlib.util
  
  spec = importlib.util.spec_from_file_location("library",f"{pathlib.Path(__file__).parent.parent.absolute()}/library-package/library.py")
  lib = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(lib)
  prompt = lib.prompt

  import random

  dice = prompt("How many dice?", int)
  faces = prompt("How many faces per die?", int)

  for i in range(dice):
    print(f"Die #{i + 1}: {random.randrange(0, faces) + 1}")
