class SpecialEntity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_action_position(self):
        return self.start
    
    def get_end_position(self):
        return self.end
    