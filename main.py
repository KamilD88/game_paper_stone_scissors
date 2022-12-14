import random


# function say hello and print game rules
def welcome():
    print("""Witaj we wspaniałej grze papier, kamień, nożyce, jaszczurka, Spock.
        Oto zasady:
        nożyce tną papier, papier zakrywa kamień, 
        kamień zgniata jaszczurkę, jaszczurka zatruwa Spocka,
        Spock niszczy nożyce, nożyce obcinają głowę jaszczurce,
        jaszczurka zjada papier, papier obala istnienie Spocka,
        Spock dezintegruje kamień, kamień tępi nożyce
        
        """)


# function random choice symbol for computer player
def computer_player():
    # P - papier
    # K - kamień
    # N - nożyce
    # J - jaszczurka
    # S - Spock
    possible_symbols = ["p", "k", "n", "j", "s"]
    computer_choice = random.choice(possible_symbols)
    print(f"komputer wybrał: {symbols.get(computer_choice)}")
    return computer_choice


# function for mode choice single with computer or multi with 2 player
def mode_choice():
    mode = str.lower(input("""Wpisz odpowiednią litere dla wybranego trybu gry:
    S - tryb gry z komputerem
    M - tryb gry 2 graczy
    Twoj wybór: """))
    return mode


# function check correctness of mode selection and print info about chosen mode
def mode_input(mode_i):
    if mode_i == 's':
        print("Wybrałeś gre z komputerem\n")
        return mode_i
    elif mode_i == 'm':
        print("Wybrałeś gre z drugim graczem\n")
        return mode_i
    else:
        print("Niepoprawny wybór proszę o wpisanie 's' lub 'm'\n")
        return mode_input(mode_choice())


# function for pick symbol and check correctnes
def symbols_pick():
    pick = str.lower(input("""Wybierz swój symbol: 
              P - papier
              K - kamień
              N - nożyce
              J - jaszczurka
              S - Spock
Twój symbol : """))
    if pick != 'p' and pick != 'k' and pick != 'n' and pick != 'j' and pick != 's':
        print(f" {pick} jest nieprawiłowy, proszę o wybranie prawidłowego symbolu\n")
        return symbols_pick()
    else:
        return pick


# pick player 1
def player_1(pick_1x):
    print(f"Player 1 wybrał: {symbols.get(pick_1x)}")
    return pick_1x


# pick player 2
def player_2(pick_2y):
    print(f"Player 2 wybrał: {symbols.get(pick_2y)}")
    return pick_2y


