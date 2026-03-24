# IDDFS Implementation in Python (with different alphabets)

# Depth-Limited Search (DLS)
def dls(graph, node, goal, depth, visited):
    if depth == 0 and node == goal:
        return True
    
    if depth > 0:
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dls(graph, neighbor, goal, depth - 1, visited):
                    return True
        
        visited.remove(node)  # backtrack
    
    return False


# Iterative Deepening DFS
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        print(f"Searching at depth: {depth}")
        
        if dls(graph, start, goal, depth, visited):
            return True
    
    return False


# Example graph (new alphabets)
graph = {
    'P': ['Q', 'R'],
    'Q': ['S', 'T'],
    'R': ['U'],
    'S': [],
    'T': ['V'],
    'U': [],
    'V': []
}

start_node = 'P'
goal_node = 'V'
max_depth = 5

# Run IDDFS
if iddfs(graph, start_node, goal_node, max_depth):
    print(f"Goal node '{goal_node}' found!")
else:
    print(f"Goal node '{goal_node}' not found.")