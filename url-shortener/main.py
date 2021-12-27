#!/usr/bin/python3
"""URL shortener application"""

if __name__ == "__main__":
  print("Inroduzca una URL, por favor")
  url = input()

  print(f"Aquí está tu URL: http://fake-url-shortening-service.com/{hash(url)}")