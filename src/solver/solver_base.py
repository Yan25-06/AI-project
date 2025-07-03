from abc import ABC, abstractmethod
from ..game.game import Board

Solution = list[Board]

class Node: 
    def __init__(self, board: Board, moves:int, previous, priority):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.priority = priority  # cho A*, UCS (có thể tùy chỉnh sau)

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

class Solver(ABC):
    def __init__(self, initial_board: Board):
        self.initial_board = initial_board
        self.solution:Solution = []
        self.moves = -1
        self.expanded_nodes = -1

    @abstractmethod
    def solve(self):
        '''
        Tìm lời giải và lưu kết quả vào self.solution và self.moves
        '''
        pass

    def get_solution(self):
        return self.solution

    def get_moves(self):
        return self.moves
    
    def get_expanded_nodes(self):
        return self.expanded_nodes
    
    def get_move_cost(self, current_state, next_state):
        for name, car in current_state.cars.items():
            other_car = next_state.cars[name]
            if (car.x, car.y) != (other_car.x, other_car.y):
                return car.length         
        return 0

    def _reconstruct_path(self, node):
        path = []
        while node:
            path.append(node.board)
            node = node.previous
        path.reverse()
        return path
