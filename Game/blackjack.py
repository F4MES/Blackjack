from random import shuffle
from card import Card
from player import Player


def generate_deck():
    """Generate a deck of cards.

    Returns:
    a new deck containing 52 cards
    """
    deck = []
    order = list(range(1,53)) 
    shuffle(order) #shuffles the order randomly
    for i in order:#puts card in the deck
        card = Card(i % 13, i % 4)
        deck.append(card)
    
    return deck

def deal_card(player, deck):
    """gets a card out of the deck, to hand over to player 
    
    Parameters:
    player: obj -- object of player
    deck: list -- list of the deck
    """
    player.cards.append(deck.pop())

def check_winner(player, house, bet):
    """Check who won the game by going through the different scenarios and dertimining who won """

    #Handles blackjack
    if house.calc_card_value() == 21:
        print("House got blackjack!")
    if player.calc_card_value() == 21:
        print(player.player_name + " got blackjack!")

    if house.calc_card_value() > 21:
        print(player.player_name + " won")
        player.deposit(bet)

    elif player.calc_card_value() > house.calc_card_value():
        print(player.player_name + " won")
        player.deposit(bet)
    elif player.calc_card_value() == house.calc_card_value():
        print("Tie!")
    else:
        print('House won')
        player.withdraw(bet) 

def play_game(player, house, deck, bet):
    """
    Game functionality; deals cards,
    handles hit and pass, 
    checks if player busts 

    Parameters:
    player: obj -- player object
    house: obj -- house object
    deck: list -- list of deck
    bet: int -- placed bet
    """

    #deals 2 cards to the player, and one for the dealer
    deal_card(house, deck)
    deal_card(player, deck)
    deal_card(player, deck)
    #prints the current card on the table
    player.print_current_cards()
    house.print_current_cards()
    bust = False
    #get user input. 
    #if user busts, bust is set to True, and the player looses their bet
    #if the user decides to hit, they are dealt another card. And the game continues 
    while True:
        action = input('press h to hit or s to stand')

        #deals a new card if user decides to hit
        if action == 'h':
            deal_card(player, deck)
            player.print_current_cards()
        
        #if the user decides to stand, it breaks out of the foor loop, and starts to deal cards to house
        elif action == 's':
            player.print_current_cards()
            break

        #checks if the user busts
        if player.calc_card_value() > 21:
            player.print_current_cards()
            print(player.player_name + ' busts')
            bust = True
            break
    
    if bust:
        player.withdraw(bet)
    else:
        #computers turn if the user decides to stand
        #by the rules of blackjack, the dealer stands at 17
        while house.calc_card_value() < 17:
            deal_card(house, deck)

    house.print_current_cards()

    if not bust:
        check_winner(player, house, bet)

    #Prints the current amount for players account
    print(f'{player.player_name} you now have {player.bet_account} in your account')



def get_player_name():
    """Gets the name of the player"""
    while True:
        name = input('What is your name?').capitalize()
        if name is not "": #check that name is not empty
            return name
        else:
            print("You need to type a name!")

def get_deposit_amount():
    """Gets the amount the player wants to deposit """
    while True:
        try:    
            deposit = int(input('How much do you want to deposit?'))
            if deposit > 0: #check if the deposit is positive and bigger than 0
                return deposit
            else:
                print("You need to deposit more than 0")
        except ValueError:
            print("Not a valid deposit")


def main():
    """Initial setup. Gets player name and how much they wants to deposit, starts game """

    #Print welcome message
    print("-------------------------------------------")
    print("Welcome to this python blackjack game!")
    print("if you dont know the rules, go read them.")
    print("Otherwise - Have fun!")
    print("-------------------------------------------")
    print()
    #get player name and deposit
    name = get_player_name()
    deposit = get_deposit_amount()
    #creates objects of player and house
    player = Player(bet_account = deposit, player_name = name)
    house = Player(bet_account = 10000000, player_name = "House")
    stop = False
    while not stop:
        deck = generate_deck()
        player.cards = []
        house.cards = []
        try:
            bet = int(input('How much do you want to bet?'))
            if bet <= player.bet_account and bet > 0:
            #starts the game
                play_game(player,house,deck,bet) 
            else:
                print("Bet cannot be bigger than what you have, and cannot be 0")
        except ValueError:
            print("Not a valid bet")       

        want_to_stop = input('To stop write ¨s¨, to try again press enter')
        if want_to_stop == "s":
            stop = True

    

if __name__ == '__main__':
    main()