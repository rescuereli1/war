# War Card Game

A Python implementation of the classic War card game. Two players compete by playing cards from their deck, with the higher card winning both cards. When cards have equal value, a "war" occurs where additional cards are played to determine the winner.

## Features

- Complete implementation of the War card game rules
- Support for custom player names
- Detailed game progress display (optional)
- Automatic handling of war situations
- Prevention of infinite games with round limits

## How to Play

War is a simple card game typically played by two players:

1. The deck is shuffled and divided evenly between two players
2. Each player simultaneously plays the top card from their deck
3. The player with the higher card wins both cards and adds them to the bottom of their deck
4. If both cards have the same value, a "war" occurs:
   - Each player places 3 cards face down, then 1 card face up
   - The player with the higher face-up card wins all the cards on the table
   - If the face-up cards are also equal, another war occurs
5. The game continues until one player has all the cards (or a round limit is reached)

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Usage

### Run the Interactive Game

```bash
python war.py
```

This will start an interactive game where you can:
- Enter custom player names
- Choose whether to see detailed game progress
- Watch the game play out automatically

### Use as a Library

```python
from war import WarGame

# Create a game with default player names
game = WarGame()
winner = game.play_game(verbose=True)
print(f"Winner: {winner}")

# Create a game with custom player names
game = WarGame("Alice", "Bob")
winner = game.play_game(verbose=False)  # Run silently
print(f"Winner: {winner}")
```

## Classes

### Card
Represents a playing card with a suit and rank. Cards have values from 2-14 (Ace high).

### Deck
A standard 52-card deck that can be shuffled and dealt from.

### Player
Represents a player with a hand of cards. Players can play cards and receive new cards.

### WarGame
The main game controller that handles game logic, rounds, and war situations.

## Example Output

```
Welcome to War Card Game!
==============================
Enter name for Player 1 (or press Enter for 'Player 1'): Alice
Enter name for Player 2 (or press Enter for 'Player 2'): Bob
Show detailed game progress? (y/n, default: y): y

Starting War game between Alice and Bob
Each player starts with 26 cards
--------------------------------------------------
Round 1: Alice plays 7 of Hearts, Bob plays K of Spades - Bob wins the round!
Alice: 25 cards, Bob: 27 cards

Round 2: Alice plays 3 of Diamonds, Bob plays 3 of Clubs - WAR!
 War resolved with 10 total cards.
Alice: 35 cards, Bob: 17 cards

...

==============================
Game Over! Winner: Alice
Total rounds played: 127
```

## Game Rules Implementation

- **Card Values**: 2=2, 3=3, ..., 10=10, J=11, Q=12, K=13, A=14
- **War Procedure**: When cards tie, each player puts down 3 cards face down and 1 face up
- **Insufficient Cards**: If a player doesn't have enough cards for a war, they use all remaining cards
- **Round Limit**: Games are limited to 1000 rounds to prevent infinite loops
- **Winner Determination**: Player with more cards when the game ends, or last player with cards

## License

This project is open source and available under the MIT License.