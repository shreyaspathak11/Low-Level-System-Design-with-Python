class Board:
    def __init__(self, size):
        self.size = size
        self.board = [0] * size
        self.special_entities = {}

    def print_board(self):
        total_cells = self.size * self.size
        for i in range(total_cells, 0, -1):
            print(f' | {i} ', end='')

            if self.has_special_entity(i):
                print(f'({self.special_entities[i].getID()})', end='')

            print(' | ', end='')

            # Print a newline every `self.size` cells to create rows
            if (total_cells - i + 1) % self.size == 0:
                print()

        
    def has_special_entity(self, position):
        return position in self.special_entities
    
    def get_special_entity(self, position):
        return self.special_entities.get(position)
    
    def add_special_entity(self, special_entity):
        action_position = special_entity.get_action_position()
        self.special_entities[action_position] = special_entity

    def get_size(self):
        return self.size*self.size