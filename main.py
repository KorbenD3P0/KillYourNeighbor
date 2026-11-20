#Deb confirmed that a main.py is necessary
from settings import YELLOW, RESET, BLUE #Importing colors from settings to display text correctly
from dealDeck import createGame #Import the main function creating the game components
from gameLoop import runGame #Import the main function running the game loop

def main():
    #Begin the process by assigning vital variables
    print("This is an "+YELLOW+"'input'"+RESET+" function, used to collect data from users. That data is being assigned to a "+BLUE+"'variable'"+RESET+" called "+BLUE+"'numDecks'"+RESET+".")
    numDecks = int(input(YELLOW+"How many decks are we using today? "+RESET)) 
    #My family believes more decks = more spice
    print("This "+YELLOW+"'input'"+RESET+" function is for specifying how many CPU players. That data is being assigned to a "+BLUE+"'variable'"+RESET+" called "+BLUE+"'cpuCount'"+RESET+".")
    cpuCount = int(input(YELLOW+"How many friends are we playing with? "+RESET))
    #Each new CPU is a new value in 'hands' that is defined later
    startEffects = input("Should the starting card trigger its effect? (y/n) ").lower()
    
    hands, deck, starting_card = createGame(numDecks, cpuCount)
    runGame(hands, deck, starting_card, cpuCount, startEffects)

if __name__ == "__main__":
    main()
