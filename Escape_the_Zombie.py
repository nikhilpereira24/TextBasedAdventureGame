## -*- coding: utf-8 -*-
#"""
#Created on Fri Oct 27 16:18:04 2017
#
#@author: nikhil
#"""
#'This program is a textbased game called Escape the Zombies and it will consist of while loops'
'''“I have neither given nor received unauthorized assistance on this assignment.'''

def game_introduction():
    print("Escape the Zombies is a fun Halloween text-based game")
    print()
    print("It is dark outside and you are trapped on Elm Street,")
    print("Hungry zombies are lurking in the distance")
    print()
    print("You have three options...")
    print("Run to the scary house (1) Run down the street (2) or fight (3)")
    print("After this, you will be not know which number leads to which path!!")
    print("Guess Correctly and Good Luck!!!")
    print()
   
def list_of_Inputs():
    number_entered = []
    
    

def chooseOption():
    option = ''
    while option != '1' and option != '2' and option != '3':
        print("There is no time to waste,they're approaching! Enter 1,2 or 3 to go somewhere")
        option = input()
        
    return option

def checkOption(chosenOption):
    if chosenOption == '1':
        print("You enter the house and the zombies cant get you")
        print("The zombies bang on the door...Act quick!")
        return True
    
    elif chosenOption == '2':
        print("You trip and fall and the zombies eat you!")
        print("Game Over!")
        return False
    
        
    elif chosenOption == '3':
        print("Your weapon breaks and the zombies surround and eat you!")
        print("Game Over!")
        return False
        

def House(Option):
    
    if Option == "1":
            print("You run to the rooftop and a rescue helicopter finds you and you escape, you win!")
            return False
    elif Option == "2":
            print("Surprise you find a zombie and die!")
            print("Game Over")
            return False
    elif Option == "3":
            print("There is no service and the zombies crowd you and kill you")
            print("Game Over")
            return False
  
    

def runGame(playerAlive):      
    game_introduction()            
    while playerAlive:
        Option = chooseOption()   
        playerAlive = checkOption(Option)    
        if playerAlive:
                Option = chooseOption()
                playerAlive = House(Option)
                
playerAlive = True 
runGame(playerAlive)           
playAgain = 'yes'
while playAgain == 'yes':
    print('Do you want to play again? yes or no')
    playAgain = input()
    
    if playAgain == 'yes':
        playerAlive = True
        runGame(playerAlive)
        
    elif playAgain == 'no':
        print("The Game is over")
        playerAlive = False
    
    
    

 

            
            
        

    
    
    
    
    
    
   
        
        
        

