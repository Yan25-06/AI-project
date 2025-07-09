from .solver_base import Solver, Node
from ..game.game import Board
import sys
sys.setrecursionlimit(10**6)
class DFSSolver(Solver):
    def __init__(self, initial_board: Board):
        super().__init__(initial_board)
        if initial_board.get_red_car().y != 2:
            raise ValueError("The red car must be at row 2 to be solveable.")
    
    def _reconstruct_path(self, node):
        return super()._reconstruct_path(node)

    # def solve(self): 
    #     # Initialize stack with the initial board state
    #     stack = [Node(self.initial_board, 0, None)] 
    #     visited = set()
    #     visited.add(self.initial_board)  # Add the initial state to visited
    #     expanded_node = 0
    #     while stack:
    #         current_node = stack.pop()
    #         current_state = current_node.board
    #         expanded_node += 1
    #         # Check all the not visited states put it in the stack
    #         next_states = current_state.generate_next_states()
    #         for next_state in next_states:
    #             if next_state not in visited:
    #                 # Check if the current state is goal
    #                 if next_state.is_goal():
    #                     self.solution = self._reconstruct_path(current_node)
    #                     self.moves = current_node.moves + 1
    #                     self.expanded_nodes = expanded_node
    #                     return
    #                 visited.add(next_state)
    #                 next_node = Node(next_state, current_node.moves + 1, current_node)
    #                 stack.append(next_node)
    #         # No solution found
    #     self.solution = []
    #     self.moves = -1
    def solve(self):
        self.expanded_nodes = 0
        visited = set()
        result = self._dfs_backtrack(self.initial_board, 0, None, visited)
        if result:
            self.solution = result
            self.moves = len(result)
            return result
        else:
            self.solution = []
            self.moves = -1

    def _dfs_backtrack(self, current_state, moves, parent_node, visited):
        visited.add(current_state)
        self.expanded_nodes += 1
        next_states = current_state.generate_next_states()
        current_node = Node(current_state, moves, parent_node)
        for next_state in next_states:
            if next_state.is_goal():
                    current_node.moves += 1
                    return self._reconstruct_path(current_node)
            if next_state not in visited:
                print(f"Visiting state: {moves}")
                next_state.print()
                result = self._dfs_backtrack(next_state, moves + 1, current_node, visited)
                if result:
                    return result
        return None    