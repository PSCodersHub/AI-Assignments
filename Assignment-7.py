# Q. Implement fundamental uninformed search algorithms like Depth-First Search (DFS). 

def dfs(graph, start):
    visited = set()
    stack = [start]  # Use stack for DFS

    while stack:
        node = stack.pop()  # Pop from the end (LIFO)

        if node not in visited:
            print("Visited:", node)
            visited.add(node)

            # Add neighbors to stack (in reversed order if you want to preserve order)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run DFS starting from 'A'
dfs(graph, 'A')

'''OUTPUT
Visited: A
Visited: B
Visited: D
Visited: E
Visited: F
Visited: C
'''