# This algorithm simulates a Pelagaletto game.

import random
# Those two next global variables are used inside the function "vincere" and I had to define them outside.
lista_carte = []
stop_game = False

# This next function "vincere" means "win" and refers to a player (eg player A),
# and is used when is it's opponent's turn (eg. player B).

# If player B loses, then player A wins. The game stops and the function returns a list which has
# in position [0] the index of player B, but increased of 1000 (the reason is seen later),
# and in position [1] another list containing strings representing all the cards played in order.
# This list is called "lista_carte".

# If player B does not lose, the game continues and it's now player A turn.
# In such case, the function still returns player B's index, but not increased by 1000.

def vincere(giocatore_1, giocatore_2, index_g1, index_g2, nome, nome2):
    try:
        print(f"Carta giocata {nome}: {giocatore_1[index_g1]}.")
        lista_carte.append(giocatore_1[index_g1])

        # The player wins by playing "uno"
        if giocatore_1[index_g1] != "inutile":
            if giocatore_1[index_g1] == "uno" and (giocatore_2[index_g2] == "inutile" or giocatore_2[index_g2] is None):
                print(f"Carta giocata {nome2}: {giocatore_2[index_g2]}.")
                lista_carte.append("inutile")
                print(f"{nome} vince il turno! \n")
                # print(index_g1)
                # print(index_g2)
                return index_g2 + 1000, lista_carte

            # The player wins by playing "due"
            elif giocatore_1[index_g1] == "due" and (
                    giocatore_2[index_g2] == "inutile" or giocatore_2[index_g2] is None) \
                    and (giocatore_2[index_g2 + 1] == "inutile" or giocatore_2[index_g2 + 1] is None):
                print(f"Carta giocata {nome2}: {giocatore_2[index_g2]}.")
                print(f"Carta giocata {nome2}: {giocatore_2[index_g2 + 1]}.")
                lista_carte.extend(("inutile", "inutile"))
                print(f"{nome} vince il turno! \n")
                index_g2 = index_g2 + 1
                # print(index_g1)
                # print(index_g2)
                return index_g2 + 1000, lista_carte

            # The player wins by playing "tre"
            elif giocatore_1[index_g1] == "tre" and (
                    giocatore_2[index_g2] == "inutile" or giocatore_2[index_g2] is None) \
                    and (giocatore_2[index_g2 + 1] == "inutile" or giocatore_2[index_g2 + 1] is None) \
                    and (giocatore_2[index_g2 + 2] == "inutile" or giocatore_2[index_g2 + 2] is None):
                print(f"Carta giocata {nome2}: {giocatore_2[index_g2]}.")
                print(f"Carta giocata {nome2}: {giocatore_2[index_g2 + 1]}.")
                print(f"Carta giocata {nome2}: {giocatore_2[index_g2 + 2]}.")
                lista_carte.extend(("inutile", "inutile", "inutile"))
                print(f"{nome} vince il turno! \n")
                index_g2 = index_g2 + 2
                # print(index_g1)
                # print(index_g2)
                return index_g2 + 1000, lista_carte
            else:
                if giocatore_2[index_g2] == "inutile":
                    print(f"Carta giocata {nome2}: {giocatore_2[index_g2]}.")
                    lista_carte.append(giocatore_2[index_g2])
                    index_g2 = index_g2 + 1
                if giocatore_2[index_g2] == "inutile":
                    print(f"Carta giocata {nome2}: {giocatore_2[index_g2]}.")
                    lista_carte.append(giocatore_2[index_g2])
                    index_g2 = index_g2 + 1
                if giocatore_2[index_g2] == "inutile":
                    print(f"Carta giocata {nome2}: {giocatore_2[index_g2]}.")
                    lista_carte.append(giocatore_2[index_g2])
                    index_g2 = index_g2 + 1
        return index_g2, lista_carte
    # It has a try-except statement because it will throw an Index_Error if player B deck is too short,
    #  which means that player A just won
    except IndexError:
        if len(giocatore_1) > len(giocatore_2):
            print(f"{nome} VINCE LA PARTITA!!!!!")
            stop_game = True
        else:
            print(f"{nome2} VINCE LA PARTITA!!!!!")
            stop_game = True

# Generating the two different decks
# "uno" means one, "due" means two, "tre" means three and "inutile" means useless
uno = random.randint(0, 4)
due = random.randint(0, 4)
tre = random.randint(0, 4)
inutile = 20 - (uno + due + tre)
gioc_1 = ["uno"] * uno + ["due"] * due + ["tre"] * tre + ["inutile"] * inutile
random.shuffle(gioc_1)
gioc_2 = ["uno"] * (4 - uno) + ["due"] * (4 - due) + ["tre"] * (4 - tre) + ["inutile"] * (28 - inutile)
random.shuffle(gioc_2)


# This next is the famous infinite game. This is the only one ever found so far.
# Giocatore 1: 0 0 3 0 2 0 2 0 3 0 3 1 0 0 0 0 0 3 1 0
# Giocatore 2: 0 0 1 0 0 2 0 0 0 0 2 0 0 0 0 0 0 0 1 0

