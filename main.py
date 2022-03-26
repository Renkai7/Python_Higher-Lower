# Get random person
# -Generate random number
# --import random
# --create random number variable
# -Get list from Game data


import random
from replit import clear
from art import vs, logo
from game_data import data


def get_celebrity():
  random_num = random.randint(1, len(data))
  celebrity_data = data[random_num - 1]
  return celebrity_data
    
def game():
  celeb_1 = get_celebrity()
  celeb_2 = get_celebrity()
  score = 0
  game_over = False
  
  while game_over != True:
    # clear()
    print(celeb_1['follower_count'])
    print(celeb_2['follower_count'])
    
    print(logo)
    print(f"Compare A: {celeb_1['name']}, {celeb_1['description']}, from {celeb_1['country']}")
    print(vs)
    print(f"Against B: {celeb_2['name']}, {celeb_2['description']}, from {celeb_2['country']}")
  
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if guess == 'A':
      if celeb_1["follower_count"] > celeb_2["follower_count"]:
        # clear()
        score += 1
        print(f"correct! score: {score}")
        celeb_1 = celeb_2
        celeb_2 = get_celebrity()    
      else:
        print(f"nope! final score is: {score}")
        game_over = True
    elif guess == 'B':
      if celeb_1["follower_count"] < celeb_2["follower_count"]:
        # clear() 
        score += 1
        print(f"correct! score: {score}")
        celeb_1 = celeb_2
        celeb_2 = get_celebrity()              
      else:
        print(f"nope! final score is: {score}")
        game_over = True

    
game()