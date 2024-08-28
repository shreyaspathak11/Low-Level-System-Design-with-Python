import random
class Dice:
    def __init__(self, n):
       self.maxValue = n
    
    def rollDice(self):
        return random.randint(1, self.maxValue)