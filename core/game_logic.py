from deck import *
from player_io import *
CARD_VALUE = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":1}
def calculate_hand_value(hand: list[dict]) -> int:
    sum = 0
    for i in hand:
        num = CARD_VALUE[i['rank']]
        sum += num
    return sum



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in player,dealer:
        num1 = deck.pop[0]
        pirst = calculate_hand_value(num1)
        num2 = deck.pop[0]
        second = calculate_hand_value(num2)
        sum = num1 + num2
        i['hand'] = sum
    print(player,dealer)

print(deal_two_each())    


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while dealer['hand'] > 17:
        return 'H'
    if dealer['hand'] > 21:
        return False
    else:
        return True



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    ask_player_action()
    if ask_player_action == 'H':
        for i in player,dealer:
            calculate_hand_value(i)
            if i > 21:
                print("you loss")
                break
            else:
                continue

    
    

         

