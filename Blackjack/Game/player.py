class Player():
    """Class handles player and game logic

     Attributes:
        bet_account: int     --  holds the players account amount
        player_name: string  --  holds the name of the player
        cards: list          --  holds the cards
    """


    def __init__(self, bet_account = 0, player_name = 'name'):
        """Inits Enitity class with bet_account, player.name and cards """
        self.bet_account = bet_account
        self.player_name = player_name
        self.cards = []
    
    def deposit(self, amount):
        """deposit momey into players account
        
        Parameters:
        amount: int -- amount to deposit
        """
        self.bet_account += amount

    def withdraw(self, amount):
        """withdraws momey from players account
        
        Parameters:
        amount: int -- amount to withdraw
        """
        self.bet_account -= amount

    def print_current_cards(self):
        """prints the current cards on the table to the terminal"""
        print('---------------------------------')
        print(f'{self.player_name.capitalize()}''s cards:')
        for card in self.cards:
            print(f'Card: {card.value[0]}, of {card.suit[0]}')
        print(f'Total card value: {self.calc_card_value()}')
        print('---------------------------------')

    def calc_card_value(self):
            """calculates the total value of a players cards, and handles aces

            Returns:
            the total value of player or house cards. 
            """
            total_value = 0
            for card in self.cards:
                total_value += card.value[1]
        
            #checks for aces, and adjust accordingly
            if total_value > 21:
                for card in self.cards:
                    if card.value[0] == "Ace":
                        total_value -= 10
                    if total_value < 21:
                        break

            return total_value


