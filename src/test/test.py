import time
import tracemalloc
import csv
from ..helper.solver_factory import initialize_solver
from ..game.game import Board
test_cases_1 = [
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

def test(solver_name, test_cases):
    results = []
    for idx, test_case in enumerate(test_cases):
        print(f"test{idx}")
        elapsed_sec, peak_memory, solver = test_func(solver_name, test_case)
        # no solution thi moves = -1 
        results.append([idx + 1, solver_name, elapsed_sec, peak_memory,len(test_case), solver.get_moves(), solver.get_expanded_nodes()])
    
    with open(f"{solver_name}_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["test_case_num", "solver_name", "time", "peak_memory","num_cars", "moves", "node"])
        writer.writerows(results)

def parse_test_cases(file_path: str) -> list[dict]:
    test_cases = []
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    i = 0
    while i < len(lines):
        puzzle_name = lines[i]     # bỏ qua tên
        i += 1
        grid_size = int(lines[i])  # cũng không dùng trong dict kết quả
        i += 1
        car_dict = {}
        label_index = 0
        labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        while i < len(lines) and lines[i] != ".":
            x, y, o, l = lines[i].split()
            x = int(x)
            y = int(y)
            l = int(l)
            dir = o.upper()

            # Red car luôn là key 'R', các xe còn lại dùng A, B, C,...
            if label_index == 0:
                label = 'R'
            else:
                label = labels[label_index - 1]
            car_dict[label] = {'x': x, 'y': y, 'length': l, 'dir': dir}

            label_index += 1
            i += 1

        test_cases.append(car_dict)
        i += 1  # bỏ qua dòng '.'
    return test_cases

def print_test_cases(test_cases: list[dict]):
    for idx, case in enumerate(test_cases, 1):
        print(f"Test case #{idx}:")
        for label in sorted(case.keys()):
            car = case[label]
            print(f"  {label}: x={car['x']}, y={car['y']}, length={car['length']}, dir={car['dir']}")
        print("-" * 40)

tests = parse_test_cases("./src/test/jams.txt")
# print_test_cases(tests)
test("BFS", tests)
# solver_name = "Astar"
# test_num = 0
# sec, mem, solver = test_func(solver_name, test_cases[test_num])
# print(sec)
# print(mem)
# print(solver.get_moves())
# print(solver.get_expanded_nodes())
# results = []
# results.append([test_num + 1, solver_name, sec, mem, solver.get_moves(), solver.get_expanded_nodes()])
# with open(f"{solver_name}_results.csv", "a", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerows(results)
# if not solver.solution:
#     print("no")
# else:
#     print("Solution:")
#     for step in solver.get_solution():
#         step.print()
#         print('---')