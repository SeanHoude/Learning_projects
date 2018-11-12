import random
import os


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
        print(f"The dealers top card is a {self.hand[1]}.")

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

    def clearscreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def initial_deal(self):
        self.dealer.hand.clear()
        self.player.hand.clear()
        for i in range(2):
            self.dealer.hand.append(self.deck.draw_card())
            self.player.hand.append(self.deck.draw_card())
        self.show_dealer_top_card()
        self.get_score(self.player)

    def hit(self, player):
        player.hand.append(self.deck.draw_card())
        print(f"a {player.hand[-1]} was drawn.")

    def display_hand(self):
        print(f"Your current hand is {self.player.hand}.")

    def hit_or_stay(self):
        choice = None
        while not (choice == 'h' or choice == 's'):
            if choice is not None:
                print("I didn't understand that, please try again.")
            choice = input("Would you like to (h)it or (s)tay?: ").lower()
        return choice == 'h'

    def place_bet(self):
        print(f"You currently have {self.chips} chips.")
        self.bet = None
        while not isinstance(self.bet, int):
            # if self.bet is not None:
            #     print("That is an invalid choice. Please try again")
            self.bet = input(f"Please place a bet (0 - {self.chips}): ")
            try:
                self.bet = int(self.bet)
                if self.bet >= 0 and self.bet <= self.chips:
                    print(f"You bet {self.bet} chips on this round.")
                    self.chips -= self.bet
                else:
                    self.bet = None
                    print("You can't bet that number of chips!")
                    continue
            except:
                print("That's not a valid answer!")
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

    def dealer_turn(self):
        while self.get_score(self.dealer) < self.get_score(self.player):
            self.hit(self.dealer)

    def determine_winner(self):
        print(f"The dealer has {self.get_score(self.dealer)} with a hand of {self.dealer.hand}.")
        if self.get_score(self.dealer) > 21 or self.get_score(self.player) > self.get_score(self.dealer):
            print('You won the round!!')
            self.chips += (self.bet * 2)
        else:
            print("The dealer won this round.")

    def play_again(self):
        choice = None
        while not (choice == 'y' or choice == 'n'):
            if choice is not None:
                print("I didn't understand that, please try again.")
            choice = input("Would you like to play again? (y/n): ").lower()
        return choice == 'y'

    # def display(self):
    #     self.clearscreen(self)
    #     print(f"Current bet: {self.bet}")
    #     print(f"Chips remaining: {self.chips}")
    #     print(f"")
    #     print(f"")

    def play_blackjack(self):
        while self.chips > 0:
            self.place_bet()
            self.initial_deal()
            self.display_hand()
            busted = False
            while self.hit_or_stay():
                self.hit(self.player)
                print(f"Your current score is {self.get_score(self.player)}")
                busted = self.is_bust(self.player)
                if busted:
                    break
            if not busted:
                self.dealer_turn()
                self.determine_winner()
        print("Looks like you're all out of chips! ")
        if self.play_again():
            self.chips = 1000
            self.play_blackjack()
        else:
            print("Thanks for playing!")

blackjack = Game()
blackjack.play_blackjack()
