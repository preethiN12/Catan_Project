import random
development = ['k','k','k','k','k','k','k','k','k','k','k','k','k','k','v','v','v','v','v','y','y','m','m','r','r']
readable = {'k':"knight card",'v':"victory point",'y':"year of plenty",'m':"monopoly",'r':'road building'}
def shuffle_development(deck):
    random.shuffle(deck)
    return deck

def human_readable(deck):
    top_card = deck.pop(0)
    if top_card in readable:
        return readable[top_card]

#shuffle_development(development)
#print(development)
#print(human_readable(development))
