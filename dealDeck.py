import random
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"] #Define the 4 suits
FACES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #Define all faces
HAND_SIZE = 7 #Starting hands are always 7
LOSING_SCORE = 100 #Determine what ends the game
#With the above defined, the components necessary to build a deck are compiled

numDecks = int(input("This is an input function, used to collect data from you. That data is being assigned to a variable called 'numDecks'.\n\nHow many decks are we using today?")) 
#My family believes more decks = more spice
cpuCount = int(input("How many friends are we playing with?"))

deck = []
#create a variable to save the end result into memory
for d in range(numDecks):
    #check against the number of decks the player selects
    for suit in SUITS:
        #for each suit in the SUITS constant ->
        for face in FACES:
            #for each face in the FACES constant ->
            deck.append(face + " of " + suit)
            #iterate through the list to connect every face to every suit once
    deck.append("Joker")
    deck.append("Joker")#These need to go INSIDE the for loop to properly connect to the deck being built
print("Cards are added to the deck via the 'append' function.")
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
