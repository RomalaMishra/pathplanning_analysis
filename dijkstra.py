
import heapq
from reconstruct import reconstruct_path

def dijkstra(grid, start, goal):
    neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}
    expanded = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        expanded += 1
        if current == goal:
            return reconstruct_path(came_from, start, goal), expanded
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:
                if grid[neighbor] == 1:
                    continue
                new_cost = cost_so_far[current] + 1
                if new_cost < cost_so_far.get(neighbor, float('inf')):
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (new_cost, neighbor))
    return None, expanded


