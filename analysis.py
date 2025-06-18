import numpy as np
import matplotlib.pyplot as plt
import time
from astar import astar
from dijkstra import dijkstra
from bfs import bfs
from dfs import dfs

def run_and_compare(grid, start, goal):
    results = {}
    algos = {
        'A*': astar,
        'Dijkstra': dijkstra,
        'BFS': bfs,
        'DFS': dfs
    }
    for name, algo in algos.items():
        t0 = time.time()
        path, expanded = algo(grid, start, goal)
        t1 = time.time()
        results[name] = {
            'Path Length': len(path) if path else None,
            'Nodes Expanded': expanded,
            'Time (ms)': (t1 - t0) * 1000,
            'Path': path
        }
    return results

def print_comparison(results):
    print(f"{'Algorithm':<10} | {'Path Len':<8} | {'Nodes Expanded':<15} | {'Time (ms)':<10}")
    print("-" * 55)
    for name, res in results.items():
        print(f"{name:<10} | {str(res['Path Length']):<8} | {res['Nodes Expanded']:<15} | {res['Time (ms)']:.2f}")

def plot_all_subplots(grid, results, start, goal):
    import tkinter as tk

    root = tk.Tk()
    root.withdraw() 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    dpi = plt.rcParams.get('figure.dpi', 100)
    fig_width = screen_width / dpi
    fig_height = screen_height / dpi

    fig, axs = plt.subplots(2, 2, figsize=(fig_width, fig_height))
    algos = list(results.keys())
    colors = {
        'A*': 'red',
        'Dijkstra': 'blue',
        'BFS': 'green',
        'DFS': 'orange'
    }
    for idx, algo in enumerate(algos):
        ax = axs[idx // 2, idx % 2]
        ax.imshow(grid, cmap='Greys', origin='lower')
        res = results[algo]
        path = res['Path']
        if path:
            px, py = zip(*path)
            ax.plot(py, px, color=colors[algo], linewidth=2, label=f'Path ({algo})')
        ax.scatter(start[1], start[0], c='green', s=100, label='Start')
        ax.scatter(goal[1], goal[0], c='blue', s=100, label='Goal')
        ax.set_title(f"{algo}\nLen: {res['Path Length']}, Expanded: {res['Nodes Expanded']}, Time: {res['Time (ms)']:.2f} ms")
        ax.legend()
        ax.set_xticks(range(grid.shape[1]))
        ax.set_yticks(range(grid.shape[0]))
        ax.grid(True, which='both', color='gray', linewidth=0.5, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()
