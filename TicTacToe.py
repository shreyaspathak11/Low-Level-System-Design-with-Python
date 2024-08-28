# Design Tic Tac Toe
class TicTacToe:
    def __init__(self, n: int) -> None:
        self.n = n
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
    
    def printBoard(self) -> None:
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end='')
                if j < self.n-1:
                    print(end=' | ')
            print()
            if i < self.n-1:
                print('---' * self.n)
    
class Game:
    def __init__(self, ) -> None:
        self.ticTacToe = TicTacToe(3)
        self.players = {}
        self.player1 = 'X'
        self.player2 = 'O'
        

    def addPlayer(self) -> None:
        for i in range(2):
            name = input(f'Enter player{i+1} name: ')
            if i == 0:
                self.players['X'] = name  
            else:
                self.players['O'] = name
        print(f'player1: {self.players[self.player1]} is {self.player1} and player2: {self.players[self.player2]} is {self.player2}')

    def switchPlayer(self, player: str) -> str:
        print(f'switching player from {player} to {self.player1 if player == self.player2 else self.player2}')
        return self.player1 if player == self.player2 else self.player2
    
    def makeMove(self, player: str, row: int, col: int) -> bool:
        if self.ticTacToe.board[row][col] == ' ':
            self.ticTacToe.board[row][col] = player
            return True
        return False

    def checkMove(self, row: int, col: int) -> bool:
        if row < 0 or row >= self.ticTacToe.n or col < 0 or col >= self.ticTacToe.n:
            print('Please make a valid move')
            return False
        if self.ticTacToe.board[row][col] != ' ':
            print('Please make a valid move')
            return False
        return True
    
    def checkWin(self, player: str) -> bool:
        n = self.ticTacToe.n
        # Check rows and columns
        for i in range(n):
            if all(self.ticTacToe.board[i][j] == player for j in range(n)) or \
               all(self.ticTacToe.board[j][i] == player for j in range(n)):
                return True
        # Check diagonals
        if all(self.ticTacToe.board[i][i] == player for i in range(n)) or \
           all(self.ticTacToe.board[i][n - 1 - i] == player for i in range(n)):
            return True
        return False

    def checkDraw(self) -> bool:
        for i in range(self.ticTacToe.n):
            for j in range(self.ticTacToe.n):
                if self.ticTacToe.board[i][j] == ' ':
                    return False
        return True
    


    def playGame(self) -> None:
        self.addPlayer()
        print('Starting game')
        print('Player 1 will start: ')
        player =  self.player1
        while True:
            self.ticTacToe.printBoard()
            print(f'Player {self.players[player]} turn make a move')
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            if not self.checkMove(row, col):
                continue
            if not self.makeMove(player, row, col):
                print('Invalid move')
                continue
            if self.checkWin(player):
                print(f'Player {self.players[player]} wins')
                self.ticTacToe.printBoard()
                break
            if self.checkDraw():
                print('Game Draw')
                self.ticTacToe.printBoard()
                break
            player = self.switchPlayer(player)


if __name__ == '__main__':
    game = Game()
    game.playGame()
