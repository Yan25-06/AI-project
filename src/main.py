from .game.game import Board
from .helper.solver_factory import initialize_solver

def main():
    cars = {
        'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 1, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
    }

    board = Board(cars) 
    print("Initial board:")
    board.print()

    solver = initialize_solver("UCS",board) 
    res = solver.solve() 

    print(f"Number of moves: {solver.get_moves()}")
    if res is None:
        print("No solution found.")
    else: 
        print("Solution:")
        for step in solver.get_solution():
            step.print()
            print('---')



if __name__ == "__main__":
    main()
