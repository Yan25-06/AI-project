import time
import tracemalloc
import csv
import ast
import pickle
from ..helper.solver_factory import initialize_solver
from ..game.game import Board

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
    print(solver_name)
    for idx, test_case in enumerate(test_cases):
        print(f"test{idx}")
        elapsed_sec, peak_memory, solver = test_func(solver_name, test_case)
        # no solution thi moves = -1 
        results.append([idx + 1, solver_name, elapsed_sec, peak_memory,len(test_case), solver.get_moves(), solver.get_expanded_nodes()])
    
    with open(f"{solver_name}_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["test_case_num", "solver_name", "time", "peak_memory","num_cars", "moves", "node"])
        writer.writerows(results)

def read_testcases(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    testcases = []
    in_cars_block = False
    cars_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("cars ="):
            in_cars_block = True
            cars_lines = [stripped[len("cars ="):].strip()]
        elif in_cars_block:
            if stripped.startswith("Initial board:"):
                cars_str = '\n'.join(cars_lines)
                car_dict = ast.literal_eval(cars_str)
                testcases.append(car_dict)
                in_cars_block = False
            else:
                cars_lines.append(stripped)

    return testcases

def make_data(algorithm, testcases, test_index):
    _, _, solver = test_func(algorithm, testcases[test_index])
    last_board = solver.solution[-1]
    new_boards = []
    for dx in range(1, 5):  # tương ứng x=5,6,7,8
        new_cars = {name: car.copy() for name, car in last_board.cars.items()}
        new_cars['R'].x = 4 + dx  # cập nhật vị trí mới của xe đỏ
        new_boards.append(Board(new_cars, size=last_board.size))
        
    # Thêm vào solver.solution
    solver.solution += new_boards
    with open(f"src/GUI/Solution/{algorithm}/MAP_{test_index + 1}.pkl", "wb") as f:
        pickle.dump(solver.solution, f)

# read final_testcase
testcases = read_testcases("./src/test/final_testcase.txt")

# -----------make data for GUI-----------
# al = ["Astar", "DFS", "BFS" "UCS"]
# for a in al:
#     for j in range(20):
#         make_data(a, j, testcases)

# -----------write time, memory,... to csv file-----------
# test("Astar", testcases)
# test("UCS", testcases)
# test("BFS", testcases)
# test("DFS", testcases)