# function to pick for players depends on game mode, logic who win the game
def game_mode(mode):
    if mode == "s":
        pick_1 = player_1(symbols_pick())
        pick_2 = computer_player()
        if pick_1 == pick_2:
            return print("Remis - nikt nie wygrał")
        elif pick_1 == "p" and pick_2 == "k":
            return print("wygrywa Player 1 - papier zakrywa kamień")
        elif pick_1 == "p" and pick_2 == "s":
            return print("wygrywa Player 1 - papier obala istnienie Spocka")
        elif pick_1 == "k" and pick_2 == "j":
            return print("wygrywa Player 1 - kamień zgniata jaszczurkę")
        elif pick_1 == "k" and pick_2 == "n":
            return print("wygrywa Player 1 - kamień tępi nożyce")
        elif pick_1 == "n" and pick_2 == "p":
            return print("wygrywa Player 1 - nożyce tną papier")
        elif pick_1 == "n" and pick_2 == "j":
            return print("wygrywa Player 1 - nożyce obcinają głowę jaszczurce")
        elif pick_1 == "j" and pick_2 == "s":
            return print("wygrywa Player 1 - jaszczurka zatruwa Spocka")
        elif pick_1 == "j" and pick_2 == "p":
            return print("wygrywa Player 1 - jaszczurka zjada papier")
        elif pick_1 == "s" and pick_2 == "n":
            return print("wygrywa Player 1 - Spock niszczy nożyce")
        elif pick_1 == "s" and pick_2 == "k":
            return print("wygrywa Player 1 - Spock dezintegruje kamień")
        elif pick_2 == "p" and pick_1 == "k":
            return print("wygrywa komputer - papier zakrywa kamień")
        elif pick_2 == "p" and pick_1 == "s":
            return print("wygrywa komputer - papier obala istnienie Spocka")
        elif pick_2 == "k" and pick_1 == "j":
            return print("wygrywa komputer - kamień zgniata jaszczurkę")
        elif pick_2 == "k" and pick_1 == "n":
            return print("wygrywa komputer - kamień tępi nożyce")
        elif pick_2 == "n" and pick_1 == "p":
            return print("wygrywa komputer - nożyce tną papier")
        elif pick_2 == "n" and pick_1 == "j":
            return print("wygrywa komputer - nożyce obcinają głowę jaszczurce")
        elif pick_2 == "j" and pick_1 == "s":
            return print("wygrywa komputer - jaszczurka zatruwa Spocka")
        elif pick_2 == "j" and pick_1 == "p":
            return print("wygrywa komputer - jaszczurka zjada papier")
        elif pick_2 == "s" and pick_1 == "n":
            return print("wygrywa komputer - Spock niszczy nożyce")
        elif pick_2 == "s" and pick_1 == "k":
            return print("wygrywa komputer - Spock dezintegruje kamień")
    elif mode == "m":
        pick_1 = player_1(symbols_pick())
        pick_2 = player_2(symbols_pick())
        if pick_1 == pick_2:
            return print("Remis - nikt nie wygrał")
        elif pick_1 == "p" and pick_2 == "k":
            return print("wygrywa Player 1 - papier zakrywa kamień")
        elif pick_1 == "p" and pick_2 == "s":
            return print("wygrywa Player 1 - papier obala istnienie Spocka")
        elif pick_1 == "k" and pick_2 == "j":
            return print("wygrywa Player 1 - kamień zgniata jaszczurkę")
        elif pick_1 == "k" and pick_2 == "n":
            return print("wygrywa Player 1 - kamień tępi nożyce")
        elif pick_1 == "n" and pick_2 == "p":
            return print("wygrywa Player 1 - nożyce tną papier")
        elif pick_1 == "n" and pick_2 == "j":
            return print("wygrywa Player 1 - nożyce obcinają głowę jaszczurce")
        elif pick_1 == "j" and pick_2 == "s":
            return print("wygrywa Player 1 - jaszczurka zatruwa Spocka")
        elif pick_1 == "j" and pick_2 == "p":
            return print("wygrywa Player 1 - jaszczurka zjada papier")
        elif pick_1 == "s" and pick_2 == "n":
            return print("wygrywa Player 1 - Spock niszczy nożyce")
        elif pick_1 == "s" and pick_2 == "k":
            return print("wygrywa Player 1 - Spock dezintegruje kamień")
        elif pick_2 == "p" and pick_1 == "k":
            return print("wygrywa Player 2 - papier zakrywa kamień")
        elif pick_2 == "p" and pick_1 == "s":
            return print("wygrywa Player 2 - papier obala istnienie Spocka")
        elif pick_2 == "k" and pick_1 == "j":
            return print("wygrywa Player 2 - kamień zgniata jaszczurkę")
        elif pick_2 == "k" and pick_1 == "n":
            return print("wygrywa Player 2 - kamień tępi nożyce")
        elif pick_2 == "n" and pick_1 == "p":
            return print("wygrywa Player 2 - nożyce tną papier")
        elif pick_2 == "n" and pick_1 == "j":
            return print("wygrywa Player 2 - nożyce obcinają głowę jaszczurce")
        elif pick_2 == "j" and pick_1 == "s":
            return print("wygrywa Player 2 - jaszczurka zatruwa Spocka")
        elif pick_2 == "j" and pick_1 == "p":
            return print("wygrywa Player 2 - jaszczurka zjada papier")
        elif pick_2 == "s" and pick_1 == "n":
            return print("wygrywa Player 2 - Spock niszczy nożyce")
        elif pick_2 == "s" and pick_1 == "k":
            return print("wygrywa Player 2 - Spock dezintegruje kamień")
        else:
            return print("błąd")


symbols = {"p": "papier", "k": "kamień", "n": "nożyce", "j": "jaszczurka", "s": "Spock"}

welcome()

game_mode(
    mode_input(
        mode_choice()
    )
)
