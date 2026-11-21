from settings import LIME, YELLOW, BLUE, RESET
import random

def cardName(card):
    #name the cards in your hand for when you refer to them in the game
    if card[0] == "Joker": #Jokers are the only different card, so it's all we need to check against
        return "Joker"
    return card[0] + " of "+ card[1]

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

def canPlay(card, top, currentSuit, penaltyFace):
    #needed a new function to stop asking for a play when there's an active penalty
    if penaltyFace != "":
        return card[0]
    return isLegal(card, top, currentSuit)

def hasLegalCard(hand, top, currentSuit):
    #Mainly used to check CPU hands each round to know if play is possible or whether to draw 1
    found = False
    for card in hand: 
        if isLegal(card, top, currentSuit):
            found = True
        return found

def drawCard(hand, deck):
    position = random.randint(0, len(deck) -1)
    #Draw a random card from a random place in the deck, and remove it (-1)
    hand.append(deck.pop(position))

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

        if hasLegalCard(hands[turn], top, currentSuit) == False:
            print(f"{who} can't play anything and draws a card.")
            drawCard(hands[turn], deck)
            #This block runs a check for a legal card in the currently playing hand each round

        elif turn == 0:
            print("Your turn. Your hand: ")
            displayHand(hands[0])
            chosen = 0
            validPlay = False
            while validPlay == False:
                try:
                    chosen = int(input("Which card number do you want to play? "))
                    if chosen < 1 or chosen > len(hands[0]):
                        print(f"Pick a number from 1 to {len(hands[0])}")
                        #The print needs to know to pick from the amount of hands that exist
                    elif isLegal(hands[0][chosen - 1], top, currentSuit) == False:
                        print(f"{cardName(hands[0][chosen - 1])} can't go on {cardName(top)}.")
                        #The print statement needs to update to whatever card was played
                    else:
                        validPlay = True
                except ValueError:
                    print("Enter the number to the next card.")
            card = hands[0].pop(chosen - 1)
            cardPlayed = True
        else:
            for i in range(len(hands[turn])):
                if cardPlayed == False and isLegal(hands[turn][i], top, currentSuit):
                    card = hands[turn].pop(i)
                    cardPlayed = True

        if cardPlayed: 
            lastPlayed.append(card)
            if card[0] != "Joker":
                currentSuit = card[1]
            print(f"{who} played {cardName(card)}. Cards left: {len(hands[turn])}")
            if len(hands[turn]) == 0:
                roundOver = True

        if roundOver == False:
            turn = (turn + direction) % playerCount

    print(f"\nROUND OVER! {who} ran out of cards.")