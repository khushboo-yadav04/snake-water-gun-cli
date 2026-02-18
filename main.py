import random
from colorama import Fore, Style, init
# This line imports specific features from the colorama library, which is used to print colored text in the terminal.

init()

print("="*40)
print(Fore.CYAN + "🐍 SNAKE WATER GUN GAME 🔫" + Style.RESET_ALL)
print("="*40)

youDict = {"s": 1, "w" : -1,"g":0}
reversedDict = {1:"Snake 🐍" , -1:"Water 💧", 0: "Gun 🔫"}

user_score = 0
comp_score = 0

for i in range(5):
    print(f"\n 🎯Round {i+1}")

    computer = random.choice([-1,1,0])
    youstr = input("Enter your choice (s/w/g): ")

    if youstr not in youDict:
        print("Invalid choice ❌")
        continue

    you = youDict[youstr]

    print(f"You chose {reversedDict[you]}")
    print(f"Computer chose {reversedDict[computer]}")


    if(computer == you):
       print(Fore.YELLOW + "It's a draw 🤝"+ Style.RESET_ALL)

    elif (you == 1 and computer == -1) or \
         (you == -1 and computer == 0) or \
         (you == 0 and computer == 1):
        print(Fore.GREEN + "You Win 🎉" + Style.RESET_ALL)
        user_score += 1

    else:
        print(Fore.RED + "Computer Wins 💻" + Style.RESET_ALL)
        comp_score += 1

print("\n" + "="*40)
print(f"\nFinal Score: You {user_score} - {comp_score} Computer")
print("="*40)

# the below logic is written on the basic of the value of computer minus you
# if((computer - you)== -1 or (computer - you)== 2)
# print("You lose")
# else:
# print("You win!!!")