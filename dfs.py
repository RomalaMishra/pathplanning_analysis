from reconstruct import reconstruct_path


def dfs(grid, start, goal):
    neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
    stack = [start]
    came_from = {}
    visited = set([start])
    expanded = 0

    while stack:
        current = stack.pop()
        expanded += 1
        if current == goal:
            return reconstruct_path(came_from, start, goal), expanded
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:
                if grid[neighbor] == 1 or neighbor in visited:
                    continue
                stack.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current
    return None, expanded

