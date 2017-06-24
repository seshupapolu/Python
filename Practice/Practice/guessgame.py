import random

def start_game():
    print("Guess the number between 1 and 100")
    secret = random.randint(1,100)
    while True:
         number = int(input())
         if number == secret:
            print("You won!!!")
            break
         elif number > secret:
            print("Higher")
         elif number < secret:
            print("lower")

print("Game Started!")
start_game()