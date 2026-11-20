from settings import LIME, YELLOW, BLUE, RESET
from dealDeck import flipStartingCard
import random

def runGame(hands, deck, startingCard, cpuCount, startEffects):
    playerCount = cpuCount + 1
    lastPlayed = [startingCard]       # the pile; the top card is lastPlayed[-1]
    currentSuit = startingCard[1]     # the suit a play must match (a Jack will change it)
    turn = random.randint(0, cpuCount)    # 0 is player, 1 and up are CPUs
    direction = 1                     # a King will flip this to -1
    roundOver = False                 # tracks the game status

    while not roundOver:
        top = lastPlayed[-1] #tell the program that the last card played (-1) is the card to remember 
        print(f"\nTop Card: {top[0]} of {top[1]}") #0 is face, 1 is suit
        
    print("Your hand:")
    for card in hands[0]:   #As player 0, this displays your hand as a list
        print(f"  {card[0]} of {card[1]}") #This had to be updated to include both variables that make up a card

    #Let's assign each card a number so player doesn't have to type the whole thing out
    currentPlay = input("What card would you like to play? ")

