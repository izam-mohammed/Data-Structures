
# BFS in directed graph
def bfs(graph, start):
    visited = set()
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend([i for i in graph[node] if i not in visited])
            
            
            
            
            