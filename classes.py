class PLAYER():
    """docstring for ."""

    def __init__(self):
        self.cards = []
        self.is_human = True
        self.drew = None
        self.after_drew = None
        #stores the card which caused the player to draw 1+ cards
        #can then be used by the AI to pick a colour which would bugger the player



class CARD():
    def __init__(self,number=None,colour=None,special,special_code=None):
        self.special = special
        self.colour = colour
        self.number = number
        self.special_code = special_code

    def is_similar(self,other_card):
        if self.special == False:
            #standard card like 1G, 6B etc
            if other_card.colour == self.colour or other_card.number == self.number:
                return True
            else:
                return False
        else:
            if other_card.special_code == self.special_code:
                return True
            else:
                return False
