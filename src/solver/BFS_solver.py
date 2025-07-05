from .solver_base import Solver, Node
from collections import deque
from ..game.game import Board
class BFSSolver(Solver):
    def __init__(self, initial_board: Board):
        super().__init__(initial_board)
        if initial_board.get_red_car().y != 2:
            raise ValueError("The red car must be at row 2 to be solveable.")   
    
    def _reconstruct_path(self, node):
        return super()._reconstruct_path(node)

    def solve(self): 
        # Initialize queue with the initial board state
        # Note: BFS uses a queue, so we use deque for efficient pop from the left
        queue = deque([Node(self.initial_board, 0, None)])
        visited = set()
        visited.add(self.initial_board)
        expanded_nodes = 0
        while queue:
            current_node = queue.popleft()
            current_state = current_node.board
            expanded_nodes += 1
            # Check all the not visited states
            # and put it in the queue
            next_states = current_state.generate_next_states()
            for next_state in next_states:
                if next_state not in visited:
                    # Applies early goal check
                    # If the current state is the goal, reconstruct the path, get solution and return
                    if next_state.is_goal():
                        self.solution = self._reconstruct_path(current_node)
                        self.moves = current_node.moves
                        self.expanded_nodes = expanded_nodes
                        return
                    visited.add(next_state)
                    next_node = Node(next_state, current_node.moves + 1, current_node)
                    queue.append(next_node)
        self.solution = []
        self.moves = -1  
    
    

    

