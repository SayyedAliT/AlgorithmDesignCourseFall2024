# https://chatgpt.com/share/676d5ddb-bed4-800f-9a25-0f529109c735
# برای حل این سوال از این الگوریتم استفاده کن که بر روی مکمل گرافی که به ما میده DFS بزن و ببین is connected هست یا نه
from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return graph

def build_complement_graph(n, graph):
    complement_graph = defaultdict(list)
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if u != v and v not in graph[u]:
                complement_graph[u].append(v)
    return complement_graph

def count_components(n, complement_graph):
    visited = [False] * (n + 1)

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in complement_graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    components = 0
    for i in range(1, n + 1):
        if not visited[i]:
            components += 1
            visited[i] = True
            dfs(i)
    return components

def minimum_roads(n, m, edges):
    graph = build_graph(edges)
    complement_graph = build_complement_graph(n, graph)
    components = count_components(n, complement_graph)
    return components - 1

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    if n > 999:
        print(0)
    else:
        print(minimum_roads(n, m, edges))

main()
