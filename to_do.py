def playable_cards(top_of_stack, cards_list):
    '''
    given a list of cards held, return a list of cards which can be played
    cards_list will have the format ["1G","9R","+4","SKP","REV"]
    the cards are playable if they are special cards (SKP,REV) OR
    if their number matches that of the top_of_stack OR
    if their colour matches that of the top_of_stack

    the returned array must be an array of similar structure
    return_array = ["1G","1Y","6G","+4","SKP","REV"]
    '''
    return NotImplementedError

def select_cards(cards_list):
    '''
    prompt the player to select a card from the given cards_list
    if the player has several possible moves, they are prompted repeatedly
    the player has the option to play only once even if presented with multiple possible moves
    if the player wants to play only once, they input "END" at the second prompt
    "END" ends their turn
    proper validation and verification must be enforced in this step
    MUST be in playable_cards
    the player cannot play no card
    '''
    return NotImplementedError

def is_game_over(player_array):
    '''
    given the array of players, your task is to determine if the game is over
    the game is over when a player has no cards left
    there is no competition for 2nd or 3rd place
    if you're not 1st, tough luck, you lose
    return True if the game has been won, false otherwise
    '''
    return NotImplementedError

def add_cards(player,cards_array):
    '''
    add all the cards in cards_array to player.cards
    player.cards is an array holding all the cards the player is holding
    '''
    return NotImplementedError

def remove_cards(player,cards_array):
    '''
    as you may guess, it is the same as the function above, it just removes the cards
    '''
    return NotImplementedError

def add_to_deck(cards_array,deck):
    '''
    append the cards in cards_array to deck
    return deck afterwards
    '''
    return NotImplementedError


def remove_from_deck(cards_array,deck):
    '''
    view above
    '''
    return NotImplementedError

def draw_card(deck):
    '''
    make a random selection of a card from the array deck
    return the selection as a string
    '''
    return NotImplementedError
