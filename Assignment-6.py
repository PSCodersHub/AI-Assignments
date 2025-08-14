# Q. Implement fundamental uninformed search algorithms like Breadth-First Search (BFS).

def bfs(graph, start):
    visited = set()           # To track visited nodes
    queue = [start]           # Use list as queue (FIFO)

    while queue:
        node = queue.pop(0)   # Remove the first item (acts like dequeue)

        if node not in visited:
            print("Visited:", node)
            visited.add(node)

            # Enqueue all unvisited neighbors
            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

# Example graph represented as an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS starting from node 'A'
bfs(graph, 'A')

'''OUTPUT
Visited: A
Visited: B
Visited: C
Visited: D
Visited: E
Visited: F
'''