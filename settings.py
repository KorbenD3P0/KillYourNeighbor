#As a functional program, like functions and data would be separated
#by similarities. Constants like the card types, losing score and 
#other game data will be grouped into this file

LIME = "\033[38;2;188;209;35m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"] #Define the 4 suits
FACES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #Define all faces

HAND_SIZE = 7 #Starting hands are always 7
LOSING_SCORE = 100 #Determine what ends the game