from random import shuffle


def authenticate(name, password):
    """Authenticate player names and passwords."""
    # Formats player details correctly
    details = name + "," + password
    match = False

    # Searches player_list for details. If found, make match = 1
    for x in player_list:
        if x == details:
            match = True

    # If no match was found
    if not match:
        print()
        print(f"Sorry, {name}, your username or password was incorrect.")
        input("Press enter to exit")
        quit()

    print()
    print(f"Welcome, {name}!")
    print()


def add_player():
    """Add new name and password to player_list."""
    print()
    name = input("Please enter the name of the new player: ")
    password = input("Please enter the password: ")

    new_data = f"{name},{password}\n"
    with open("player_list.csv", "a") as file:
        file.write(new_data)

    print()
    print(f"{name} added!")
    print()


def win_hand(card_list, player):
    """Append cards to winner's stack and report win."""
    # Appends both cards to the winner's card stack
    card_list.append(p1ActiveCard)
    card_list.append(p2ActiveCard)
    print(f"{player} won that hand!")
    print()
    input("Press enter to continue")
    print()


colourDict = {
    'Red Black' or 'Black Red': 'Red',
    'Yellow Red' or 'Red Yellow': 'Yellow',
    'Black Yellow' or 'Yellow Black': 'Black'
}


def colour_compare(colour1, colour2):
    """Compare colours and declare winner."""
    colour = f"{colour1} {colour2}"
    # Compares concatenated colour string with dictionary to get winning colour
    colour_win = colourDict.get(colour)
    if colour_win == colour1:
        win_hand(p1Cards, p1Name)
    else:
        win_hand(p2Cards, p2Name)


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

# === Authentication system

# Gets file of player details as a list
with open("player_list.csv") as f:
    player_list = f.read().splitlines()

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

# Get deck as a list as ["colour number", ...]
with open("deck.txt") as f:
    deck = f.read().splitlines()

shuffle(deck)

# Initialises player's card stacks as empty
p1Cards = []
p2Cards = []

input("Press enter to start")
print("Let's begin the game!")
print()

handNum = 1

# Loop until deck is empty
while len(deck) > 0:
    print(f"Hand: {handNum}")
    # Both players take the top card
    p1ActiveCard = deck[0]
    del deck[0]
    p2ActiveCard = deck[0]
    del deck[0]

    print(f"{p1Name} drew a {p1ActiveCard}")
    print(f"{p2Name} drew a {p2ActiveCard}")
    print()
    input("Press enter to continue")
    print()

    p1Colour = p1ActiveCard.split(" ")[0]
    p2Colour = p2ActiveCard.split(" ")[0]

    # If colours are the same, largest number wins
    if p1Colour == p2Colour:
        p1Number = int(p1ActiveCard.split(" ")[1])
        p2Number = int(p2ActiveCard.split(" ")[1])

        if p1Number > p2Number:
            win_hand(p1Cards, p1Name)
        else:
            win_hand(p2Cards, p2Name)

    # If colours are different, call function
    else:
        colour_compare(p1Colour, p2Colour)

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

for i in win_cards:
    print(i)

print()

# Append score & player to scores.txt
with open("scores.txt", "a") as f:
    f.write(f"{winNum} {winner}\n")

numLines = len(open("scores.txt").readlines())

if numLines < 5:
    print("There are not enough high scores to display them.")
else:
    # Get scores.txt as list called scores_all[] in the form ["score name", ...]
    with open("scores.txt") as f:
        scores_all = f.read().splitlines()

    scores_high = sorted(scores_all, reverse=True)  # Sort scores_high

    input("These are the high scores:")
    print()
    for i in range(5):
        print(scores_high[i])

print()
input("Press enter to finish")
print()
print(f"Thank you, {p1Name} and {p2Name}, for playing The Card Game!")
input("Goodbye!")
