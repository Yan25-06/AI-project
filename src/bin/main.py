from ..game.game import Board
from ..helper.solver_factory import initialize_solver

def main():
    # cars = {
    #     'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'},
    #     'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
    #     'B': {'x': 1, 'y': 3, 'length': 2, 'dir': 'V'},
    #     'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
    # }

    # cars = {
    #     'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'},
    #     'A': {'x': 4, 'y': 2, 'length': 2, 'dir': 'V'},
    #     'B': {'x': 4, 'y': 4, 'length': 2, 'dir': 'H'}
    # }

    cars = {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 5, 'y': 0, 'length': 3, 'dir': 'V'},
        'B': {'x': 2, 'y': 1, 'length': 2, 'dir': 'V'},
        'C': {'x': 2, 'y': 0, 'length': 3, 'dir': 'H'},
        'D': {'x': 2, 'y': 4, 'length': 2, 'dir': 'H'},
        'E': {'x': 4, 'y': 4, 'length': 2, 'dir': 'H'}
    }


    board = Board(cars) 
    print("Initial board:")
    print(board)

    solver = initialize_solver("UCS",board) 
    res = solver.solve() 

    print(f"Number of moves: {solver.get_moves()}")
    if res is None:
        print("No solution found.")
    else: 
        print(f"Number of expanded nodes: {solver.expanded_nodes}")
        print("Solution:")
        for step in solver.get_solution():
            step.print()
            print('---')



if __name__ == "__main__":
    main()
