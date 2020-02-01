import random


class Deck:

    face_cards = ["Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Clubs", "Diamonds", "Heart"]

    def __init__(self, amount_of_cards=36, suits=suits, face_cards=face_cards):
        self.cards = {}
        self.suits = suits
        for each_suit in self.suits:
            for card in range(2, amount_of_cards//(len(self.suits)) + 2):
                # applicable only for 36 cards decks:
                if card > 5:
                    self.cards[f"{card} of {each_suit}"] = card
                elif card < 5:
                    self.cards[f"{face_cards[card - 2]} of {each_suit}"] = card


class Player:

    def __init__(self, name, hand=[], score=0):
        self.name = name
        self.hand = hand
        self.score = score
        self.status = ""


class Game:

    def __init__(self, deck, *players):
        self.deck = deck
        self.players = players

    def check_player_busted(self):
        if self.player.score > 21:
            player.status = "BUSTED"
            return player.status

    def start(self):
        for player in self.players:
            player.status = "active"


russian_deck = Deck(36)
player_1 = Player("Vasya")
player_2 = Player("Kolya", 9, 7)

def main():

    o4ko = Game(russian_deck, player_1, player_2)
    print(player_1.name, player_1.hand)
    print(russian_deck.cards, player_2.name, player_2.hand)

    for person in o4ko.players:
        print(person.hand, person.status)

    o4ko.start()

    for person in o4ko.players:
        print(person.hand, person.status)


if __name__ == "__main__":
    main()
