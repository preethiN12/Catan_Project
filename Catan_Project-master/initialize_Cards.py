
#creating cards
def initialize_Cards(type):
    deck = []
    for i in range (19):
        deck.append(type)
    return deck
initialize_Cards("grain")
initialize_Cards("wool")
initialize_Cards("lumber")
initialize_Cards("brick")
initialize_Cards("ore")