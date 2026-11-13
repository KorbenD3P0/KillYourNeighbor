import random
LIME = "\033[38;2;188;209;35m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
print(LIME+"Welcome to Kill Your Neighbor! "+RESET+"I'll be teaching you a card game and how to write some python code today.")
print("These messages are displayed via the "+YELLOW+"'print'"+RESET+", function, like 'print(\"Hello, World!\")\n")
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"] #Define the 4 suits
FACES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #Define all faces
print(f"A "+BLUE+"'constant'"+RESET+" is a value defined once at the top that the program never changes, like suits and faces.\nExample: "+BLUE+"SUITS = [\"Hearts\", \"Diamonds\", \"Clubs\", \"Spades\"]"+RESET)
HAND_SIZE = 7 #Starting hands are always 7
LOSING_SCORE = 100 #Determine what ends the game
print("Hand size ("+BLUE+"7 per player"+RESET+") and the losing score ("+BLUE+"currently 100"+RESET+") are also both defined as "+BLUE+"variables"+RESET+".\n")
#With the above defined, the components necessary to build a deck are compiled

numDecks = int(input("This is an "+YELLOW+"'input'"+RESET+" function, used to collect data from users. That data is being assigned to a variable called "+BLUE+"'numDecks'"+RESET+".\n\n"+YELLOW+"How many decks are we using today? "+RESET)) 
#My family believes more decks = more spice
cpuCount = int(input(YELLOW+"How many friends are we playing with? "+RESET))
#Each new CPU is a new value in 'hands' that is defined later

deck = []
#create a variable to save the end result into memory
print("\nNow a "+ YELLOW+"for"+RESET+" loop builds the deck. A loop repeats the indented lines under it, once per item. Example:")
print("for d in range(numDecks):\n#check against the number of decks the player selects\n    for suit in SUITS:\n    #for each suit in the SUITS constant ->\n        for face in FACES:\n        #for each face in the FACES constant ->")
print("The outer loop (range(numDecks)) repeats once per deck amount chosen, the middle loop once per suit, and the inner loop once per face.\n")
for d in range(numDecks):
    #check against the number of decks the player selects
    for suit in SUITS:
        #for each suit in the SUITS constant ->
        for face in FACES:
            #for each face in the FACES constant ->
            deck.append(face + " of " + suit)
            #iterate through the list to connect every face to every suit once
    deck.append("Joker")
    deck.append("Joker") #INSIDE the deck loop, so every deck gets its own 2 jokers
print(f"Selected cards are then added to the deck with 'append'. Example: deck.append(face + \" of \" + suit)\n\nThe deck now has {len(deck)} cards.\n")
#My game comes with jokers for extra sauce

hands = [] #create the variable for player's hands
for n in range(cpuCount + 1): 
    #n is a throwaway variable only used in this loop, and the +1 will keep it iterating until all CPUs are dealt for
    hands.append([]) #add the number of CPU entities to the number of hands total

while len(hands[0]) < HAND_SIZE:
    #player 1 is position 0; while their hand is below the hand size, deal
    for hand in hands: #We want a random card put in the hand and removed from the deck variable
        position = random.randint(0, len(deck) -1) #picks a random card from what's left until HAND_SIZE is no longer greater
        card = deck.pop(position) #removes the card from the deck as 'card'
        hand.append(card) #puts it in player's hand
print("Your hand:", hands[0])
#As player 0, this displays your hand as a list
print("Cards left:", len(deck))

