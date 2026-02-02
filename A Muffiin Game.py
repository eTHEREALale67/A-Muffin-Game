import time
import random
import sys

from requests import options

def slow_print(text, speed=0.05, newline=True):
    for char in text:
        sys.stdout.write(char)  
        sys.stdout.flush()      
        time.sleep(speed)       
    if newline:
        print() 

prod = [
  "seeb",
  "Oprah Winfrey",
  "Gu-Gu-Gu",
  "Degraded Versions",
  "Denial",
  "Mickey Mouse's Pants",
  "God",
  "Jeffrey Epstein",
  "Donald Drump",
  "Satan",
  "'berries'",
  "Vietnam"
  ]
slogan = [
  "sample text",
  "Absolutely not 'bees' backwards",
  "not illegal, we prefer 'legally distinct'",
  "Hey, isn't this product supposed to be in jail?",
  "Your mother is a prostitute unless you buy this product"
]

def start_of_game():
  slow_print("Welcome to The Muffin Game!")
  time.sleep(2)
  slow_print("In this game, you run a cafe")
  time.sleep(2)
  slow_print("Why are you still here dude play the damn game")
  time.sleep(2)
  slow_print("Theese are your options: ", newline=False)
  options = input("1. Bake Muffins\n2. Bake Cupcakes\n3. Bake Cookies\n\n4. Bake a Cake\n5. Bake a Pie\n6. Bake some Bread\n7. Dan\n8.Deliver Food/n Choose an option (1-8): ")
  if options == "1":
    bake_muffins()

  elif options == "2":
    bake_cupcakes()

  elif options == "3":
    bake_cookies()

  elif options == "4":
    bake_cake()

  elif options == "5":
    bake_pie()

  elif options == "6":
    bake_bread()

  elif options == "7":
    dan()

  elif options == "8":
    deliver_food()

  else:
    slow_print("Invalid option. Please choose a number between 1 and 8.")
    start_of_game()

def bake_muffins():
  pass

def bake_cupcakes():
  pass

def bake_cookies():
  pass

def bake_cake():
  pass

def bake_pie():
  pass

def bake_bread():
  pass

def dan():
  pass

def deliver_food():
  pass