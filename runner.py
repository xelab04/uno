import to_do as ToDo
from classes import *
import artificial_intelligense as AI

def change_index(player_index,increment):
    new_index = player_index
    new_index += increment
    if new_index >= len(player_array):
        new_index = 0
    elif new_index < 0:
        new_index = len(player_array) - 1
    return new_index

def change_top_stack(cards_played,top_of_stack,deck):
    if len(cards_played) > 1:
        ToDo.add_to_deck(cards_played[:-1:])
        #add everything to deck, excluding last one
    ToDo.add_to_deck(top_of_stack)
    #just adding the top of stack to deck
    top_of_stack = cards_played[-1]
    return top_of_stack
    #last one in the cards played array is the last card played
    #therefore top of stack now

def main():
    player_array = [PLAYER(),AI.AI()]
    player_index = -1
    increment = 1
    top_of_stack = None

    deck = []

    #game loop
    while True:
        player_index = change_index(player_index,increment)
        #increment changes to -1 if a reverse card is played

        current_player = player_array[player_index]

        while playable_cards(top_of_stack, current_player.cards) == []:
            current_player.drew = top_of_stack
            print("No valid cards :<")
            #time to draw cards until a card is usable
            card = ToDo.draw_card(deck)#get a random card
            ToDo.remove_card([card],deck)#remove from deck
            add_cards(current_player,[card])#add to player's hand

            if playable_cards(top_of_stack, [card]) != []:
                current_player.after_drew = card


        #basically get the cards which are being played
        if current_player.is_human:
            print(current_player.cards)
            cards = ToDo.select_cards()
        else:
            #get the AI to select one or more cards
            cards = current_player.select_cards(top_of_stack,change_index(player_index,increment))
            #be careful as it may change player_index which would be a pain

        #remove cards from player's hand
        #beware, this may not affect the player's hand itself
        remove_cards(player,cards)
        #already deals with adding cards to the deck
        top_of_stack = change_top_stack(cards_played,top_of_stack,deck)

        if ToDo.is_game_over:
            print("GAME OVER!")
            return 0
            #game has ended


if __name__ == "__main__":
   main()
