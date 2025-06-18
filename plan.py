import numpy as np
from analysis import run_and_compare, print_comparison, plot_all_subplots

class Plan:
    def __init__(self, grid_size, obstacles, start, goal):
        grid = np.zeros(grid_size)
        for obs in obstacles:
            grid[obs] = 1

        results = run_and_compare(grid, start, goal)
        print_comparison(results)
        plot_all_subplots(grid, results, start, goal)

if __name__ == "__main__":

    rows = int(input("Enter number of rows for grid: "))
    cols = int(input("Enter number of columns for grid: "))
    grid_size = (rows, cols)

    print("Enter obstacles as pairs of row and column indices (e.g., 1 7), one per line.")
    print("Enter a blank line to finish entering obstacles.")
    obstacles = []
    while True:
        line = input("Obstacle (row col): ").strip()
        if not line:
            break
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            obstacles.append((int(parts[0]), int(parts[1])))
        else:
            print("Invalid input. Please enter two integers separated by space.")


    start_row = int(input("Enter start row: "))
    start_col = int(input("Enter start column: "))
    goal_row = int(input("Enter goal row: "))
    goal_col = int(input("Enter goal column: "))
    start = (start_row, start_col)
    goal = (goal_row, goal_col)

    Plan(grid_size, obstacles, start, goal)
