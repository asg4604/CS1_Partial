import random
def make_card_deck():
    deck = []
    for card_num in range(1, 10):
        deck += [card_num] * 4
    return deck + 16 * [10]

def main():
    deck = make_card_deck()
    shuffled_deck = random.shuffle(deck)
    while len(deck) > 0:
        input("Press enter for a new card:")
        print(deck.pop())    
    pass

if __name__ == "__main__": 
    main()

