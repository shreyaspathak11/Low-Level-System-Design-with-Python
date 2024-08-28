from SpecialEntity import SpecialEntity

class Snake(SpecialEntity):
    def __init__(self, start, end):
        super().__init__(start, end)
    
    def getID(self):
        return f'(S_{self.end})'
    
    