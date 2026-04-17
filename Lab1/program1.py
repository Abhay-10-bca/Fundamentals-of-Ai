def dfs_maze(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    # Stack stores (current_position, path_taken)
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        # Check if goal is reached
        if (x, y) == goal:
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            # Possible movements: Up, Down, Left, Right
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                # Check valid move
                if (0 <= nx < rows and
                    0 <= ny < cols and
                    maze[nx][ny] != 1 and
                    (nx, ny) not in visited):

                    stack.append(((nx, ny), path + [(nx, ny)]))

    return None


maze = [
    ['S', 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 'G']
]

start = (0, 0)
goal = (3, 3)

solution = dfs_maze(maze, start, goal)

if solution:
    print("Path found:")
    print(solution)
else:
    print("No path found.")