# This is it written for this game:
#gioc_1 = ["inutile", "inutile", "tre", "inutile", "due", "inutile", "due", "inutile", "tre", "inutile", "tre",
#          "uno", "inutile", "inutile", "inutile", "inutile", "inutile", "tre", "uno", "inutile"]
#gioc_2 = ["inutile", "inutile", "uno", "inutile", "inutile", "due", "inutile",
#          "inutile", "inutile", "inutile", "due", "inutile", "inutile", "inutile", "inutile",
#          "inutile", "inutile", "inutile", "uno", "inutile"]

# This variable is used to change who starts depending on who just won
Antonio_won_last_time = True
# This variable means "turns"
turni = 0

# The first part of the algorithm skips all those turns when both players have "useless" cards.
while (len(gioc_1) != 0 or len(gioc_2) != 0) and stop_game == False:
    breaker = False
    turni = turni + 1
    print(f"Turno numbero {turni}")
    print(f"Antonio = {gioc_1}")
    print(f"Ulrich = {gioc_2}")
    index_1 = 0
    index_2 = 0
    useless_cards_list = []
    lista_carte = []
    # It has a try-except statement because it will throw an Index_Error if one deck is too short,
    #  which means that the opponent won
    try:
        while gioc_1[index_1] == "inutile" and gioc_2[index_2] == "inutile":
            # if Antonio_won_last_time == True:
            print(f"Carta giocata giocatore 1: {gioc_1[index_1]}.")
            useless_cards_list.append("inutile")
            print(f"Carta giocata giocatore 2: {gioc_2[index_2]}.")
            useless_cards_list.append("inutile")
            index_1 = index_1 + 1
            index_2 = index_2 + 1
    except IndexError:
        if len(gioc_1) == 0:
            print("Giocatore 2 vince la partita! \n")
            break
        elif len(gioc_2) == 0:
            print("Giocatore 1 vince la partita! \n")
            break
        else:
            # IndexError as index_error
            # print(index_error)
            pass
    # print("EXIT USELESS CARDS TURNS! \n")

    # This loop uses the "vincere function". It basically loops and increases both player indexes until the "vincere
    # function" returns an index greater than 900. In such case, it appends to the winner all the useless cards
    # played in the loop before as well as "lista_carte" (which is the list of "useful" cards, those played in all
    # the vincere functions run in this while loop. This is also why I put "lista_carte" as a global variable: it
    # needs to NOT reset each "vincere" function, but to reset each time a player wins.) Then, all the cards played
    # are eliminated from the beginning of both player's decks.
    while True:
        try:
            if Antonio_won_last_time:
                var = vincere(gioc_1, gioc_2, index_1, index_2, "Giocatore 1", "Giocatore 2")
                index_2 = var[0]
                index_1 = index_1 + 1
                if index_2 > 900:
                    index_2 = index_2 - 1000
                    # print(useless_cards_list + var[1])
                    gioc_1.extend(useless_cards_list)
                    gioc_1.extend(var[1])
                    del gioc_2[:index_2 + 1]
                    del gioc_1[:index_1]
                    Antonio_won_last_time = True
                    break
                varr = vincere(gioc_2, gioc_1, index_2, index_1, "Giocatore 2", "Giocatore 1")
                index_1 = varr[0]
                index_2 = index_2 + 1
                if index_1 > 900:
                    index_1 = index_1 - 1000
                    # print(useless_cards_list + varr[1])
                    gioc_2.extend(useless_cards_list)
                    gioc_2.extend(varr[1])
                    del gioc_2[:index_2]
                    del gioc_1[:index_1 + 1]
                    Antonio_won_last_time = False
                    break
            # Those next lines are for when player 2 won last time and therefore is supposed to start now.
            else:
                varr = vincere(gioc_2, gioc_1, index_2, index_1, "Giocatore 2", "Giocatore 1")
                index_1 = varr[0]
                index_2 = index_2 + 1
                if index_1 > 900:
                    index_1 = index_1 - 1000
                    gioc_2.extend(useless_cards_list)
                    gioc_2.extend(varr[1])
                    del gioc_2[:index_2]
                    del gioc_1[:index_1 + 1]
                    Antonio_won_last_time = False
                    break
                var = vincere(gioc_1, gioc_2, index_1, index_2, "Giocatore 1", "Giocatore 2")
                index_2 = var[0]
                index_1 = index_1 + 1
                if index_2 > 900:
                    index_2 = index_2 - 1000
                    gioc_1.extend(useless_cards_list)
                    gioc_1.extend(var[1])
                    del gioc_2[:index_2 + 1]
                    del gioc_1[:index_1]
                    Antonio_won_last_time = True
                    break
        # This is just because if you do not do this it will throw a Type_Error at the end of the game
        except TypeError:
            breaker = True
            break

    if breaker:
        break

# CONSIDERATION FOR FUTURE ALGORITHMS: It would be interesting to see in the future is if someone can cheat to
# increase its hedge. Like what if I always start first? Do I have more or less possibilities to win? By how much?
# Another cool study would be to calculate certain statistics (for example, the average duration of a game)
