from SpecialEntity import SpecialEntity

class Ladder(SpecialEntity):
    def __init__(self, start, end):
        super().__init__(start, end)
    
    def getID(self):
        return f'(L_{self.end})'