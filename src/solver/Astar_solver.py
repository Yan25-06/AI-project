from .solver_base import Solver, Node
from ..game.game import Board
#from heapdict import heapdict
class AstarSolver(Solver):
    def _calc_up_down_block_car(self, target_car, board):
        up, down = 0, 0

        for car in board.cars.values():
            # up
            if (car.y < 2 and ((car.dir == 'V' and car.x == target_car.x) or (car.dir == 'H' and car.x <= target_car.x and car.x + car.length - 1 >= target_car.x))):
                up += 1
            # down
            elif (car.y > 2 and ((car.dir == 'V' and car.x == target_car.x) or (car.dir == 'H' and car.x <= target_car.x and car.x + car.length - 1 >= target_car.x))):
                down += 1

        return up, down

    def heuristic(self, board):
        red_car = board.get_red_car()
        # h(n) = 0 if it's at exit
        if (red_car.x == board.exit_col):
            return 0
        
        # h(n) = a (num of block cars of redCar) + min(num of block cars of a) + manhanttan distance

        # calc manhattan distance
        heuristics_val = board.exit_col - red_car.x

        # calc num of block cars of redCar
        block_cars = []
        for car in board.cars.values():
            if (car.dir == 'V' and car.x >= red_car.x + red_car.length and (car.y <= red_car.y and car.y + car.length - 1 >= red_car.y)):
                heuristics_val += 1
                block_cars.append(car)

        # calc min num of block cars of a
        for block_car in block_cars:
            block_car_up, block_car_down = self._calc_up_down_block_car(block_car, board)
            if (block_car == 3): # chi tinh phia duoi 
                heuristics_val += block_car_down
            else: 
                heuristics_val += min(block_car_up, block_car_down)

        return heuristics_val
    
    def solve(self): 
        open_set = heapdict()
        visited: dict[Board,int] = {}
        f_score: dict[Board,int] = {}
        board_to_Node: dict[Board, Node] = {}

        self.expanded_nodes = 0
        init_state = Node(self.initial_board, self.moves, None)
        init_state.priority = self.heuristic(self.initial_board)
        open_set[self.initial_board] = init_state.priority
        f_score[self.initial_board] = init_state.priority
        board_to_Node[self.initial_board] = init_state
        
        while open_set:
            current_board, curr_priority = open_set.popitem()
            self.expanded_nodes += 1
            curr_node = board_to_Node[current_board]
            if current_board.is_goal():
                self.solution = self._reconstruct_path(curr_node)
                self.moves = len(self.solution) - 1
                return 
               
            if current_board in visited:
                continue
            visited[current_board] = curr_priority
            next_states = current_board.generate_next_states() 

            for board in next_states:
                if board in visited:
                    continue
                g = curr_node.moves + self.get_move_cost(current_board, board)
                f = g + self.heuristic(board)
                if board not in f_score or f < f_score[board]:
                    open_set[board] = f
                    f_score[board] = f
                    neighbor = Node(board, g, curr_node)
                    neighbor.priority = f
                    board_to_Node[board] = neighbor
        return