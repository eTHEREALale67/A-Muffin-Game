import time
import random
import sys
import threading
import select

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

side_effect = [
  "Causes extreme denial",
  "Scary hallucinations of Mickey Mouse",
  ""
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
  quality = baking_slider_minigame("Muffins", difficulty=1)
  slow_print(f"You baked muffins with {quality}% quality!")
  start_of_game()

def bake_cupcakes():
  quality = baking_slider_minigame("Cupcakes", difficulty=2)
  slow_print(f"You baked cupcakes with {quality}% quality!")
  start_of_game()

def bake_cookies():
  quality = baking_slider_minigame("Cookies", difficulty=2)
  slow_print(f"You baked cookies with {quality}% quality!")
  start_of_game()

def bake_cake():
  quality = baking_slider_minigame("Cake", difficulty=2)
  slow_print(f"You baked a cake with {quality}% quality!")
  start_of_game()

def bake_pie():
  quality = baking_slider_minigame("Pie", difficulty=3)
  slow_print(f"You baked a pie with {quality}% quality!")
  start_of_game()

def bake_bread():
  quality = baking_slider_minigame("Bread", difficulty=1)
  slow_print(f"You baked bread with {quality}% quality!")
  start_of_game()

def dan():
  pass

def deliver_food():
  pass

def baking_slider_minigame(recipe_name, difficulty=1):
  """
  A timing-based slider minigame for baking.
  
  Args:
    recipe_name: The name of the recipe being baked
    difficulty: 1-3, affects slider speed and target zone size
  
  Returns:
    Quality score (0-100)
  """
  slow_print(f"\n🍰 Baking {recipe_name}! Use the slider minigame to get it perfect!")
  time.sleep(1)
  
  # Difficulty settings
  difficulty_settings = {
    1: {"speed": 0.02, "target_width": 15, "time_limit": 8},
    2: {"speed": 0.015, "target_width": 10, "time_limit": 6},
    3: {"speed": 0.01, "target_width": 8, "time_limit": 4}
  }
  
  settings = difficulty_settings.get(difficulty, difficulty_settings[1])
  slider_width = 50
  target_pos = random.randint(10, slider_width - settings["target_width"])
  
  slow_print(f"Difficulty: {'Easy' if difficulty == 1 else 'Medium' if difficulty == 2 else 'Hard'}")
  slow_print(f"Press SPACE when the slider enters the target zone (marked with |)")
  time.sleep(2)
  
  # Display initial state
  print("\n" + display_slider(0, slider_width, target_pos, settings["target_width"]))
  
  slider_pos = 0
  direction = 1
  start_time = time.time()
  pressed = False
  
  # Main game loop
  while True:
    elapsed = time.time() - start_time
    
    if elapsed > settings["time_limit"]:
      slow_print("\nTime's up!")
      break
    
    # Update slider position
    slider_pos += direction * settings["speed"] * 100
    
    # Bounce slider back and forth
    if slider_pos >= slider_width - 1:
      direction = -1
    elif slider_pos <= 0:
      direction = 1
    
    # Display slider
    print("\r" + display_slider(int(slider_pos), slider_width, target_pos, settings["target_width"]), end="", flush=True)
    
    # Check for user input (non-blocking)
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
      user_input = sys.stdin.read(1)
      if user_input == ' ':
        pressed = True
        break
    
    time.sleep(0.05)
  
  print()  # New line after slider
  
  # Calculate quality based on where slider stopped
  if pressed:
    distance_from_target = abs(slider_pos - (target_pos + settings["target_width"] / 2))
    if distance_from_target < settings["target_width"] / 2:
      quality = max(80, 100 - int(distance_from_target * 2))
      slow_print(f"Perfect! 🎯 Quality: {quality}")
    elif distance_from_target < settings["target_width"]:
      quality = max(50, 80 - int(distance_from_target * 2))
      slow_print(f"Good! Quality: {quality}")
    else:
      quality = max(20, 50 - int(distance_from_target))
      slow_print(f"Okay, could be better. Quality: {quality}")
  else:
    quality = random.randint(10, 40)
    slow_print(f"You ran out of time! Quality: {quality}")
  
  time.sleep(1)
  return quality

def display_slider(current_pos, width, target_start, target_width):
  """Display the slider with target zone"""
  slider = ['─'] * width
  target_end = target_start + target_width
  
  # Mark target zone
  for i in range(target_start, min(target_end, width)):
    slider[i] = '█'
  
  # Place current slider position
  if 0 <= current_pos < width:
    slider[int(current_pos)] = '●'
  
  return "[" + "".join(slider) + "]"
start_of_game()