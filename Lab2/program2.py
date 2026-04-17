def dfs_maze_3d(maze, start, goal):
    layers = len(maze)
    rows = len(maze[0])
    cols = len(maze[0][0])

    stack = [(start, [start])]
    visited = set()

    while stack:
        (z, x, y), path = stack.pop()

        # Goal check
        if (z, x, y) == goal:
            return path

        if (z, x, y) not in visited:
            visited.add((z, x, y))

            # 6 possible movements in 3D
            moves = [
                (0, -1, 0),   # Up
                (0, 1, 0),    # Down
                (0, 0, -1),   # Left
                (0, 0, 1),    # Right
                (-1, 0, 0),   # Back layer
                (1, 0, 0)     # Forward layer
            ]

            for dz, dx, dy in moves:
                nz, nx, ny = z + dz, x + dx, y + dy

                if (0 <= nz < layers and
                    0 <= nx < rows and
                    0 <= ny < cols and
                    maze[nz][nx][ny] != 1 and
                    (nz, nx, ny) not in visited):

                    stack.append(((nz, nx, ny), path + [(nz, nx, ny)]))

    return None


# 3D Maze definition
maze = [
    # Layer 0
    [
        ['S', 0, 1],
        [1, 0, 1],
        [1, 0, 0],
    ],
    # Layer 1
    [
        [1, 1, 1],
        [0, 0, 0],
        [1, 1, 0],
    ],
    # Layer 2
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 'G'],
    ],
]

start = (0, 0, 0)
goal = (2, 2, 2)

solution = dfs_maze_3d(maze, start, goal)

if solution:
    print("Path found:")
    for step in solution:
        z, x, y = step
        print(f"Layer {z}, Row {x}, Col {y}")
    print(f"\nTotal steps: {len(solution)}")
else:
    print("No path found.")
