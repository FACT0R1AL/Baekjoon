import sys
from collections import deque

input = sys.stdin.readline

def dfs_stack(graph, start):
    visited = []
    stack = [start]
    flag = False

    for key in graphs.keys():
        if (key == start): flag = True

    if (flag):
        while stack:
            node = stack.pop()

            if node not in visited:
                visited.append(node)
                dfs_result.append(node)

                for next_node in reversed(graph[node]):
                    if next_node not in visited:
                        stack.append(next_node)
        
        return visited
    else:
        dfs_result.append(start)
        return


def bfs(graph, start):
    queue = deque([start])
    visited = [start]
    flag = False

    for key in graphs.keys():
        if (key == start): flag = True

    if (flag):
        while queue:
            node = queue.popleft()
            bfs_result.append(node)

            for next in graph[node]:
                if next not in visited:
                    visited.append(next)
                    queue.append(next)
    else:
        bfs_result.append(start)
        return

n, m, v = map(int, input().rstrip().split())
graphs = {}
dfs_visited = []

dfs_result = []
bfs_result = []

for _ in range(m):
    a, b = map(int, input().split())
    graphs.setdefault(a, []).append(b)
    graphs.setdefault(b, []).append(a)

for key in graphs:
    graphs[key].sort()

# print(graphs)

dfs_stack(graphs, v)
bfs(graphs, v)

print(*dfs_result)
print(*bfs_result)