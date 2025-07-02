from .game.game import Board, Car
from .solver.BFS_solver import BFSSolver

def main():
    cars = {
    'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
    'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
    'B': {'x': 2, 'y': 2, 'length': 2, 'dir': 'V'},
    'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
    'D': {'x': 1, 'y': 4, 'length': 3, 'dir': 'H'},
    }
    board = Board(cars)
    board.print()

    solver = BFSSolver(board)
    solver.solve()

    print(f"Number of moves: {solver.get_moves()}")
    print("Solution:")
    for step in solver.get_solution():
        step.print()
        print('---')


if __name__ == "__main__":
    main()
