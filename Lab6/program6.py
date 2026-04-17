import heapq

# Graph definition
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3)],
    "D": [("G", 3)],
    "E": [("G", 1)],
    "F": [("G", 6)],
    "G": []
}


def ucs(graph, start, goal):
    # Priority Queue: (cost, node, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        # Goal check
        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        # Explore neighbors
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (new_cost, neighbor, new_path))

    return None, None


# Run UCS
start_node = "A"
goal_node = "G"

print("Running UCS from", start_node, "to", goal_node)

path, cost = ucs(graph, start_node, goal_node)

if path:
    print("Path Found:", path)
    print("Total Cost:", cost)
else:
    print("No path found")
