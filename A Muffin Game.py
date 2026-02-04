import time
import random
import sys
import threading
import select

def slow_print(text, speed=0.03, newline=True):
    for char in text:
        sys.stdout.write(char)  
        sys.stdout.flush()      
        time.sleep(speed)       
    if newline:
        print() 
weights = [6, 7, 6, 5, 1]

foodGrades = [
  "perfect",
  "good",
  "odd",
  "bad",
  "in the face of Jeffery Epstein",
]

foodGrade = random.choices(foodGrades, weights=weights, k=1)[0]

prod = [
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

side_effect = [
  "Extreme denial",
  "Scary hallucinations of Mickey Mouse",
  "God in all of his true glory shining down upon you and yours",
  "Sudden urges to visit Epstein island",
  "Makes you believe Diddy is behind you at all times",
  "becoming a muffin",
  "getting trapped in a Vietnam war flashback",
  "controllable laughter",
  "privilege of killing every single human on the planet."
]

deliveryEvents = [
  "you realize you forgot to put the food in the van and have to go back to your cafe to get it.",
  "you get into a car accident and have to go to the hospital.",
  "you think you see a celebrity on the street and stop to take a picture, but it turns out to be a homeless person and they steal your food.",
  "Your GPS tells you to 'go f*ck yourself' you decide that maybe Temu was not a good place to buy phones.",
  "paranormal activity occurs right in front of your car, and you begin to question your sanity, but then you realize that the paranormal activity is actually just a glitch in the matrix and you are able to escape it unharmed.",
  "your favorite song comes on the radio and then you somehow think youre in a plane and theres autopiolot but there is not and you crash into a tree. After you wake up, you find yourself in Narnia with the food so you decide to open a cafe there.",
  "you get a flat tire and have to change it, but then you realize you dont know how to change a tire and you end up getting hit by a car while trying to figure it out.",
  "you randomly teleport to the customers house and deliver the food, and end up getting a 5 star review!",
  ""
]

def fight():
  c_hp = 100
  hp = 100
  slow_print(f"CoNgLoMeRaTe HP = {c_hp}")
  slow_print(f"Your HP = {hp}")
  slow_print("You have 3 options: \n1. Pummel \n2. Dropkick \n3. Needle")
  while c_hp > 0 and hp > 0:
    choice = input("Choose an option (1-3): ")
    if choice == "1":
      damage = random.randint(15, 50)
      for rounds in range(10):
        time.sleep(0.1)
        print("HIT")
      c_hp -= damage
      slow_print(f"You pummel the conglomerate for {damage} damage!")
    elif choice == "2":
      damage = random.randint(15, 60)
      c_hp -= damage
      slow_print(f"You dropkick the conglomerate for {damage} damage!")
    elif choice == "3":
      damage = random.randint(15, 50)
      c_hp -= damage
      slow_print(f"You needle the conglomerate for {damage} damage!")
      hp += random.randint(5, 15)
    else:
      slow_print("Invalid option. Please choose a number between 1 and 3.")
      continue
    if c_hp > 0:
      c_damage = random.randint(10, 30)
      c_hp += random.randint(5, 15)
      slow_print(f"Conglomerate used H3x0r! it deals {c_damage} damage to you but heals itself for {random.randint(5, 15)} HP!")
    if c_hp <= 0:
      slow_print("You defeated the conglomerate! Congratulations!")
      break
      
    if hp <= 0:
      slow_print("You died. But hey, guess what! you died")
      break
    
    # Conglomerate's turn to attack
    c_damage = random.randint(10, 20)
    hp -= c_damage
    slow_print(f"The conglomerate attacks you for {c_damage} damage!")
    advertisement()
    
    if hp <= 0:
      slow_print("You were defeated by the conglomerate. Better luck next time!")
      break
  
  start_of_game()

def advertisement():
  print("=======================================\n MANDITORY BAKERY ADVERTISEMENT BREAK \n========================================")
  slow_print(f"Introducing {random.choice(prod)}!")
  slow_print(f"{random.choice(slogan)}")
  slow_print(f"Side Effects May Include: {random.choice(side_effect)} and {random.choice(side_effect)}")

def start_of_game():
  slow_print("Welcome to The Muffin Game!")
  time.sleep(2)
  slow_print("Here, you run a cafe")
  time.sleep(2)
  print()
  advertisement()
  time.sleep(2)
  print()
  time.sleep(1)
  slow_print("These are your options:")
  options = input("\n1. Bake Muffins\n2. Bake Cupcakes\n3. Bake Cookies\n4. Bake a Cake\n5. Bake a Pie\n6. Bake some Bread\n7. Dan\n8.Deliver Food\n Choose an option (1-9): ")
  
  if options == "1":
    bake_muffins(foodGrade)

  elif options == "2":
    bake_cupcakes(foodGrade)

  elif options == "3":
    bake_cookies(foodGrade)

  elif options == "4":
    bake_cake(foodGrade)

  elif options == "5":
    bake_pie(foodGrade)

  elif options == "6":
    bake_bread(foodGrade)

  elif options == "7":
    dan(foodGrade)

  elif options == "8":
    deliver_food()
  elif options == "9":
    fight()
  else:
    slow_print("Invalid option. Please choose a number between 1 and 9.")
    start_of_game()

def bake_muffins(foodGrade):
  slow_print("Mixing Batter...")
  time.sleep(1)
  slow_print("Putting muffins in oven...")
  time.sleep(2)
  slow_print(f"Your muffins came out {foodGrade}!")
  time.sleep(2)
  advertisement()



def bake_cupcakes(foodGrade):
  slow_print("Mixing Batter...")
  time.sleep(1)
  slow_print("Putting cupcakes in oven...")
  time.sleep(2)
  slow_print(f"Your cupcakes came out {foodGrade}!")
  time.sleep(2)
  advertisement()



def bake_cookies(foodGrade):
  slow_print("Mixing Batter...")
  time.sleep(1)
  slow_print("Putting cookies in oven...")
  time.sleep(2)
  slow_print(f"Your cookies came out {foodGrade}!")
  time.sleep(2)
  advertisement()


def bake_cake(foodGrade):
  slow_print("Mixing Batter...")
  time.sleep(1)
  slow_print("Putting cake in oven...")
  time.sleep(2)
  slow_print(f"Your cake came out {foodGrade}!")
  time.sleep(2)
  advertisement()


def bake_pie(foodGrade):
  slow_print("Mixing Batter...")
  time.sleep(1)
  slow_print("Putting pie in oven...")
  time.sleep(2)
  slow_print(f"Your pie came out {foodGrade}!")
  time.sleep(2)
  advertisement()


def bake_bread(foodGrade):
  slow_print("Mixing Batter...")
  time.sleep(1)
  slow_print("Putting bread in oven...")
  time.sleep(2)
  slow_print(f"Your bread came out {foodGrade}!")
  time.sleep(2)
  advertisement()


def dan(foodGrade):
  slow_print("In this game, your name is dan!")
  time.sleep(2)
  slow_print("You put yourself in the oven...")
  slow_print(f"And your dan came out {foodGrade}!")
  time.sleep(2)
  slow_print(f"Dan says: 'thank you for giving me life.'")
  slow_print(f"Dan leaves the bakery, to 'pursue true glory'")
  advertisement()


def deliver_food():
  slow_print("you get in your delivery van and start driving to your customer's house...")
  time.sleep(2)
  slow_print(f"But then, {random.choice(deliveryEvents)}")
  time.sleep(2)
  advertisement()


if __name__ == "__main__":
  start_of_game()