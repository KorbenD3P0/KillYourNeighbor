from settings import LIME, YELLOW, BLUE, RESET
import random

def cardName(card):
    #name the cards in your hand for when you refer to them in the game
    if card[0] == "Joker": #Jokers are the only different card, so it's all we need to check against
        return "Joker"
    return card[0] + "of "+ card[1]

def displayHand(hand):
    for h in range(len(hand)):
    #for each individual card h/hand from beginning to end, in order, from data source 'hand'
        print(f" {h + 1}. {cardName(hand[h])}")

def isLegal(card, top, currentSuit):
    #check if the card beign played is legal
    if card[0] == "J" or card[0] == "Joker":
        #card[0] is the 'face' part of the card, not the player
        return True
    if card [1] == currentSuit or card [0] == top[0]:
        #card[1] is the suit, top[0] is the last face played, since a match is legal
        return True
    return False#If no matches, not a legal card/PageLayout:

def runGame(hands, deck, startingCard, cpuCount, startEffects):
    playerCount = cpuCount + 1
    lastPlayed = [startingCard]       # the pile; the top card is lastPlayed[-1]
    currentSuit = startingCard[1]     # the suit a play must match (a Jack will change it)
    turn = random.randint(0, cpuCount)    # 0 is player, 1 and up are CPUs
    direction = 1                     # a King will flip this to -1
    roundOver = False                 # tracks the game status

    print(f"Starting card is: {startingCard[0]} of {startingCard[1]}") #0 is the face and 1 is the suit value
    while roundOver == False:
        top = lastPlayed[-1] #tell the program that the last card played (-1) is the card to remember 
        print(f"\nTop Card: {top[0]} of {top[1]}") #0 is face, 1 is suit
        if turn == 0:
            who = "You"
        else:
            who= f"CPU {turn}"

        cardPlayed = False
        card = None

        #The card being played needs to be legal, function to check needs written, along with if the cpu has any legal cards in hand
        print("Your turn. Your hand: ")
        displayHand(hands[0])

    for card in hands[0]:   #As player 0, this displays your hand as a list
        print(f"  {card[0]} of {card[1]}") #This had to be updated to include both variables that make up a card

    #Let's assign each card a number so player doesn't have to type the whole thing out
    currentPlay = input("What card would you like to play? ")

