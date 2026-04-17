import heapq


class Node:
    def __init__(self, name, parent, g, h):
        self.name = name
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def a_star_trace(graph, heuristic, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_list, start_node)

    step = 0

    while open_list:
        step += 1
        current = heapq.heappop(open_list)

        print(f"\n===== Step {step} =====")
        print(f"Current Node: {current.name}")
        print(f"g(n) = {current.g}, h(n) = {current.h}, f(n) = {current.f}")

        # Print path so far
        path = []
        temp = current
        while temp:
            path.append(temp.name)
            temp = temp.parent
        path.reverse()

        print("Path so far:", " → ".join(path))

        # Goal check
        if current.name == goal:
            print("\nGoal Reached!")
            return current

        closed_set.add(current.name)

        # Expand neighbors
        for neighbor, cost in graph[current.name]:
            if neighbor in closed_set:
                continue

            new_node = Node(
                neighbor,
                current,
                current.g + cost,
                heuristic[neighbor]
            )

            heapq.heappush(open_list, new_node)

        # Print OPEN list
        print("\nOPEN LIST:")
        for node in open_list:
            print(f"{node.name} (g={node.g}, h={node.h}, f={node.f})")

        # Print CLOSED set
        print("\nCLOSED SET:")
        print(closed_set)

    return None


def print_final_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent

    path.reverse()
    print("\nFinal Path:", " → ".join(path))


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

solution = a_star_trace(graph, heuristic, start, goal)

if solution:
    print_final_path(solution)
else:
    print("No path found")
