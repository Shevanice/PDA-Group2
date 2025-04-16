"""
Maze Game - Deanna Brown
Date: [April 16]

Description:
A maze game where the player should must avoid monsters 😈 and  get the cat🐱  home safely 🏠.
Includes features such as dice roll, movement logic, obstacle collision, and analytics tracking.

A die will be rolled given the player to move up to 1-6 places to reach their destination.
Each time the die is rolled the player must specify which way they would like to go with the aim of
having the smalles amount of moves.

"""

import random
import sys
import maze_analytics

"""
ANSI escape codes for terminal text coloring.

Each variable stores an escape code that sets the foreground (text) color in the terminal.
These are used to enhance user experience by providing visual cues such as:
Source Reference:
- ANSI escape codes: https://en.wikipedia.org/wiki/ANSI_escape_code
"""

RESET = "\033[0m"
GRAY = "\033[90m"
WHITE = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"
PURPLE = "\033[95m"

# Define a base class Character that holds common attributes and behavior for both Player and Monster
class Character:
    def __init__(self, name, symbol, position):

        self.name = name
        
        self.symbol = symbol
   
        self.position = position
    # A method that allows the character to move to a new position in the maze
    def move(self, new_position):
        self.position = new_position

class Player(Character):
    def __init__(self, position=[1,1]):
        # Call the parent class (Character) constructor with specific attributes
        super().__init__('Cat', '🐱', position)


class Monster(Character):
    def __init__(self, position):
        # Call the parent constructor with the name 'Monster' and symbol '😈'
        super().__init__('Monster', '😈', position)

        

maze_grid = [
    ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
    ['W','S',' ',' ','W',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','W'],
    ['W',' ','W',' ','W',' ','W','W',' ','W',' ','W','W','W','W',' ',' ','W'],
    ['W',' ','W',' ',' ',' ','W',' ',' ',' ',' ',' ',' ',' ','W',' ','W','W'],
    ['W',' ','W','W','W','W','W',' ','W','W','W',' ','W',' ','W',' ',' ','W'],
    ['W',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','W',' ',' ',' ','W','W'],
    ['W',' ','W','W','W',' ','W','W','W',' ','W',' ','W','W','W',' ',' ','W'],
    ['W',' ',' ',' ','W',' ',' ',' ','W',' ','W',' ',' ',' ',' ','W',' ','W'],
    ['W','W','W',' ','W','W','W',' ','W',' ','W','W','W','W',' ','W',' ','W'],
    ['W',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','W',' ',' ',' ','W'],
    ['W',' ','W','W','W','W','W','W','W','W','W','W',' ','W','W','W',' ','W'],
    ['W',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','E'],
    ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W']
]

monster_positions = [[4, 4], [2, 9], [10, 6], [10, 14]]
monsters = [Monster(pos) for pos in monster_positions]

player = Player([1, 1])
scores = []   # Moves when the player wins
losses = []   # Moves when the player loses

for i, row in enumerate(maze_grid):
    for j, cell in enumerate(row):
        if cell == 'S':
            player.position = [i, j]

def display_maze():
    for i, row in enumerate(maze_grid):
        line = ""
        for j, cell in enumerate(row):
            if [i, j] == player.position:
                line +=  player.symbol + RESET
                
            elif any(mon.position == [i, j] for mon in monsters):
                line += PURPLE + "😈" + RESET
            elif cell == 'W':
                line += GRAY + "⬛" + RESET
            elif cell == 'S':
                line += GREEN + "🚩" + RESET
            elif cell == 'E':
                line += RED + "🏠" + RESET
            else:
                line += WHITE + "⬜" + RESET
        print(line)
    print()

def move_player(direction, steps):
    
    """
    Moves the player in the specified direction by a number of steps.

    Handles:
    - Out-of-bounds checks
    - Wall collision
    - Monster detection

    Source references:
    - Tuple/list operations: https://docs.python.org/3/tutorial/datastructures.html
    - String input validation: https://docs.python.org/3/tutorial/errors.html
    """
    
    moves = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
    if direction not in moves:
        return None  # Indicates invalid move

    for _ in range(steps):
        new_pos = [player.position[0] + moves[direction][0], player.position[1] + moves[direction][1]]

        # First check for out-of-bounds
        if not (0 <= new_pos[0] < len(maze_grid) and 0 <= new_pos[1] < len(maze_grid[0])):
            print("Out of bounds!")
            break

        # Then check if monster is at the new position (before wall check!)
        if any(mon.position == new_pos for mon in monsters):
            player.move(new_pos)
            display_maze()
            print(RED + "You encountered a monster! Game Over." + RESET)
            return False  # End game round

        # Then check for wall
        if maze_grid[new_pos[0]][new_pos[1]] == 'W':
            print("You hit a wall!")
            break

        # Otherwise valid move
        player.move(new_pos)

    return True

def show_analytics():
    total_games = len(scores) + len(losses)
    print("\nGame Analytics:")
    print(f"Total Games Played: {total_games}")
    print(f"Games Won: {len(scores)}")
    print(f"Games Lost: {len(losses)}")

    if scores:
        print(f"Average Moves (Wins Only): {maze_analytics.calc_mean(scores)}")
        print(f"Best Score (Fewest Moves): {maze_analytics.calc_min(scores)}")
        print(f"Worst Score (Most Moves): {maze_analytics.calc_max(scores)}")
        print(f"Range of Winning Scores: {maze_analytics.calc_range(scores)}")
    else:
        print("No wins yet. Keep trying!")

def play_maze():
    global player
    player = Player([1, 1])
    moves_taken = 0
    print("----------------------------------------------------------------------------")
    print( PURPLE +"Welcome to the Cat Maze\n" + RESET)   
    print( PURPLE +"Help the cat 🐱 find its way home 🏠!" + RESET)
    print("----------------------------------------------------------------------------")

    while maze_grid[player.position[0]][player.position[1]] != 'E':
        display_maze()
        dice_roll = random.randint(1, 6)
        print(f"🎲 You rolled a {dice_roll}! You can move {dice_roll} steps.")

        direction = None
        while direction is None:
            move = input("Move (up, down, left, right): ").strip().lower()
            result = move_player(move, dice_roll)

            if result is None:
                print("Invalid direction! Please try again.")
            elif result is False:  # Player hit monster
                print(RED + f"You lost in {moves_taken} moves." + RESET)
                return moves_taken, False
            else:
                direction = move
                moves_taken += 1

    display_maze()
    print("----------------------------------------------------------------------------")
    print(GREEN + f"Congratulations! You've brought the cat home in {moves_taken} moves! 🐱🏠" + RESET)
    print("----------------------------------------------------------------------------")
    return moves_taken, True




def prompt_replay():
    while True:
        choice = input("\nPlay again? (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            print("Thanks for playing!")
            return False
        else:
            print("Invalid input, please type yes or no.")


def main():
    while True:
        moves, won = play_maze()

        if won:
            scores.append(moves)
        else:
            losses.append(moves)

        show_analytics()

        if not prompt_replay():
            break

if __name__ == "__main__":
    main()
