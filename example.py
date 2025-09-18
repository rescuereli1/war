#!/usr/bin/env python3
"""
Example usage of the War Card Game

This script demonstrates different ways to use the War game implementation.
"""

from war_game import WarGame, Card, Deck, Player


def quick_game_demo():
    """Demonstrate a quick game between two players."""
    print("=== Quick Game Demo ===")
    game = WarGame("Player A", "Player B")
    winner = game.play_game(verbose=False)
    print(f"Winner: {winner} after {game.round_count} rounds!")
    print()


def verbose_game_demo():
    """Demonstrate a detailed game with full output."""
    print("=== Verbose Game Demo ===")
    game = WarGame("Alice", "Bob")
    winner = game.play_game(verbose=True)
    print()


def card_demo():
    """Demonstrate Card and Deck functionality."""
    print("=== Card and Deck Demo ===")
    
    # Create and display some cards
    card1 = Card("Hearts", "Ace")
    card2 = Card("Spades", "King")
    print(f"Card 1: {card1} (value: {card1.value})")
    print(f"Card 2: {card2} (value: {card2.value})")
    print(f"Ace beats King: {card1.value > card2.value}")
    print()
    
    # Create and shuffle a deck
    deck = Deck()
    print(f"Full deck created with {len(deck.cards)} cards")
    
    # Deal some cards
    print("Top 5 cards from shuffled deck:")
    for i in range(5):
        card = deck.deal_card()
        if card:
            print(f"  {i+1}. {card}")
    print()


def custom_game_demo():
    """Demonstrate creating a custom game setup."""
    print("=== Custom Game Demo ===")
    
    # Create players with custom names
    player1 = Player("Emma")
    player2 = Player("Oliver")
    
    # Create a game with custom settings
    game = WarGame(player1.name, player2.name)
    
    print(f"Created game between {game.player1.name} and {game.player2.name}")
    winner = game.play_game(verbose=False)
    print(f"Game result: {winner} wins!")
    print()


def main():
    """Run all demonstrations."""
    print("War Card Game - Examples and Demonstrations")
    print("=" * 50)
    print()
    
    # Run different types of demos
    card_demo()
    quick_game_demo()
    custom_game_demo()
    
    # Ask if user wants to see a verbose game
    try:
        response = input("Would you like to see a detailed game? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            verbose_game_demo()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting demonstrations.")
    
    print("Thank you for trying the War Card Game!")


if __name__ == "__main__":
    main()