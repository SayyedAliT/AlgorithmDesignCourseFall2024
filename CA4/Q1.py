# https://chatgpt.com/c/676d165d-b5f8-800f-b8a5-10d0d1670ce4
# assume that
# We have a graph
# In the input of the first hazard, first we enter the number of vertices and the number of edges with a space, and then we enter the edges in the next n line, now we have to do dfs or bfs on it and see if we can reach all the vertices or not.
# change code based on this
from collections import defaultdict, deque

def build_graph(n, m, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfs(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return visited

def can_reach_all_vertices(graph, n):
    visited = bfs(graph, 1, n)
    return all(visited[1:])

def minimum_edges_to_connect(n, m, edges):
    graph = build_graph(n, m, edges)
    return (n - 1) if can_reach_all_vertices(graph, n) else 0

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(minimum_edges_to_connect(n, m, edges))

# Main execution
if __name__ == "__main__":
    main()
