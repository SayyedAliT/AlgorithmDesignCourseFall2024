class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False


def solve(n, m, edges):
    edges_sorted = sorted(edges, key=lambda x: x[2])  # sort edges by weight
    dsu = DSU(n)

    mst_edges = []
    # Step 1: Kruskal's algorithm to get MST
    for u, v, w, idx in edges_sorted:
        if dsu.union(u, v):
            mst_edges.append((u, v, w, idx))

    mst_edges_set = set((min(u, v), max(u, v)) for u, v, w, idx in mst_edges)

    result = ["none"] * m
    # Step 2: Identify "any" edges (those present in every MST)
    for u, v, w, idx in edges:
        edge = (min(u, v), max(u, v))
        if edge in mst_edges_set:
            result[idx] = "any"

    # Step 3: Identify "at least one" edges (those present in at least one MST)
    for u, v, w, idx in edges:
        edge = (min(u, v), max(u, v))
        if edge in mst_edges_set:
            result[idx] = "at least one"

    return result


# Input parsing
n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((a - 1, b - 1, w, i))

# Solve and print the result
answers = solve(n, m, edges)
for ans in answers:
    print(ans)
