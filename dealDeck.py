import random
from settings import SUITS, FACES, HAND_SIZE, YELLOW, RESET, LIME, BLUE

print("These messages are displayed via the "+YELLOW+"'print'"+RESET+", function, like "+YELLOW+"'print(\"Hello, World!\")\n"+RESET)
print(f"A "+BLUE+"'constant'"+RESET+" is a (usually capitalized) value defined once at the top that the program never changes, like suits and faces.\nExample: "+BLUE+"SUITS = [\"Hearts\", \"Diamonds\", \"Clubs\", \"Spades\"]"+RESET)
print("Hand size ("+BLUE+"7 per player"+RESET+") and the losing score ("+BLUE+"currently 100"+RESET+") are also both defined as "+BLUE+"constants"+RESET+".\n")
#With the above defined, the components necessary to build a deck are compiled
def buildDeck(numDecks):
    deck = []   #create a variable to save the end result into memory
    print("\nNow a set of '"+ YELLOW+"for loops"+RESET+"' build the deck. A "+ YELLOW+"loop"+RESET+" repeats the indented lines under it, once per item. Example:")
    for d in range(numDecks):
        #check against the number of decks the player selects
        for suit in SUITS:
            #for each suit in the SUITS constant ->
            for face in FACES:
                #for each face in the FACES constant ->
                deck.append([face, suit])
                #iterate through the list to connect every face to every suit once
        print(f"Selected cards are then added to the deck with 'append'. Example: deck.append(face + \" of \" + suit)\n")
        #The game comes with jokers for extra sauce. 50 points/5 cards each!
        deck.append(["Joker", "none"])
        deck.append(["Joker", "none"])    #INSIDE the deck loop, so every deck gets its own 2 jokers
        return deck

print(YELLOW+"for d in range(numDecks)"+RESET+":\n#for the number of 'd for decks' the player selects V\n    "+YELLOW+"for suit in SUITS"+RESET+":\n    #for each suit in the SUITS constant V\n        "+YELLOW+"for face in FACES"+RESET+":\n        #for each face in the FACES constant V")
print("The outer loop (range(numDecks)) repeats once per deck amount chosen, the middle loop once per suit, and the inner loop once per face.\n")

def makeHands(playerCount):
    hands = [] #create the variable for player's hands
    for n in range(playerCount): 
        #n is a throwaway variable only used in this loop, and the +1 will keep it iterating until all CPUs are dealt for
        hands.append([])    #add the number of CPU entities to the number of hands total
    return hands

def dealHands(deck, hands):
    while len(hands[0]) < HAND_SIZE:
        #player 1 is position 0; while their hand is below the hand size, deal
        for hand in hands:  #We want a random card put in the hand and removed from the deck variable
            position = random.randint(0, len(deck) -1)  #picks a random card from what's left until HAND_SIZE is no longer greater
            card = deck.pop(position)   #removes the card from the deck as 'card'
            hand.append(card)   #puts it in player's hand
    print("The CPU players have been dealt their cards.\n")
    #dealHands doesn't return anything because it's just manupilating data, not creating it

def flipStartingCard(deck):
    #Now we need to pick a starting card at random, and we have a lot of code already done from the deck creation
    #No for loop is needed this time since we're only picking and assigning a single card
    position = random.randint(0, len(deck) - 1)
    return deck.pop(position)
    #buildDeck, makeHands and flipStartingCard create something, so they return something


def createGame(numDecks, cpuCount):
    deck = buildDeck(numDecks)
    hands = makeHands(cpuCount + 1)
    dealHands(deck, hands)
    startingCard = flipStartingCard(deck)
    return hands, deck, startingCard
    #createGame is the one that ties all of the functions together and returns all 3 retulst