import random

# SNAKE, WATER, GUN GAME

def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return True
        elif you == 'g':
            return False   
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False  
    elif comp == 'g':
        if you == 'w':
            return False
        elif you == 's':
            return True                       

print( "Computer's turn: Snake(s), water(w), Gun(g)")
randNo = random.randint(1,3)      # randint function produces random integers between the given limits .... it will either give 1,2 or 3 anything randomly
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'        


you = (input("Your turn: Snake(s), water(w), Gun(g)"))

a = game(comp,you)

print(f"The computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie")
elif a:  
    print("You win")
else:
    print("You Lose")  

