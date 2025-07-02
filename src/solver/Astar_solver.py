from .solver_base import Solver, Node
import heapq
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
        expanded_nodes = 0
        open_set = []
        visited = set()
        init_state = Node(self.initial_board, self.moves, None, self.heuristic(self.initial_board))
        heapq.heappush(open_set, init_state)
        while open_set:
            current = heapq.heappop(open_set)
            visited.add(current.board)
            expanded_nodes += 1
            if current.board.is_goal():
                self.solution = self._reconstruct_path(current)
                self.moves = current.moves
                print("tim thay path")
                return expanded_nodes
            next_states = current.board.generate_next_states()
            for board in next_states:
                if board in visited:
                    continue
                heapq.heappush(open_set, Node(board, current.moves + 1, current, current.moves + 1 + self.heuristic(board)))
        return None