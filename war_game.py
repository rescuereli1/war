#!/usr/bin/env python3
"""
War Card Game Implementation

A simple implementation of the classic War card game for two players.
"""

import random
from typing import List, Tuple


class Card:
    """Represents a playing card with suit and rank."""
    
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self.RANKS.index(rank) + 2  # 2 has value 2, Ace has value 14
    
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
    
    def deal_card(self) -> Card:
        """Deal one card from the top of the deck."""
        if self.cards:
            return self.cards.pop()
        return None
    
    def is_empty(self) -> bool:
        """Check if the deck is empty."""
        return len(self.cards) == 0


class Player:
    """Represents a player in the War card game."""
    
    def __init__(self, name: str):
        self.name = name
        self.hand = []
    
    def add_cards(self, cards: List[Card]):
        """Add cards to the bottom of the player's hand."""
        self.hand.extend(cards)
    
    def play_card(self) -> Card:
        """Play the top card from the player's hand."""
        if self.hand:
            return self.hand.pop(0)
        return None
    
    def has_cards(self) -> bool:
        """Check if the player has any cards left."""
        return len(self.hand) > 0
    
    def card_count(self) -> int:
        """Return the number of cards in the player's hand."""
        return len(self.hand)


class WarGame:
    """Main game class for the War card game."""
    
    def __init__(self, player1_name: str = "Player 1", player2_name: str = "Player 2"):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()
        self.round_count = 0
        self.max_rounds = 10000  # Prevent infinite games
    
    def deal_cards(self):
        """Deal cards evenly to both players."""
        while not self.deck.is_empty():
            # Deal alternating cards to each player
            card1 = self.deck.deal_card()
            card2 = self.deck.deal_card()
            
            if card1:
                self.player1.add_cards([card1])
            if card2:
                self.player2.add_cards([card2])
    
    def play_round(self) -> Tuple[bool, str]:
        """
        Play a single round of War.
        Returns (game_over, round_description)
        """
        if not self.player1.has_cards() or not self.player2.has_cards():
            return True, "Game Over - A player has no cards left!"
        
        self.round_count += 1
        
        # Check for maximum rounds to prevent infinite games
        if self.round_count > self.max_rounds:
            return True, f"Game ended after {self.max_rounds} rounds to prevent infinite play!"
        
        cards_in_play = []
        
        # Initial card play
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()
        
        if not card1 or not card2:
            return True, "Game Over - A player ran out of cards!"
        
        cards_in_play.extend([card1, card2])
        round_description = f"Round {self.round_count}: {self.player1.name} plays {card1}, {self.player2.name} plays {card2}"
        
        # Handle war (tie)
        while card1.value == card2.value:
            round_description += f" - WAR! (Both played {card1.rank})"
            
            # Each player plays 3 cards face down and 1 face up
            war_cards = []
            for _ in range(3):  # 3 cards face down
                war_card1 = self.player1.play_card()
                war_card2 = self.player2.play_card()
                
                if not war_card1 or not war_card2:
                    # A player ran out of cards during war
                    if war_card1:
                        cards_in_play.append(war_card1)
                    if war_card2:
                        cards_in_play.append(war_card2)
                    
                    winner = self.player1 if self.player1.has_cards() else self.player2
                    winner.add_cards(cards_in_play)
                    return True, round_description + " - Game Over during WAR!"
                
                war_cards.extend([war_card1, war_card2])
            
            # The face-up cards for war
            card1 = self.player1.play_card()
            card2 = self.player2.play_card()
            
            if not card1 or not card2:
                cards_in_play.extend(war_cards)
                if card1:
                    cards_in_play.append(card1)
                if card2:
                    cards_in_play.append(card2)
                
                winner = self.player1 if self.player1.has_cards() else self.player2
                winner.add_cards(cards_in_play)
                return True, round_description + " - Game Over during WAR!"
            
            cards_in_play.extend(war_cards)
            cards_in_play.extend([card1, card2])
            round_description += f" War cards: {self.player1.name} plays {card1}, {self.player2.name} plays {card2}"
        
        # Determine winner of this round
        if card1.value > card2.value:
            winner = self.player1
            round_description += f" - {self.player1.name} wins!"
        else:
            winner = self.player2
            round_description += f" - {self.player2.name} wins!"
        
        # Winner takes all cards in play
        random.shuffle(cards_in_play)  # Shuffle to add randomness
        winner.add_cards(cards_in_play)
        
        round_description += f" ({len(cards_in_play)} cards won)"
        round_description += f" | Cards remaining: {self.player1.name}: {self.player1.card_count()}, {self.player2.name}: {self.player2.card_count()}"
        
        return False, round_description
    
    def play_game(self, verbose: bool = True) -> str:
        """
        Play a complete game of War.
        Returns the name of the winner.
        """
        print("Starting War Card Game!")
        print("=" * 50)
        
        # Deal cards
        self.deal_cards()
        print(f"Cards dealt: {self.player1.name}: {self.player1.card_count()}, {self.player2.name}: {self.player2.card_count()}")
        print()
        
        game_over = False
        
        while not game_over:
            game_over, round_description = self.play_round()
            
            if verbose:
                print(round_description)
            
            # Check for winner
            if not self.player1.has_cards():
                print(f"\n🎉 {self.player2.name} wins the game!")
                print(f"Game lasted {self.round_count} rounds.")
                return self.player2.name
            elif not self.player2.has_cards():
                print(f"\n🎉 {self.player1.name} wins the game!")
                print(f"Game lasted {self.round_count} rounds.")
                return self.player1.name
        
        # If game ended due to max rounds, determine winner by card count
        if self.player1.card_count() > self.player2.card_count():
            print(f"\n🎉 {self.player1.name} wins by card count!")
            return self.player1.name
        elif self.player2.card_count() > self.player1.card_count():
            print(f"\n🎉 {self.player2.name} wins by card count!")
            return self.player2.name
        else:
            print("\n🤝 It's a tie!")
            return "Tie"


def main():
    """Main function to run the War card game."""
    print("Welcome to War Card Game!")
    print()
    
    # Create and play a game
    game = WarGame("Alice", "Bob")
    winner = game.play_game(verbose=True)
    
    print(f"\nFinal Result: {winner} is the winner!")


if __name__ == "__main__":
    main()