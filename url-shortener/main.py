#!/usr/bin/python3
"""URL shortener application"""
import base64

if __name__ == "__main__":
  print("Inroduzca una URL, por favor")
  url = input()
  short = base64.b64encode(bytes(str(hash(url)), "utf-8")).decode("utf-8")

  print(f"Aquí está tu URL: https://fake.site/{short}")
  
