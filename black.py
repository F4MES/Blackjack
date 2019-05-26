from random import shuffle

class Card():
    """Class handles cards in a deck

     Attributes:
        suit       --  The possible suits in a deck of cards
        card_value --  The possible values in a deck of cards
    """

    suits = [('Heart',1), ('Diamond',2), ('Spade',3), ('Club',4)]
    values = [('Ace',11),('Two',2),('Three',3),('Four',4),('Five',5),
     ('Six',6),('Seven',7), ('Eight',8), ('Nine',9), ('Ten',10),
     ('Jack',10), ('Queen',10),('King',10)]
    
    def __init__(self, card_value = 0, suit = 0):
        """Inits Card class with card_value and suit """
        self.card_value = Card.values[card_value]
        self.suit = Card.suits[suit]

class Entity():
    """Class handles entities and game logic

     Attributes:
        bet_account: int     --  holds the players account amount
        entity_name: string  --  holds the name of the player
        cards: list          --  holds the cards
    """


    def __init__(self, bet_account = 0, entity_name = 'name'):
        """Inits Enitity class with bet_account, entity.name and cards """
        self.bet_account = bet_account
        self.entity_name = entity_name
        self.cards = []
    

    def deposit(self, amount):
        """deposit momey into players account
        
        Parameters:
        amount: int -- amount to deposit
        """
        self.bet_account += amount


    def calc_card_value(self):
        """calculates the total value of a players cards, and handles aces

        Returns:
        the total value of player or house cards. 
        """
        total_value = 0
        for card in self.cards:
            total_value += card.card_value[1]
        
        #checks for aces, and adjust accordingly
        if total_value > 21:
            for card in self.cards:
                if card.card_value[0] == "Ace":
                    total_value -= 10
                if total_value < 21:
                    break

        return total_value

    def print_current_cards(self):
        """prints the current cards on the table to the terminal"""
        print('---------------------------------')
        print(f'{self.entity_name.capitalize()}''s cards:')
        for card in self.cards:
            print(f'Card: {card.card_value[0]}, of {card.suit[0]}')
        print(f'Total card value: {self.calc_card_value()}')
        print('---------------------------------')


def generate_deck():
    """Generate a deck of cards.

    Returns:
    a new deck containing 52 cards
    """
    deck = []
    order = list(range(1,53))
    shuffle(order)
    for i in order:
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
    """Check who won the game by going through the scores and dertimining who won """

    if house.calc_card_value() == 21:
        print("House got blackjack!")
    if player.calc_card_value() == 21:
        print(player.entity_name + " got blackjack!")

    if house.calc_card_value() > 21:
        print(player.entity_name + " won")
        player.deposit(bet)

    elif player.calc_card_value() > house.calc_card_value():
        print(player.entity_name + " won")
        player.deposit(bet)
    else:
        print('House won')
        player.deposit(-bet)  


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
    #if the user decides to hit, they are dealt another card. 
    while True:
        action = input('(h (hit) or s (stand)?')
        if action == 'h':
            deal_card(player, deck)
            player.print_current_cards()
        
        elif action == 's':
            player.print_current_cards()
            break

        if player.calc_card_value() > 21:
            player.print_current_cards()
            print(player.entity_name + ' busts')
            bust = True
            break
    
    if bust:
        player.deposit(-bet)
    #computers turn if the user decides to stand
    else:
        while house.calc_card_value() < 17:
            deal_card(house, deck)

    house.print_current_cards()

    if not bust:
        check_winner(player, house, bet)

    print(f'{player.entity_name} you now have {player.bet_account} in your account')

    
def main():
    """Initial setup. Gets player name and how much they wants to deposit, starts game """
    print()
    name = input('What is your name?').capitalize()
    if name == "":
        print("You need to type a name")
        main() 
    try:       
        money = int(input('How much do you want to deposit?'))
    except ValueError:
        print("Not a valid deposit")
        main()
    #creates objects of player and house
    player = Entity(bet_account = money, entity_name = name)
    house = Entity(bet_account = 10000000, entity_name = "House")
    stop = False
    while not stop:
        deck = generate_deck()
        player.cards = []
        house.cards = []
        try:
            bet = int(input('How much do you want to bet?'))
            if bet <= player.bet_account:
            # starts the game
                play_game(player,house,deck,bet) 
            else:
                print("You cannot bet more than you have!")
        except ValueError:
            print("Not a valid bet")       

        want_to_stop = input('To stop write stop, to try again press enter')
        if want_to_stop == "stop":
            stop = True

    

if __name__ == '__main__':
    main()