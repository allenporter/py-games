#!/usr/bin/python3
"""Bathtub Solitaire.

Bathtub Solitaire is a solitaire card game that is played with a standard 52-card deck. 

Rules:
- If less than 4 cards turned over, draw until 4 cards
- If first and last are same number, discard all 4
- If first and last are same suit, discard middle 2
- Repeat until deck is done
"""

import random
from dataclasses import dataclass
from colorist import Color, BgColor
import numpy as np


@dataclass
class Card:
    suit: str
    number: str

    def __repr__(self) -> str:
        if self.suit in ["♥", "♦"]:
            return f"{Color.RED}{self.suit}{self.number}{Color.OFF}"
        return f"{Color.BLUE}{self.suit}{self.number}{Color.OFF}"


def create_deck() -> list[Card]:
    """Create a standard 52-card deck."""
    suits = ["♠", "♣", "♥", "♦"]
    cards = []
    for suit in suits:
        for number in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            cards.append(Card(suit, number))
    return cards


def render_state(hand: list[Card], deck: list[Card]) -> str:
    """Render the state of the game."""
    return f"({len(hand):2d}.{len(deck):2d}): {hand}"


def play_game() -> int:
    """Play the game and return the number of cards left in the hand."""
    deck = create_deck()
    random.shuffle(deck)

    hand = []
    draw = False
    while deck:
        while len(hand) < 4 or draw:
            if not deck:
                break
            draw = False
            state = render_state(hand, deck)
            #print(f"{state}: {BgColor.MAGENTA}[Draw]{BgColor.OFF}")
            hand.insert(0, deck.pop())
        
        while len(hand) >= 4:
            state = render_state(hand, deck)
            if hand[0].number == hand[3].number:
                #print(f"{state}: {BgColor.GREEN}[Drop 4]{BgColor.OFF}")
                hand.pop(0)
                hand.pop(0)
                hand.pop(0)
                hand.pop(0)
            elif hand[0].suit == hand[3].suit:
                #print(f"{state}: {BgColor.CYAN}[Drop mid 2]{BgColor.OFF}")
                hand.pop(1)
                hand.pop(1)
            else:
                break
        draw = True

    assert not deck
    state = render_state(hand, deck)
    #print(f"{state}: {BgColor.RED}[END]{BgColor.OFF}")
    return len(hand)


def main() -> None:
    total = 0
    winners = 0
    history = []
    for _ in range(0, 100000):
        cards_left = play_game()
        #print(f"Cards left: {cards_left}")
        #print("----------------------")
        if cards_left == 0:
            winners += 1
        total += 1
        history.append(cards_left)

    ratio = (winners / total)
    print(f"Winners: {winners} Total: {total} Win Rate: {(ratio)*100:0.2}%" )
    # Calculate 1 out of N chances
    chance = int(1 / ratio)
    print(f"1 in {chance} chance of winning")



if __name__ == "__main__":
    main()