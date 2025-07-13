from src.test.test import *

def main():
    # read final_testcase
    testcases = read_testcases("./src/test/final_testcase.txt")

    # -----------write time, memory,... to csv file-----------
    print("Choose the algorithm to run:")
    print("1. A*")
    print("2. UCS")
    print("3. BFS")
    print("4. DFS")

    choice = input("Enter the number corresponding to the algorithm (1-4): ").strip()

    if choice == "1":
        print("Running Astar...")
        test("Astar", testcases)
    elif choice == "2":
        print("Running UCS...")
        test("UCS", testcases)
    elif choice == "3":
        print("Running BFS...")
        test("BFS", testcases)
    elif choice == "4":
        print("Running DFS...")
        test("DFS", testcases)
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
    print("Done!")

    # -----------make data for GUI-----------
    # al = ["Astar", "DFS", "BFS" "UCS"]
    # for a in al:
    #     for j in range(20):
    #         make_data(a, j, testcases)
    
if __name__ == "__main__":
    main()