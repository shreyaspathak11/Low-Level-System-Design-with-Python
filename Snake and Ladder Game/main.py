from Player import Player
from Game import Game
from Snake import Snake
from Ladder import Ladder
from Dice import Dice
from Board import Board

def main():
    snake1 = Snake(12, 28)
    snake2 = Snake(34, 78)
    snake3 = Snake(6, 69)
    snake4 = Snake(65, 84)

    ladder1 = Ladder(24, 56)
    ladder2 = Ladder(43, 83)
    ladder3 = Ladder(3, 31)
    ladder4 = Ladder(72, 91)

    board = Board(10)
    board.add_special_entity(snake1)
    board.add_special_entity(snake2)
    board.add_special_entity(snake3)
    board.add_special_entity(snake4)

    board.add_special_entity(ladder1)
    board.add_special_entity(ladder2)
    board.add_special_entity(ladder3)
    board.add_special_entity(ladder4)

    dice = Dice(6)

    print("Welcome to Snake and Ladder Game")
    print("Developed by: Shreyas Pathak")
    print("Version: 1.0")
    print()

    n = int(input("Enter number of players: "))

    game = Game(board, dice)  # Create an instance of Game with board and dice

    for i in range(n):
        name = input(f"Enter player no. {i+1} name: ")
        player = Player(name)
        game.add_player(player)  # Use the game instance to add players
    
    print("Let's start the game!!")
    game.start_game()  # Use the game instance to start the game

if __name__ == '__main__':
    main()

