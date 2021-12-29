#!/usr/bin/python3
"""Make a window with a button that counts how many times it has been clicked
@dependency Tk
@dependency tkinter"""

if __name__ == "__main__":
  from tkinter import *

  root = Tk()

  class Window(Frame):
    def __init__(self, master=None):
      Frame.__init__(self, master)
      self.master = master

      self.pack(fill=BOTH, expand=1)

      self.clickCount = 0

      button = Button(self, text="Click me!", command=self.clickButton)
      button.place(x=0, y=0)

    def clickButton(self):
      self.clickCount += 1
      root.wm_title(f"You've clicked the button {self.clickCount} times!")

  app = Window(root)
  
  root.wm_title("Click the button!")
  root.geometry("400x300")
  root.mainloop()