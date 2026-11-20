import random
from dealDeck import cpuCount, startingCard

playerCount = cpuCount + 1
lastPlayed = [startingCard]       # the pile; the top card is lastPlayed[-1]
currentSuit = startingCard[1]     # the suit a play must match (a Jack will change it)
turn = random.randint(0, cpuCount)    # 0 is player, 1 and up are CPUs
direction = 1                     # a King will flip this to -1
roundOver = False                 # tracks the game status

