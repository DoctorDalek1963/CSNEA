from CSNEA_Shared import *
import random


class Card:
    def __init__(self, colour: str, number: int):
        self.colour = colour
        self.number = number

    def __repr__(self):
        return self.colour + " " + str(self.number)


def win_hand(player_name: str, card_list: list):
    """Append cards to winner's stack and report win."""
    # Appends both cards to the winner's card stack
    card_list.append(p1ActiveCard)
    card_list.append(p2ActiveCard)
    print(f"{player_name} won that hand!")
    print()
    input("Press enter to continue")
    print()


colourDict = {
    'Red,Black' or 'Black,Red': 'Red',
    'Yellow,Red' or 'Red,Yellow': 'Yellow',
    'Black,Yellow' or 'Yellow,Black': 'Black'
}


def compare(card1: Card, card2: Card):
    """Compare cards to find winner of hand."""
    if card1.colour == card2.colour:
        if card1.number > card2.number:
            win_hand(p1Name, p1Cards)
        else:
            win_hand(p2Name, p2Cards)

        return

    colour = card1.colour + "," + card2.colour
    win_colour = colourDict.get(colour)
    if win_colour == card1.colour:
        win_hand(p1Name, p1Cards)
    else:
        win_hand(p2Name, p2Cards)


# ===== Welcome & Rules

print("Welcome to The Card Game!")
print("In this game, each player draws a card, the cards are compared and the winner takes both cards.")
print("In total, 15 hands are drawn.")
print("The player with the most cards at the end wins.")
print()
addPlayerFlag = input("Press 1 to add a new player. Press enter to log in. ")
if addPlayerFlag == 1:
    add_player()
print()

# Authenticate players
p1Name = input("Player 1 please enter your name: ")
p1Pass = input("And your password: ")

authenticate(p1Name, p1Pass)

p2Name = input("Player 2 please enter your name: ")
p2Pass = input("And your password: ")

# Check that player 2 is a different person
if p2Name == p1Name:
    print(f"Sorry, {p2Name}, but that's the same account as player 1.")
    input("Press enter to exit")
    quit()

authenticate(p2Name, p2Pass)

# ===== The Game

# Initialises player's card stacks as empty
p1Cards = []
p2Cards = []

input("Press enter to start")
print("Let's begin the game!")
print()

# Create list of all cards as Card objects
with open("deck.csv") as f:
    deckList = [Card(line.split(",")[0], int(line.split(",")[1])) for line in f.read().splitlines()]

random.shuffle(deckList)

handNum = 1

while len(deckList) > 0:
    print(f"Hand: {handNum}")
    p1ActiveCard = deckList[0]
    del deckList[0]
    p2ActiveCard = deckList[0]
    del deckList[0]

    print(f"{p1Name} drew a {p1ActiveCard}")
    print(f"{p2Name} drew a {p2ActiveCard}")
    print()
    input("Press enter to continue")
    print()

    compare(p1ActiveCard, p2ActiveCard)

    handNum = handNum + 1

print("All cards have been drawn!")
input("The winner is...")
print()

if len(p1Cards) > len(p2Cards):
    winner = p1Name
    winNum = len(p1Cards)
    win_cards = p1Cards
else:
    winner = p2Name
    winNum = len(p2Cards)
    win_cards = p2Cards

print(f"{winner}! With {winNum} cards!")
print()
input("They had these cards:")
print()

for card in win_cards:
    print(card)

print()

with open("card_game_scores.csv", "a") as f:
    f.write(f"{winner},{winNum}\n")

# Create list of all scores as Score objects
with open("card_game_scores.csv") as f:
    scoresList = [Score(line.split(",")[0], int(line.split(",")[1])) for line in f.read().splitlines()]

scoresList.sort(key=lambda x: x.number, reverse=True)

input("These are the high scores:")
print()

for i in range(5):
    try:
        print(scoresList[i])
    except IndexError:
        break  # Stops loop if IndexError occurs

print()
input("Press enter to finish")
print()
print(f"Thank you, {p1Name} and {p2Name}, for playing The Card Game!")
input("Goodbye!")