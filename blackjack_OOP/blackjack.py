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
        self.chips = 1000
        self.bet = 0

    def initial_deal(self):
        for i in range(2):
            self.dealer.hand.append(self.deck.draw_card())
            self.player.hand.append(self.deck.draw_card())

    def hit(self, player):
        player.hand.append(self.deck.draw_card())
        print(f"a {player.hand[-1]} was drawn")

    def display_hand(self):
        print(f"Your current hand is {self.player.hand}")

    def hit_or_stay(self):
        choice = None
        while not (choice == 'h' or choice == 's'):
            if choice is not None:
                print("I didn't understand that, please try again")
            choice = input("Would you like to (h)it or (s)tay?: ").lower()
        return choice == 'h'

    def place_bet(self):
        print(f"You currently have {self.chips} chips")
        self.bet = None
        while not isinstance(self.bet, int):
            if self.bet is not None:
                print("I didn't understand that, please try again")
            bet = input(f"Please place a bet (0 - {self.chips}): ")
            try:
                self.bet = int(bet)
                print(f"You bet {self.chips} chips on this round.")
                self.chips -= self.bet
            except:
                continue

    def show_dealer_top_card(self):
        self.dealer.dealer_top_card()

    def get_score(self, player):
        score = sum([card.get_value() for card in player.hand])
        has_ace = [card.get_value() for card in player.hand if card.rank == 'Ace']
        if has_ace and score <= 11:
            score += 10
        return score

    def is_bust(self, player):
        is_busted = self.get_score(player) > 21
        if is_busted:
            print('You busted!')
        return is_busted

    def determine_winner(self):
        print(f"The dealer has {self.get_score(self.dealer)} with a hand of {self.dealer.hand}")
        if self.get_score(self.player) > self.get_score(self.dealer):
            print('You won the round!!')
            self.chips += (self.bet * 2)
        else:
            print("The dealer wins this round")

    def play_blackjack(self):
        while self.chips > 0:
            self.place_bet()
            self.initial_deal()
            self.show_dealer_top_card()
            self.display_hand()
            while self.hit_or_stay():
                self.hit(self.player)
                print(f"Your current score is {self.get_score(self.player)}")
                busted = self.is_bust(self.player)
                if busted:
                    break
            if not busted:
                self.determine_winner()
        if play_again():
            self.chips = 1000
            play_blackjack(self)
        else:
            print("Thanks for playing!")

blackjack = Game()
blackjack.play_blackjack()
