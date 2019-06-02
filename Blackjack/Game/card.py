class Card():
    """Class handles cards in a deck

     Attributes:
        suit       --  The possible suits in a deck of cards
        value      --  The possible values in a deck of cards
    """

    suits = [('Heart',1), ('Diamond',2), ('Spade',3), ('Club',4)]
    values = [('Ace',11),('Two',2),('Three',3),('Four',4),('Five',5),
     ('Six',6),('Seven',7), ('Eight',8), ('Nine',9), ('Ten',10),
     ('Jack',10), ('Queen',10),('King',10)]
    
    def __init__(self, card_value = 0, suit = 0):
        """Inits Card class with card_value and suit """
        self.value = Card.values[card_value]
        self.suit = Card.suits[suit]

        
