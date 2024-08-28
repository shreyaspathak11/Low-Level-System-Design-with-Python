from GameStatus import GameStatus
from Player import Player
from Game_Already_Started_Exception import GameAlreadyStartedException
from collections import deque

class Game:
    def __init__(self, board, dice):
        self.board = board
        self.dice = dice
        self.players = deque()
        self.status = GameStatus.NOT_STARTED

    def start_game(self):
        self.status = GameStatus.IN_PROGRESS
        self.board.print_board()

        while len(self.players) > 1:
            player = self.players.popleft()
            self.make_move(player)

            if player.position == self.board.get_size():
                player.won = True
                print(f'{player.name} has won the game')
                break
            else:
                self.players.append(player)

        self.status = GameStatus.FINISHED

    def make_move(self, player):
        print()
        print(f"{player.name}'s turn")
        input('Press any key to roll the dice')

        player_position = player.get_position()
        roll_value = self.dice.rollDice()
        new_position = player_position + roll_value

        if new_position > self.board.get_size():
            print(f'{player.name} rolled {roll_value} and cannot move')
            print('INVALID MOVE')
        else:
            if self.board.has_special_entity(new_position):
                special_entity = self.board.get_special_entity(new_position)
                print(f'{player.name} rolled {roll_value} and landed on {special_entity.getID()}')
                new_position = special_entity.get_end_position()
            print(f'{player.name} moved to {new_position}')
            player.position = new_position  # Update the player's position


    def add_player(self, player: Player):
        if self.status == GameStatus.IN_PROGRESS:
            raise GameAlreadyStartedException()
        self.players.append(player)