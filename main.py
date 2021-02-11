from IPython.display import clear_output


def Tictac_printgame(a):
    print("   i   i   ")
    print(f" {a[7]} i {a[8]} i {a[9]} ")
    print("   i   i   ")
    print("-----------")
    print("   i   i   ")
    print(f" {a[4]} i {a[5]} i {a[6]} ")
    print("   i   i   ")
    print("-----------")
    print("   i   i   ")
    print(f" {a[1]} i {a[2]} i {a[3]} ")
    print("   i   i   ")


def Tictac_choose_position():
    choice = "wrong"
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        choice = input(
            "choose a position corresponding to the numbers on your numpad: ")
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("invalid input")
    return int(choice)


def Tictac_chooseplayer():
    player = "spatne"
    while player not in ["O", "X"]:
        player = input("Should the first player be X or O?")
        if player not in ["O", "X"]:
            clear_output()
            print("invalid input")
    return player


def Tictac_place_symbol(Tictac_gamelist, current_player):
    Tictac_gamelist[Tictac_choose_position()] = current_player


def Tictac_game_tie(Tictac_gamelist):
    if " " not in Tictac_gamelist.values():
        return True
    return False


def Tictac_game_end(Tictac_gamelist):
    if Tictac_gamelist[1] == Tictac_gamelist[2] == Tictac_gamelist[3] and Tictac_gamelist[1] != " ":
        return True
    elif Tictac_gamelist[4] == Tictac_gamelist[5] == Tictac_gamelist[6] and Tictac_gamelist[4] != " ":
        return True
    elif Tictac_gamelist[7] == Tictac_gamelist[8] == Tictac_gamelist[9] and Tictac_gamelist[7] != " ":
        return True
    elif Tictac_gamelist[1] == Tictac_gamelist[4] == Tictac_gamelist[7] and Tictac_gamelist[1] != " ":
        return True
    elif Tictac_gamelist[2] == Tictac_gamelist[5] == Tictac_gamelist[8] and Tictac_gamelist[2] != " ":
        return True
    elif Tictac_gamelist[3] == Tictac_gamelist[6] == Tictac_gamelist[9] and Tictac_gamelist[3] != " ":
        return True
    elif Tictac_gamelist[1] == Tictac_gamelist[5] == Tictac_gamelist[9] and Tictac_gamelist[1] != " ":
        return True
    elif Tictac_gamelist[7] == Tictac_gamelist[5] == Tictac_gamelist[3] and Tictac_gamelist[7] != " ":
        return True
    else:
        return False


def Tictac_continue():
    continue_game = "wrong"
    while continue_game not in ["Yes", "No"]:
        continue_game = input("Do you want to continue (Yes / No)?")
        if continue_game not in ["Yes", "No"]:
            print("invalid input")
    return continue_game == "Yes"


chces_hrat = True

while chces_hrat == True:
    hracilist = {1: " ", 2: " ", 3: " ", 4: " ",
                 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    hrac = Tictac_chooseplayer()

    while True:
        clear_output()
        Tictac_printgame(hracilist)
        print("hraje {}".format(hrac))
        Tictac_place_symbol(hracilist, hrac)
        if Tictac_game_end(hracilist) == True:
            clear_output()
            Tictac_printgame(hracilist)
            print(f"hra skoncila, vyhrál {hrac}")
            break
        if Tictac_game_tie(hracilist) == True:
            clear_output()
            Tictac_printgame(hracilist)
            print(f"hra skoncila, remíza")
            break
        if hrac == "X":
            hrac = "O"
        elif hrac == "O":
            hrac = "X"
    chces_hrat = Tictac_continue()
    clear_output()
clear_output()
print("Thanks for playing")
