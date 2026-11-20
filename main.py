#Deb confirmed that a main.py is necessary
from settings import LIME, YELLOW, RESET, BLUE #Importing colors from settings to display text correctly
from dealDeck import createGame #Import the main function creating the game components
from gameLoop import runGame #Import the main function running the game loop

print(LIME+"Welcome to Kill Your Neighbor! "+RESET+"I'll be teaching you a card game and how to write some python code today.\n")
input("Press enter to continue...")

def main():
    #Begin the process by assigning vital variables
    numDecks = 0
    validInput = False
    while validInput == False:
        try:
            numDecks = int(input(YELLOW+"How many decks are we using today? "+RESET)) 
            if numDecks >= 1:
                validInput = True
            else:
                print("You need at least 1 deck!")
        except ValueError: #A ValueError is used with integers
            print("Invalid response! Try entering numbers.")
        #My family believes more decks = more pissed off neighbors
    print(f"That question was asked inside of an {YELLOW}'input'{RESET} function, used to collect data from users. That {numDecks} is being assigned to a {BLUE}'variable'{RESET} called {BLUE}'numDecks'{RESET}, and referencing it in the program is how I can correctly say every time you play that you chose {BLUE}{numDecks}{RESET} deck(s).")

    try:
        cpuCount = int(input(YELLOW+"How many CPU friends are we playing with? "+RESET))
        print(f"That {YELLOW}'input'{RESET} function was for specifying how many CPU players. That data is being assigned to a {BLUE}'variable'{RESET} called {BLUE}'cpuCount'{RESET}, and I can reference it to let you know that you chose {BLUE}{cpuCount}{RESET} CPUs to play against.")
        #Each new CPU is a new value in 'hands' that is defined later
    except ValueError:
        print("Invalid response! Try entering numbers.")
    
    startEffects = input("Should the starting card trigger its effect? (y/n) ").lower()
    #This decides if things like 2's, jokers, or other active cards take effect on the first play    

    hands, deck, starting_card = createGame(numDecks, cpuCount)
    runGame(hands, deck, starting_card, cpuCount, startEffects)

if __name__ == "__main__":
    main()
