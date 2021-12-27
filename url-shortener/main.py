#!/usr/bin/python3

print("Inroduzca una URL, por favor")
url = input()

print(f"Aquí está tu URL: http://fake-url-shortening-service.com/{hash(url)}")