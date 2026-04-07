tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dfs_iterative(start):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.append(node)
            
            # Add neighbors in reverse to maintain order
            stack.extend(reversed(tree[node]))
    
    return visited

result = dfs_iterative(1)
print("DFS Traversal:", " ".join(map(str, result)))