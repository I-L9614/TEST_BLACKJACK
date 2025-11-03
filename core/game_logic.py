from deck import *
from player_io import *

def calculate_hand_value(hand: list[dict]) -> int:
    sum = 0
    for i in hand:
        if i['rank'] == 'A':
            sum += 1
        elif i['rank'] == '2':
            sum += 2
        elif i['rank'] == '3':
            sum += 3
        elif i['rank'] == '4':
            sum += 4
        elif i['rank'] == '5':
            sum += 5
        elif i['rank'] == '6':
            sum += 6
        elif i['rank'] == '7':
            sum += 7
        elif i['rank'] == '8':
            sum += 8
        elif i['rank'] == '9':
            sum += 9
        elif i['rank'] == '10':
            sum += 10
        elif i['rank'] == ' j':
            sum += 10
        elif i['rank'] == 'Q':
            sum += 10
        elif i['rank'] == 'K':
            sum += 10
                                          
    return sum



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in player,dealer:
       card1 = deck.pop(0)
       i['hand'].append(card1)
       card2 = deck.pop(0)
       i['hand'].append(card1)
       print(calculate_hand_value(i['hand']))




def dealer_play(deck: list[dict], dealer: dict) -> bool:
    if calculate_hand_value(dealer['hand']) > 17:
        card = deck.pop(0)
        dealer.append(card)
    return de



# def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
#     deal_two_each(deck,player,dealer)
#     ask_player_action()
#     if ask_player_action == 'H':
#         for i in player,dealer:
#             calculate_hand_value(i)
#             if i > 21:
#                 print("you loss")
#                 break
#             else:
#                 continue

    
    

         

