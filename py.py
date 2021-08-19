# bazi


#import pdb
#pdb.set_trace()
from pyfiglet import figlet_format as f_form

from termcolor2 import colored

print(colored(f_form("Erfani"), "green"))


print(colored("sang...." ,"blue"))
print(colored("kaghaz....", "magenta"))
print(colored("gheychi....", "blue"))

gameRaund = int(input("How many raund do you want to play?"))

user1_Scor = 0
user2_Scor = 0



while user1_Scor < gameRaund and user2_Scor < gameRaund:
    import random
    randomChoose = random.randint(0, 2)
    #user2 = "h"
    if randomChoose == 0:
        randomChoose = "sang"
    elif randomChoose == 1:
        randomChoose = "kaghaz"
    elif randomChoose == 2:
        randomChoose = "gheychi"

    user1 = input("which one? sang, kaghaz or gheychi?")
    print(user1)

    if user1 == "q":
        break
    elif user1 == randomChoose:
        print(colored(f_form("No one wins!"), "yellow"))
    elif user1 == "sang":
        if randomChoose == "kaghaz":
            print(colored(f_form("user 2 wins"), "red"))
            user2_Scor += 1
        elif randomChoose == "gheychi":
            print(colored(f_form("user 1 wins"), "green"))
            user1_Scor += 1

    elif user1 == "kaghaz":
        if randomChoose == "sang":
            print(colored(f_form("user 1 wins"), "green"))
            user1_Scor += 1
        elif randomChoose == "gheychi":
            print(colored(f_form("user 2 wins"), "red"))
            user2_Scor += 1
    elif user1 == "gheychi":
        if randomChoose == "sang":
            print(colored(f_form("user 2 wins"), "red"))
            user2_Scor += 1
        elif randomChoose == "kaghaz":
            print(colored(f_form("user 1 wins"), "green")) 
            user1_Scor += 1
    else: 
        print(colored(f_form("Some thing went wrong!"), "yellow"))
    print(f"User1 choosed {user1} and user2 choosed {randomChoose}")



print(colored(f_form("Game finished!"), "yellow"))

if user1_Scor == gameRaund and gameRaund != 0:
    print(colored(f_form("you win!"), "green"))
elif user2_Scor == gameRaund and gameRaund != 0:
    print(colored(f_form("Camputer wins!"), "red"))
else:
    print(colored(f_form("No one wins!"), "yellow"))

