from collections import deque

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}
print("DFS:")
print(dfs(graph, 2))

print("\nBFS:")
print(bfs(graph, 2))
