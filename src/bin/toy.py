from ..game.game import Board
from ..helper.solver_factory import initialize_solver
from ..solver.solver_base import Node 

def is_goal_check():
    cars = {
        'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 1, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
    }
    board = Board(cars) 
    res = board.is_goal() 
    print(f"Is goal state: {res}")  # Expected: False


    cars = {
        'R': {'x': 4, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 1, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
    }
    board = Board(cars) 
    res = board.is_goal() 
    print(f"Is goal state: {res}")  # Expected: true

def main():
    cars = {
        'R': {'x': 2, 'y': 0, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 1, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
    }

    board = Board(cars) 
    print("Initial board:")
    board.print() 
    print("Generating next states...")
    states = board.generate_next_states()  # Generate next states to test the function
    for state in states:
        print("Next state:")
        state.print()  # Print each generated state

    return
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

def equality_check():  
    nodea = Node(Board({'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'}}), 0, None) 
    nodeb = Node(Board({'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'}}), 0, None)
    # print(f"Node A == Node B: {nodea == nodeb}")  # Expected: True 
    visited = {} 
    visited[nodea] = 1.0 

    # print( nodeb in visited ) # True  
    print(f"Node A == Node B: {nodea == nodeb}")  # Expected: True


    # board check 
    boardA = Board({'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'}}) 
    boardB = Board({'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'}}) 

    visited = set()
    visited.add(boardA)
    visited.add(boardB)

    print(f"Board A == Board B: {boardA == boardB}")  # True
    print(len(visited)) # in ra 1
    print(boardA in visited)  # True
    print(boardB in visited)  # True




def set_passed_by_reference(visited: set): 
    visited.add(2)
    print("visited in nested", visited)
def is_set_passed_by_reference():  
    visited = set()     
    # boardA = Board({'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'}})

    set_passed_by_reference(visited) 
    print("visited in main", visited)  








if __name__ == "__main__":
    # equality_check()
    #is_set_passed_by_reference()
    pass 
    # main()
    # is_goal_check()
    

