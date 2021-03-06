import random
from pprint import pprint


class Deck:
    face_cards = ["Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Clubs", "Diamonds", "Heart"]

    def __init__(self, amount_of_cards = 36, suits=suits, face_cards=face_cards):
        self.cards = {}
        self.suits = suits
        for each_suit in self.suits:
            # Setup the Ace - can be either 11 | 1
            self.cards[f"{face_cards[3]} of {each_suit}"] = 11
            for card in range(2, amount_of_cards // (len(self.suits)) + 2):
                # applicable only for 36 cards decks:
                if card > 5:
                    self.cards[f"{card} of {each_suit}"] = card
                elif card < 5:
                    self.cards[f"{face_cards[card - 2]} of {each_suit}"] = card


class Player:

    def __init__(self, name, hand={}, score=0):
        self.name = name
        self.hand = hand
        self.score = score
        self.status = ""


class Game:

    def __init__(self, deck, *players):
        self.deck = deck
        self.players = players

    @staticmethod
    def check_player_busted(player):
        """
        :param player:
        :return: player status
        """
        if player.score > 21:
            player.status = "busted"
        return player.status

    def draw_card(self, player):
        drawn_card = random.choice(list(self.deck.cards))
        player.hand.update({drawn_card : self.deck.cards[drawn_card]})
        player.score += self.deck.cards[drawn_card]
        self.deck.cards.pop(drawn_card)
        return player.hand, player.score


    def prompt(self, player):
        query = input("Would you like to draw a card? (Y/N) ").upper()
        if query == "N":
            player.status = "resigned"
        elif query == "Y":
            self.draw_card(player)
            print(player.name, player.hand, player.score)
        else:
            print("Invalid input, try again ")

    def play_round(self, player):
        while player.status == "active":
            if self.check_player_busted(player) != "busted":
                self.prompt(player)

    def start(self):
        for player in self.players:
            player.status = "active"
            self.play_round(player)


russian_deck = Deck(36)
player_1 = Player("Vasya")
player_2 = Player("Kolya", 9, 27)


def main():
    first_game: Game = Game(russian_deck, player_1, player_2)
    print(player_1.name, player_1.hand)
    print(russian_deck.cards)

    for person in first_game.players:
        print(person.hand, person.status)

    first_game.start()

    for person in first_game.players:
        print(person.name, person.hand, person.score, person.status, first_game.check_player_busted(person))
    pprint(russian_deck.cards)


if __name__ == "__main__":
    main()
