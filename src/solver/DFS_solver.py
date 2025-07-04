from .solver_base import Solver, Node
from ..game.game import Board
class DFSSolver(Solver):
    def __init__(self, initial_board: Board):
        super().__init__(initial_board)
        if initial_board.get_red_car().y != 2:
            raise ValueError("The red car must be at row 2 to be solveable.")
    
    def _reconstruct_path(self, node):
        return super()._reconstruct_path(node)

    def solve(self): 
        # Initialize stack with the initial board state
        stack = [Node(self.initial_board, 0, None)] 
        visited = set()
        visited.add(self.initial_board)  # Add the initial state to visited
        expanded_node = 0
        while stack:
            current_node = stack.pop()
            current_state = current_node.board
            # Check if the current state is goal
            if current_state.is_goal():
                self.solution = self._reconstruct_path(current_node)
                self.moves = current_node.moves
                self.expanded_nodes = expanded_node
                return
            # Check all the not visited states put it in the stack
            next_states = current_state.generate_next_states()
            for next_state in next_states:
                if next_state not in visited:
                    expanded_node += 1
                    visited.add(next_state)
                    next_node = Node(next_state, current_node.moves + 1, current_node)
                    stack.append(next_node)
            # No solution found
        self.solution = []
        self.moves = -1