import to_do as ToDo

class AI(object):
    """docstring fo AI."""

    def __init__(self):
        self.cards = []
        self.is_human = False
        self.drew = None
        self.after_drew = None

    def select_cards(self,top_of_stack,next_player):
        possible_plays = ToDo.playable_cards(top_of_stack,self.cards)
        
        #need to find a way to best get the card to play
        #maybe want to make next person draw card
        #maybe want to get rid of cards

        #if following player after has less cards, prioritise making them gain cards
        #otherwise, get rid of own cards, keeping in mind making following player's cards
        return selection
