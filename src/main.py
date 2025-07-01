from .game.game import Board
from .solver.BFS_solver import BFSSolver

def main():
    cars = {
        'R': {'x': 2, 'y': 0, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 1, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
    }

    board = Board(cars)
    board.print()

    return 

    solver = BFSSolver(board)
    solver.solve()

    print(f"Number of moves: {solver.get_moves()}")
    print("Solution:")
    for step in solver.get_solution():
        step.print()
        print('---')


if __name__ == "__main__":
    main()
