from collections import deque

def bfs_maze(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        # Goal check
        if (x, y) == goal:
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            # Possible moves: Up, Down, Left, Right
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                # Check valid move
                if (0 <= nx < rows and
                    0 <= ny < cols and
                    maze[nx][ny] != 1 and
                    (nx, ny) not in visited):

                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None

# Maze definition
maze = [
    ['S', 1, 0, 0, 0],
    [0,   1, 0, 1, 0],
    [0,   0, 0, 1, 0],
    [1,   1, 0, 0, 0],
    [0,   0, 0, 1, 'G']
]

start = (0, 0)
goal = (4, 4)

solution = bfs_maze(maze, start, goal)

if solution:
    print("Shortest path found:")
    print(solution)
    print("Steps:", len(solution))
else:
    print("No path found.")
