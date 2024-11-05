# Snakes and Ladders

This is a simple command-line implementation of the classic **Snakes and Ladders** game in Python. It allows two players to roll a die and move their positions on a board from square 1 to square 42, with random snakes and ladders along the way. The goal is to be the first to reach or exceed square 42.

## Features

- **Two-player mode**: Alternating turns between Player 1 and Player 2.
- **Snakes**: Landing on a snake moves the player down to a lower square.
- **Ladders**: Landing on a ladder moves the player up to a higher square.
- **Automatic dice roll**: Each player rolls a six-sided die on their turn.

## Game Rules

1. Each player starts at square 1.
2. On each turn, the player rolls a six-sided die (simulated by `roll_dice()`).
3. The player moves forward by the number rolled.
4. If the player lands on a square with a **snake**, they slide down to a lower square.
5. If the player lands on a square with a **ladder**, they climb up to a higher square.
6. The first player to reach or exceed square 42 wins.

## Code Overview

### Snakes and Ladders Positions

Snakes and ladders are defined as dictionaries:
- **Snakes** move the player down:
  ```python
  snakes = {
      13: 3,
      10: 6,
      30: 9,
      35: 21,
      41: 24
  }

- **Ladders** move the player up:
ladders = {
    2: 15,
    7: 28,
    14: 27,
    25: 38,
    19: 32
}

## Main Functions

roll_dice(): Simulates rolling a six-sided die and returns a random integer between 1 and 6.
move_position(roll, player_position): Updates the player's position based on the dice roll and checks if they landed on a snake or ladder.
play_game(): Alternates turns between the two players until one reaches square 42 or above, indicating a win.