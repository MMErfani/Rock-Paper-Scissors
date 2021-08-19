# game

#first install these modules \/ \/

from pyfiglet import figlet_format as f_form

from termcolor2 import colored


print(colored("Rock...." ,"blue"))
print(colored("Paper....", "magenta"))
print(colored("Scissors....", "blue"))

gameRaund = int(input("What would you like the final score to be?"))

user1_Scor = 0
user2_Scor = 0



while user1_Scor < gameRaund and user2_Scor < gameRaund:
    import random
    randomChoose = random.randint(0, 2)
    
    if randomChoose == 0:
        randomChoose = "ROCK"
    elif randomChoose == 1:
        randomChoose = "PAPER"
    elif randomChoose == 2:
        randomChoose = "SCISSORS"

    user1 = str(input("which one? Rock, Paper or Scissors?"))
    print(user1)

    if user1 == "Q":
        break
    elif user1.upper() == randomChoose:
        print(colored(f_form("No one wins!"), "yellow"))
    elif user1.upper() == "ROCK":
        if randomChoose == "PAPER":
            print(colored(f_form("Camputer wins"), "red"))
            user2_Scor += 1
        elif randomChoose == "SCISSORS":
            print(colored(f_form("You win"), "green"))
            user1_Scor += 1

    elif user1.upper() == "PAPER":
        if randomChoose == "ROCK":
            print(colored(f_form("You win"), "green"))
            user1_Scor += 1
        elif randomChoose == "SCISSORS":
            print(colored(f_form("Camputer wins"), "red"))
            user2_Scor += 1
    elif user1.upper() == "SCISSORS":
        if randomChoose == "ROCK":
            print(colored(f_form("Camputer wins"), "red"))
            user2_Scor += 1
        elif randomChoose == "PAPER":
            print(colored(f_form("You win"), "green")) 
            user1_Scor += 1
    else: 
        print(colored(f_form("Some thing went wrong!"), "yellow"))
    print(f"Because you choosed {user1} and camputer choosed {randomChoose}")



print(colored(f_form("Game finished!"), "yellow"))

if user1_Scor == gameRaund and gameRaund != 0:
    print(colored(f_form("you win!"), "green"))
elif user2_Scor == gameRaund and gameRaund != 0:
    print(colored(f_form("Camputer wins!"), "red"))
else:
    print(colored(f_form("No one wins!"), "yellow"))


print(colored(f_form("Our Github & Gitlab \/ \/"), "green"))

print(colored("https://github.com/MohammadMehdiErfani   &   https://gitlab.com/MohammadMehdiErfani", "blue"))