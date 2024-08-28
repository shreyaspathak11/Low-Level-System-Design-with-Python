class Player:
    def __init__(self, name: str):
        self.name = name
        self.position = 0
        self.won = False
    
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position