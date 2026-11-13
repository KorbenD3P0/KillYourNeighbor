SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"] #Define the 4 suits
FACES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #Define all faces
HAND_SIZE = 7 #Starting hands are always 7
LOSING_SCORE = 100 #Determine what ends the game
#With the above defined, the components necessary to build a deck are compiled

def buildDeck():
    #plainly state what the function will handle
    deck = []
    #create a variable to save the end result into memory
    for suit in SUITS:
        #for each suit in the SUITS constant ->
        for face in FACES:
            #for each face in the FACES constant ->
            deck.append(face + " of " + suit)
            #iterate through the list to connect every face to every suit once
    deck.append("Joker")
    deck.append("Joker")
    #My game comes with jokers for extra sauce
    print({["Clubs"]deck})
    #I want to print all assigned items in a specific suit, but this may be more complicated
    return(deck)
    #hand that compiled info back to the program

buildDeck()
