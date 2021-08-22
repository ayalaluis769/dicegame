#Before

"""import random

high_score = 0


def dice_game():


dice_game()"""

"""Your Challenge:
Write the content of the body for the dicegame function so that it works
Entering a choice of 1 results in a pair of dice being "thrown". That is, two separate random integers from 1-6 are chosen. 
The result from each "roll" is shown to the player, along with the total. 
The total is also compared to the value of high_score. If it is higher than the high_score, then it is set as the new high score, and a message is shown.
The player can repeat option 1 as many times as they like. If they choose option 2, the game exits:
TIPS:
Use an infinite while loop, breaking out of the loop if the player chooses option "2". 
To include newlines in your print statements, you can use \n inside quotes. For example, the \n in this print statement creates a newline at the end of the text:
print("New high score!\n")
You will need to use what you learned about modifying global variables in local scope. """

#After

import random

high_score = 0

def dice_game():
        global high_score
        global first_dice
        global second_dice
        global score

        print("Current High score:", + high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")

    
        if choice == "1":
                first_dice = random.randint(1,6)
                print("You roll a... ", first_dice)
                second_dice = random.randint(1,6)
                print("You roll a... ", second_dice)
                score = (first_dice + second_dice)
                print("\nYou have rolled a total of: ", score)
                print("\nNew high score!")
        if choice == "2":
            print("Goodbye!")        
                
                    

dice_game()