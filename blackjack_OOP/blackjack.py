import random


# Generates cards based on the num of decks specified, then shuffles it once. Has a draw card method
class Deck:
    def __init__(self, num_decks=1):
        ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.cards *= num_decks
        random.shuffle(self.cards)

    def __str__(self):
        return str([str(card) for card in self.cards])

    # def __repr__(self):
        # return [card for card in self.cards]

    def draw_card(self):
        # random.shuffle(self.cards)
        return self.cards.pop()


# Holds suit and rank attributes for cards, and determines the score of each card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def get_value(self):
        if type(self.rank) == int:
            return self.rank
        elif self.rank == 'Ace':
            return 1
        else:
            return 10


# holds the cards in each players hand, calculates the score of the hand,
# and shows the portion of a hand the player is allowed to see
class Hand:
    def __init__(self):
        self.hand = []

    def dealer_top_card(self):
        print(f"The dealers top card is a {self.hand[0]}")

    # def __Str__(self):
    #     stringy = ", ".join([str(card) for card in self.hand])
    #     return 'asdasdaw'

    # def __repr__(self):
    #     # stringy = ", ".join([str(card) for card in self.hand])
    #     # return stringy
    #     return 'asda'


class Game:
    def __init__(self):
        self.deck = Deck(6)
        self.player = Hand()
        self.dealer = Hand()

    def initial_deal(self):
        for i in range(2):
            self.dealer.hand.append(self.deck.draw_card())
            self.player.hand.append(self.deck.draw_card())

    def hit(self, player):
        player.hand.append(self.deck.draw_card())
        print(f"a {player.hand[-1]} was drawn")

    # def show_dealer_top_card(self):
    #     self.dealer.dealer_top_card()

    # def deal_to_dealer(self, num=1):
    #     for i in range(num):
    #         self.dealer.hand.append(self.deck.draw_card())

    # def deal_to_player(self, num=1):
    #     for i in range(num):
    #         self.player.hand.append(self.deck.draw_card())

    def play_round(self):
        self.initial_deal()
        # show_dealer_top_card()
        self.dealer.dealer_top_card()
        hit(self.player)

blackjack = Game()

blackjack.play_round()
# print(blackjack.deck)