# Q1.  Implement fundamental informed search algorithms like Greedy Search.

def greedy_search(graph, start, goal, heuristic):
    visited = []
    frontier = [start]
    
    while frontier:
        # Select the node with the lowest heuristic value
        current = min(frontier, key=lambda n: heuristic[n])
        frontier.remove(current)
        
        print("Visited:", current)
        if current == goal:
            break
        visited.append(current)
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited and neighbor not in frontier:
                frontier.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0
}

greedy_search(graph, 'A', 'F', heuristic)

'''OUTPUT
Visited: A
Visited: B
Visited: E
Visited: F
'''
