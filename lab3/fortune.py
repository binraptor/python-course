#!/usr/bin/env python3

def fortune_telling(n):
    deck = cards.CardDeck()
    deck.shuffle()
    card = deck.draw(n)

    print("Your fortune:")
    for i in card:
        print(f"- {i.rank} of {i.suit}")


def main(args):
    n = int(input("Enter the number of cards to draw: "))
    fortune_telling(n)


if __name__ == '__main__':
    import sys
    import cards

    main(sys.argv)

