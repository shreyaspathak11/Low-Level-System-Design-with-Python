class GameAlreadyStartedException(Exception):
    def __init__(self):
        super().__init__('Game has already started. Cannot add more players')