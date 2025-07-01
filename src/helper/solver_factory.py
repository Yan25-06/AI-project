
from typing import Literal

from ..solver.solver_base import Solver
from ..solver.BFS_solver import BFSSolver
from ..solver.UCS_solver import UCSSolver
from ..solver.DFS_solver import DFSSolver
from ..solver.Astar_solver import AstarSolver 
from ..game.game import Board

SOLVER_NAME = Literal["BFS", "UCS", "DFS", "Astar"]
def initialize_solver(solver_name: SOLVER_NAME, board:Board) -> Solver:
    """
    Initialize the solver based on the given solver name.
    
    Args:
        solver_name (str): The name of the solver to initialize.
        board (Board): The game board to be solved.

    Returns:
        Solver: An instance of the specified solver.
    """
    if solver_name == 'BFS':
        return BFSSolver(board)
    elif solver_name == 'UCS':
        return UCSSolver(board)
    elif solver_name == 'DFS':
        return DFSSolver(board)
    elif solver_name == 'Astar':
        return AstarSolver(board)
    else:
        raise ValueError(f"Unknown solver: {solver_name}")