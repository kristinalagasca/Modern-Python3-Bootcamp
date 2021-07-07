from random import shuffle as sh


class Card:
    """
    OOP Exercise — Deck of Cards
    Specifications

    Card:
    1. Each instance of Card should have a suit
    2. Each instance of Card should have a value
    3. Card's __repr__ method should return the card's value and suit
    """
    def __init__(self, value, suits):
        self.value = value
        self.suits = suits

    def __repr__(self):
        return f"{self.value} of {self.suits}"


class Deck:
    """
    Deck:
    1. Each instance of Deck should have a cards attribute with all 52 possible instances of Card.
    2. Deck should have an instance method called count which returns a count of how many cards remain in the deck.
    3. Deck's __repr__  method should return information on how many cards are in the deck
    4. Deck should have an instance method called _deal which accepts a number and removes at most that many cards
    from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!).
    If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
    5. Deck should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards
    missing from the deck, this method should raise a ValueError  with the message "Only full decks can be shuffled".
    shuffle should return the shuffled deck.
    6. Deck should have an instance method called deal_card  which uses the _deal method to deal a single card from the
    deck and return that single card.
    7. Deck should have an instance method called deal_hand which accepts a number and uses the _deal method to deal a
    list of cards from the deck and return that list of cards.
    """
    def __init__(self):                 # 1
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(v, suit) for suit in suits for v in value]

    def __repr__(self):                 # 3
        return f"Deck of {self.count()} cards"

    def count(self):                    # 2
        return len(self.cards)

    def _deal(self, num):               # 4
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt.")
        card = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return card

    def shuffle(self):                  # 5
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled!")
        sh(self.cards)
        return self

    def deal_card(self):                # 6
        return self._deal(1)[0]

    def deal_hand(self, hand_size):     # 7
        return self._deal(hand_size)


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(hand)
card3 = d.deal_card()
print(card3)
# print(d.cards)
