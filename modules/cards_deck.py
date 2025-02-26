import random

STANDARD_52_DECK: dict = {
    "suits": ["Hearts", "Spades", "Diamonds", "Clubs"],
    "rank_range": (2, 15),
    "face_cards": {
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
    },
    "scores": {
        11: 10,
        12: 10,
        13: 10,
        14: 11,
    },
}


class Card(object):
    def __init__(self, value: int, suit: str, rank: str, score: int | None):
        self.value = value
        self.suit = suit
        self.rank = rank
        self.score = score

    def show(self):
        print(f"{self.rank} of {self.suit} (score: {self.score})")


class Stack(object):
    def __init__(self):
        self.cards = []

    def get(self):
        return self.cards

    def size(self):
        return len(self.cards)

    def draw(self, index: int = -1):
        return self.cards.pop(index)

    def insert(self, card: Card, index: int = 0):
        self.cards.insert(index, card)

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]


class Deck(Stack):
    def __init__(
        self,
        values: list[int] = list(
            range(
                STANDARD_52_DECK["rank_range"][0],
                STANDARD_52_DECK["rank_range"][1],
            )
        ),
        suits: list[str] = STANDARD_52_DECK["suits"],
        face_cards: dict[int, str] = STANDARD_52_DECK["face_cards"],
        scores: dict[int, int] = STANDARD_52_DECK["scores"],
    ):
        self.cards = []
        self.values = values
        self.suits = suits
        self.face_cards = face_cards
        self.scores = scores
        self.build()

    def build(self):
        for suit in self.suits:
            for value in self.values:
                rank = (
                    self.face_cards.get(value)
                    if value in self.face_cards.keys()
                    else value
                )
                score = self.scores.get(value) if value in self.scores.keys() else value
                self.cards.append(
                    Card(value=value, suit=suit, rank=str(rank), score=score)
                )


class Hand(Stack):
    def __init__(self, name: str):
        self.cards = []
        self.name = name


if __name__ == "__main__":
    deck = Deck()
    # deck.shuffle()
    print(deck.size())
    # for i in range(5):
    #     card = deck.draw()
    #     print(deck.size())
    #     deck.insert(card)
    # print("\nDeck after insert:")
    table = Hand("Table")
    print(table.name)
    print(table.size())
