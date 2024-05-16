import random
import matplotlib.pyplot as plt
import numpy as np

class Card:
    SUITS = ["♣️", "♦️", "♥️", "♠️"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    def __gt__(self, other):
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __eq__(self, other):
        return self.rank == other.rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]
        self._cards = tuple(cards)

    def shuffle(self):
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

# Hand class with the cards property fixed
class Hand:
    def __init__(self, deck):
        cards = []
        for i in range(5):
            cards.append(deck.cards[i])
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    @property
    def is_3_kind(self):
        ranks = [card.rank for card in self.cards]
        for rank in set(ranks):  # Using set to minimize unnecessary checks
            if ranks.count(rank) == 3:
                return True
        return False

# Simulation setup
num_iterations = 30000
three_of_a_kind_count = 0
probabilities = []

# Simulation execution
for i in range(1, num_iterations + 1):
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    if hand.is_3_kind:
        three_of_a_kind_count += 1
    probability = (three_of_a_kind_count / i) * 100
    probabilities.append(probability)

# Final probability output
final_probability = probabilities[-1]
print(f"The final computed probability of drawing a Three of a Kind is approximately {final_probability:.4f}%")

# Plotting the probability over iterations
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_iterations + 1), probabilities)
plt.title('Probability of Drawing a Three of a Kind Over Time')
plt.xlabel('Number of Draws')
plt.ylabel('Probability (%)')
plt.grid(True)
plt.show()
