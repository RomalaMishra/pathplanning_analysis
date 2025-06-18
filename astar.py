import heapq
from reconstruct import reconstruct_path

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    gscore = {start: 0}
    expanded = 0

    while open_set:
        _, _, current = heapq.heappop(open_set)
        expanded += 1
        if current == goal:
            return reconstruct_path(came_from, start, goal), expanded
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:
                if grid[neighbor] == 1:
                    continue
                tentative_gscore = gscore[current] + 1
                if tentative_gscore < gscore.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_gscore
                    fscore = tentative_gscore + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (fscore, tentative_gscore, neighbor))
    return None, expanded

