import time
import tracemalloc
import csv
from ..helper.solver_factory import initialize_solver
from ..game.game import Board
test_cases = [
    {
        'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 4, 'y': 2, 'length': 2, 'dir': 'V'},
        'B': {'x': 4, 'y': 4, 'length': 2, 'dir': 'H'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 2, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 3, 'y': 1, 'length': 3, 'dir': 'H'},
        'D': {'x': 3, 'y': 4, 'length': 3, 'dir': 'H'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 2, 'y': 2, 'length': 2, 'dir': 'V'},
        'C': {'x': 2, 'y': 1, 'length': 3, 'dir': 'H'},
        'D': {'x': 1, 'y': 4, 'length': 3, 'dir': 'H'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 5, 'y': 0, 'length': 3, 'dir': 'V'},
        'B': {'x': 2, 'y': 1, 'length': 2, 'dir': 'V'},
        'C': {'x': 2, 'y': 0, 'length': 3, 'dir': 'H'},
        'D': {'x': 2, 'y': 4, 'length': 2, 'dir': 'H'},
        'E': {'x': 4, 'y': 4, 'length': 2, 'dir': 'H'}
    },
    {
        'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 4, 'y': 0, 'length': 3, 'dir': 'V'},
        'B': {'x': 3, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 4, 'y': 4, 'length': 2, 'dir': 'H'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 0, 'y': 4, 'length': 2, 'dir': 'V'},
        'E': {'x': 3, 'y': 0, 'length': 2, 'dir': 'V'},
        'F': {'x': 3, 'y': 2, 'length': 2, 'dir': 'V'},
        'G': {'x': 4, 'y': 2, 'length': 2, 'dir': 'V'},
        'H': {'x': 4, 'y': 4, 'length': 2, 'dir': 'V'},
        'B': {'x': 4, 'y': 0, 'length': 2, 'dir': 'H'},
        'C': {'x': 5, 'y': 1, 'length': 3, 'dir': 'V'},
        'D': {'x': 1, 'y': 4, 'length': 3, 'dir': 'H'}
    },
    {
        'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 4, 'y': 2, 'length': 2, 'dir': 'V'},
        'E': {'x': 4, 'y': 0, 'length': 2, 'dir': 'V'},
        'F': {'x': 3, 'y': 4, 'length': 2, 'dir': 'V'},
        'H': {'x': 2, 'y': 1, 'length': 2, 'dir': 'H'},
        'B': {'x': 4, 'y': 4, 'length': 2, 'dir': 'H'},
        'C': {'x': 2, 'y': 3, 'length': 3, 'dir': 'V'},
        'D': {'x': 5, 'y': 0, 'length': 3, 'dir': 'V'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 4, 'y': 3, 'length': 3, 'dir': 'V'},
        'B': {'x': 2, 'y': 0, 'length': 3, 'dir': 'V'},
        'C': {'x': 0, 'y': 4, 'length': 2, 'dir': 'V'},
        'D': {'x': 1, 'y': 4, 'length': 2, 'dir': 'H'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 1, 'y': 0, 'length': 2, 'dir': 'H'},
        'B': {'x': 3, 'y': 0, 'length': 2, 'dir': 'H'},
        'C': {'x': 0, 'y': 0, 'length': 2, 'dir': 'V'},
        'D': {'x': 2, 'y': 1, 'length': 2, 'dir': 'V'},
        'F': {'x': 3, 'y': 2, 'length': 3, 'dir': 'V'},
        'G': {'x': 4, 'y': 2, 'length': 3, 'dir': 'V'},
        'H': {'x': 0, 'y': 4, 'length': 3, 'dir': 'H'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 5, 'y': 1, 'length': 2, 'dir': 'V'},
        'B': {'x': 2, 'y': 4, 'length': 2, 'dir': 'H'},
        'C': {'x': 1, 'y': 4, 'length': 2, 'dir': 'V'},
        'D': {'x': 0, 'y': 3, 'length': 2, 'dir': 'H'},
        'E': {'x': 2, 'y': 5, 'length': 2, 'dir': 'H'},
        'F': {'x': 3, 'y': 1, 'length': 3, 'dir': 'V'},
        'G': {'x': 4, 'y': 1, 'length': 3, 'dir': 'V'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 2, 'y': 1, 'length': 2, 'dir': 'V'},
        'B': {'x': 2, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 1, 'y': 4, 'length': 2, 'dir': 'V'},
        'D': {'x': 0, 'y': 3, 'length': 2, 'dir': 'H'},
        'E': {'x': 2, 'y': 5, 'length': 2, 'dir': 'H'},
        'F': {'x': 3, 'y': 1, 'length': 3, 'dir': 'V'},
        'G': {'x': 4, 'y': 1, 'length': 3, 'dir': 'V'}
    },
    {
        'R': {'x': 2, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 4, 'y': 0, 'length': 3, 'dir': 'V'},
        'B': {'x': 3, 'y': 3, 'length': 2, 'dir': 'V'},
        'C': {'x': 4, 'y': 4, 'length': 2, 'dir': 'H'},
        'D': {'x': 0, 'y': 4, 'length': 3, 'dir': 'H'}
    },
    {
        'R': {'x': 0, 'y': 2, 'length': 2, 'dir': 'H'},
        'A': {'x': 4, 'y': 2, 'length': 2, 'dir': 'V'},
        'E': {'x': 4, 'y': 0, 'length': 2, 'dir': 'V'},
        'F': {'x': 3, 'y': 4, 'length': 2, 'dir': 'V'},
        'H': {'x': 2, 'y': 1, 'length': 2, 'dir': 'H'},
        'G': {'x': 0, 'y': 4, 'length': 2, 'dir': 'H'},
        'B': {'x': 4, 'y': 4, 'length': 2, 'dir': 'H'},
        'C': {'x': 2, 'y': 3, 'length': 3, 'dir': 'V'},
        'D': {'x': 5, 'y': 0, 'length': 3, 'dir': 'V'}
    },
]

def test_func(solver_name, test_case):
    board = Board(test_case)
    solver = initialize_solver(solver_name, board)

    tracemalloc.start()
    start_time = time.perf_counter()

    solver.solve()

    end_time = time.perf_counter()
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_sec = end_time - start_time  # second
    peak_memory_kb = peak_memory / 1024   # KB

    return elapsed_sec, peak_memory_kb, solver

def test(solver_name):
    results = []
    for idx, test_case in enumerate(test_cases):
        elapsed_sec, peak_memory, solver = test_func(solver_name, test_case)
        # no solution thi moves = -1 
        results.append([idx + 1, solver_name, elapsed_sec, peak_memory, solver.get_moves(), solver.get_expanded_nodes()])
    
    with open(f"{solver_name}_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["test_case_num", "solver_name", "time", "peak_memory", "moves", "node"])
        writer.writerows(results)


test("Astar")