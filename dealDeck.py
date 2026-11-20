import random
LIME = "\033[38;2;188;209;35m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

print(LIME+"Welcome to Kill Your Neighbor! "+RESET+"I'll be teaching you a card game and how to write some python code today.\n")
print("These messages are displayed via the "+YELLOW+"'print'"+RESET+", function, like "+YELLOW+"'print(\"Hello, World!\")\n"+RESET)
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"] #Define the 4 suits
FACES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #Define all faces
print(f"A "+BLUE+"'constant'"+RESET+" is a (usually capitalized) value defined once at the top that the program never changes, like suits and faces.\nExample: "+BLUE+"SUITS = [\"Hearts\", \"Diamonds\", \"Clubs\", \"Spades\"]"+RESET)

HAND_SIZE = 7 #Starting hands are always 7
LOSING_SCORE = 100 #Determine what ends the game
print("Hand size ("+BLUE+"7 per player"+RESET+") and the losing score ("+BLUE+"currently 100"+RESET+") are also both defined as "+BLUE+"constants"+RESET+".\n")
#With the above defined, the components necessary to build a deck are compiled

#Ask the questions that begin the process by assigning vital variables
print("This is an "+YELLOW+"'input'"+RESET+" function, used to collect data from users. That data is being assigned to a "+BLUE+"'variable'"+RESET+" called "+BLUE+"'numDecks'"+RESET+".")
numDecks = int(input(YELLOW+"How many decks are we using today? "+RESET)) 
    #My family believes more decks = more spice
print("This "+YELLOW+"'input'"+RESET+" function is for specifying how many CPU players. That data is being assigned to a "+BLUE+"'variable'"+RESET+" called "+BLUE+"'cpuCount'"+RESET+".")
cpuCount = int(input(YELLOW+"How many friends are we playing with? "+RESET))
    #Each new CPU is a new value in 'hands' that is defined later

deck = []   #create a variable to save the end result into memory
print("\nNow a set of '"+ YELLOW+"for loops"+RESET+"' build the deck. A "+ YELLOW+"loop"+RESET+" repeats the indented lines under it, once per item. Example:")
print(YELLOW+"for d in range(numDecks)"+RESET+":\n#for the number of 'd for decks' the player selects V\n    "+YELLOW+"for suit in SUITS"+RESET+":\n    #for each suit in the SUITS constant V\n        "+YELLOW+"for face in FACES"+RESET+":\n        #for each face in the FACES constant V")
print("The outer loop (range(numDecks)) repeats once per deck amount chosen, the middle loop once per suit, and the inner loop once per face.\n")
for d in range(numDecks):
    #check against the number of decks the player selects
    for suit in SUITS:
        #for each suit in the SUITS constant ->
        for face in FACES:
            #for each face in the FACES constant ->
            deck.append(face, suit)
            #iterate through the list to connect every face to every suit once
    deck.append(["Joker", "none"])
    deck.append(["Joker", "none"])    #INSIDE the deck loop, so every deck gets its own 2 jokers
print(f"Selected cards are then added to the deck with 'append'. Example: deck.append(face + \" of \" + suit)\n")
#The game comes with jokers for extra sauce. 50 points/5 cards each!

hands = [] #create the variable for player's hands
for n in range(cpuCount + 1): 
    #n is a throwaway variable only used in this loop, and the +1 will keep it iterating until all CPUs are dealt for
    hands.append([])    #add the number of CPU entities to the number of hands total

while len(hands[0]) < HAND_SIZE:
    #player 1 is position 0; while their hand is below the hand size, deal
    for hand in hands:  #We want a random card put in the hand and removed from the deck variable
        position = random.randint(0, len(deck) -1)  #picks a random card from what's left until HAND_SIZE is no longer greater
        card = deck.pop(position)   #removes the card from the deck as 'card'
        hand.append(card)   #puts it in player's hand
print("The CPU players have been dealt their cards.\n")

#Now we need to pick a starting card at random, and we have a lot of code already done from the deck creation
#No for loop is needed this time since we're only picking and assigning a single card
position = random.randint(0, len(deck) - 1)
startingCard = deck.pop(position)
startEffects = input("Should the starting card trigger its effect? (y/n) ").lower()
#This will determine if the first card has any authority or not


print(f"Starting card is: {startingCard[0]} of {startingCard[1]}") #0 is the face and 1 is the suit value
print("Your hand:")
for card in hands[0]:   #As player 0, this displays your hand as a list
    print(f"  {card[0]} of {card[1]}") #This had to be updated to include both variables that make up a card

#Let's assign each card a number so player doesn't have to type the whole thing out
currentPlay = input("What card would you like to play? ")

#Begin card assessment
if currentPlay == "Joker":
    card = hands.pop(position) #Remove the card from the player's hand
