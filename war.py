#!/usr/bin/env python3
"""
War Card Game Implementation

A simple implementation of the classic War card game where two players
compete by playing cards from their deck. The player with the higher
card wins both cards. In case of a tie, a "war" occurs.
"""

import random
from typing import List, Tuple, Optional


class Card:
    """Represents a playing card with suit and rank."""
    
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    RANK_VALUES = {rank: idx + 2 for idx, rank in enumerate(RANKS)}
    
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self.RANK_VALUES[rank]
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self) -> str:
        return f"Card('{self.suit}', '{self.rank}')"


class Deck:
    """Represents a deck of playing cards."""
    
    def __init__(self):
        self.cards = []
        self._create_deck()
        self.shuffle()
    
    def _create_deck(self):
        """Create a standard 52-card deck."""
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)
    
    def deal_card(self) -> Optional[Card]:
        """Deal a card from the top of the deck."""
        return self.cards.pop() if self.cards else None
    
    def is_empty(self) -> bool:
        """Check if the deck is empty."""
        return len(self.cards) == 0


class Player:
    """Represents a player in the War game."""
    
    def __init__(self, name: str):
        self.name = name
        self.hand = []
    
    def add_cards(self, cards: List[Card]):
        """Add cards to the bottom of the player's hand."""
        self.hand.extend(cards)
    
    def play_card(self) -> Optional[Card]:
        """Play a card from the top of the hand."""
        return self.hand.pop(0) if self.hand else None
    
    def has_cards(self) -> bool:
        """Check if the player has cards."""
        return len(self.hand) > 0
    
    def card_count(self) -> int:
        """Return the number of cards in hand."""
        return len(self.hand)


class WarGame:
    """Main War game class."""
    
    def __init__(self, player1_name: str = "Player 1", player2_name: str = "Player 2"):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()
        self.round_count = 0
        self.max_rounds = 1000  # Prevent infinite games
        
    def deal_cards(self):
        """Deal cards evenly to both players."""
        while not self.deck.is_empty():
            card1 = self.deck.deal_card()
            card2 = self.deck.deal_card()
            if card1:
                self.player1.add_cards([card1])
            if card2:
                self.player2.add_cards([card2])
    
    def play_round(self) -> Tuple[bool, str]:
        """
        Play a single round of War.
        Returns (game_over, message)
        """
        if not self.player1.has_cards():
            return True, f"{self.player2.name} wins! {self.player1.name} is out of cards."
        
        if not self.player2.has_cards():
            return True, f"{self.player1.name} wins! {self.player2.name} is out of cards."
        
        self.round_count += 1
        if self.round_count > self.max_rounds:
            return True, f"Game ended after {self.max_rounds} rounds to prevent infinite loop."
        
        # Play cards
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()
        
        table_cards = [card1, card2]
        message = f"Round {self.round_count}: {self.player1.name} plays {card1}, {self.player2.name} plays {card2}"
        
        if card1.value > card2.value:
            # Player 1 wins
            self.player1.add_cards(table_cards)
            message += f" - {self.player1.name} wins the round!"
        elif card2.value > card1.value:
            # Player 2 wins
            self.player2.add_cards(table_cards)
            message += f" - {self.player2.name} wins the round!"
        else:
            # War!
            message += " - WAR!"
            war_cards = self._handle_war(table_cards)
            message += f" War resolved with {len(war_cards)} total cards."
        
        return False, message
    
    def _handle_war(self, table_cards: List[Card]) -> List[Card]:
        """
        Handle a war situation.
        Each player puts down 3 cards face down and 1 face up.
        """
        # Each player puts down 3 cards (or all remaining if less than 3)
        for _ in range(3):
            if self.player1.has_cards():
                card = self.player1.play_card()
                if card:
                    table_cards.append(card)
            
            if self.player2.has_cards():
                card = self.player2.play_card()
                if card:
                    table_cards.append(card)
        
        # Check if either player runs out of cards
        if not self.player1.has_cards() or not self.player2.has_cards():
            # Award all cards to player with cards remaining
            if self.player1.has_cards():
                self.player1.add_cards(table_cards)
            else:
                self.player2.add_cards(table_cards)
            return table_cards
        
        # Play the decisive cards
        war_card1 = self.player1.play_card()
        war_card2 = self.player2.play_card()
        table_cards.extend([war_card1, war_card2])
        
        if war_card1.value > war_card2.value:
            self.player1.add_cards(table_cards)
        elif war_card2.value > war_card1.value:
            self.player2.add_cards(table_cards)
        else:
            # Another war!
            table_cards = self._handle_war(table_cards)
        
        return table_cards
    
    def play_game(self, verbose: bool = True) -> str:
        """
        Play a complete game of War.
        Returns the winner's name.
        """
        self.deal_cards()
        
        if verbose:
            print(f"Starting War game between {self.player1.name} and {self.player2.name}")
            print(f"Each player starts with {self.player1.card_count()} cards")
            print("-" * 50)
        
        while True:
            game_over, message = self.play_round()
            
            if verbose:
                print(message)
                print(f"{self.player1.name}: {self.player1.card_count()} cards, "
                      f"{self.player2.name}: {self.player2.card_count()} cards")
                print()
            
            if game_over:
                if verbose:
                    print(message)
                
                # Determine winner
                if self.player1.card_count() > self.player2.card_count():
                    return self.player1.name
                elif self.player2.card_count() > self.player1.card_count():
                    return self.player2.name
                else:
                    return "Tie"


def main():
    """Main function to run the War game."""
    print("Welcome to War Card Game!")
    print("=" * 30)
    
    # Get player names
    player1_name = input("Enter name for Player 1 (or press Enter for 'Player 1'): ").strip()
    if not player1_name:
        player1_name = "Player 1"
    
    player2_name = input("Enter name for Player 2 (or press Enter for 'Player 2'): ").strip()
    if not player2_name:
        player2_name = "Player 2"
    
    # Ask for verbose mode
    verbose_input = input("Show detailed game progress? (y/n, default: y): ").strip().lower()
    verbose = verbose_input != 'n'
    
    print()
    
    # Create and play game
    game = WarGame(player1_name, player2_name)
    winner = game.play_game(verbose=verbose)
    
    print("=" * 30)
    print(f"Game Over! Winner: {winner}")
    print(f"Total rounds played: {game.round_count}")


if __name__ == "__main__":
    main()