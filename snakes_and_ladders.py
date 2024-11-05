import random

snakes = {
    13: 3,
    10: 6,
    30: 9,
    35: 21,
    41: 24
}

ladders = {
    2: 15,
    7: 28,
    14: 27,
    25: 38,
    19: 32
}

player_one_position = {
    'position': 1
}

player_two_position = {
    'position': 1
}


def roll_dice() -> int:
    """Returns a random number on a six sided die"""
    return random.randint(1, 6)


def move_position(roll: int, player_position: dict) -> None:
    """Moves the players position based on roll accounting for snakes and ladders"""
    position = player_position['position'] + roll
    if position in snakes.keys():
        print("You landed on a snake!")
        position = snakes[position]
    elif position in ladders.keys():
        print("You landed on a ladder!")
        position = ladders[position]
    player_position['position'] = position


def play_game():
    """Game initiation function, alternates player turns"""
    players = [player_one_position, player_two_position]
    player_names = ["Player 1", "Player 2"]
    current_player = 0

    while True:
        input(
            f"{player_names[current_player]}'s turn! Press Enter to roll the dice...")

        roll = roll_dice()
        print(f"{player_names[current_player]} rolled a {roll}.")

        move_position(roll, players[current_player])
        print(
            f"{player_names[current_player]} is now on square {players[current_player]['position']}")

        if players[current_player]['position'] >= 42:
            print(f"{player_names[current_player]} wins!")
            break

        current_player = 1 - current_player


if __name__ == '__main__':
    play_game()
