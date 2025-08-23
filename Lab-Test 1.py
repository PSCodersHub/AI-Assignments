# Q. Implement Breadth-First Search (BFS).

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            print("Visited:", node)
            visited.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

graph = {
    '0': ['1', '2', '3'],
    '1': ['3'],
    '2': ['4'],
    '3': ['5', '6'],
    '4': ['5', '7'],
    '5': ['2'],
    '6': ['5'],
    '7': ['5','8'],
    '8': []
}

bfs(graph, '0')

'''OUTPUT
Visited: 0
Visited: 1
Visited: 2
Visited: 3
Visited: 4
Visited: 5
Visited: 6
Visited: 7
Visited: 8
'''




# Q. Implement Depth-First Search (DFS).

def dfs(graph, start):
    visited = []   # Also we can use (set()).
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print("Visited:", node)
            visited.append(node) # If we use set(), then instead of append() we have to use add().

            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    '0': ['1', '2', '3'],
    '1': ['3'],
    '2': ['4'],
    '3': ['5', '6'],
    '4': ['5', '7'],
    '5': ['2'],
    '6': [],
    '7': []
}

dfs(graph, '0')


'''OUTPUT
Visited: 0
Visited: 1
Visited: 3
Visited: 5
Visited: 2
Visited: 4
Visited: 7
Visited: 6
'''
