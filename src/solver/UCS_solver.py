from .solver_base import Solver, Node

class UCSSolver(Solver):
    def solve(self): ...
    # if is_goal
    #   self.solution = _reconstruct_path 
    #   ...