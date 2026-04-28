from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque()

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        \



        
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {
    'P': ['Q', 'R'],
    'Q': ['S', 'T'],
    'R': ['U', 'V'],
    'S': [],
    'T': [],
    'U': [],
    'V': []
}

# Start BFS
bfs(graph, 'P')