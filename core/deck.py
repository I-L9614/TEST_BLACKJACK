import random
CARD_VALUE = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":1}

SUIT = ["H","C","D","S"]

def build_standard_deck() -> list[dict]:
    DECK = []
    CARD = {}
    for k in CARD_VALUE:
        for j in SUIT:
            CARD = {'rank':k, 'suit':j}
            DECK.append(CARD)
    return DECK


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(swaps):
        i = random.randint(0 ,len(deck) - 1)
        j = random.randint(0, len(deck) - 1 )
        if i == j:
            j = random.randint(0, len(deck) - 1 )
        else:
            if deck[i]['suit'] == 'H':
                if j % 5 == 0:
                    deck[i],deck[j] = deck[j],deck[i]
                else:
                    continue   
            elif deck[i]['suit'] == 'C':
                if j % 3 == 0:
                    deck[i],deck[j] = deck[j],deck[i]
                else:
                    continue
            elif deck[i]['suit'] == 'D':
                if j % 2 == 0:
                    deck[i],deck[j] = deck[j],deck[i]
                else:
                    continue
            elif deck[i]['suit'] == 'S':   
                if j % 7 == 0:
                     deck[i],deck[j] = deck[j],deck[i]
                else:
                    continue
            else:
                continue    
    return deck

print(shuffle_by_suit(build_standard_deck()))

                
                    
                

