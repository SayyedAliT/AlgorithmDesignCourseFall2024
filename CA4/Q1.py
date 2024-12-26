class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [0] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def is_connected(n, edges):
    if not edges:
        return False

    uf = UnionFind(n)
    components = n

    for u, v in edges:
        if uf.union(u, v):
            components -= 1

    return components == 1


def solve():
    # Read input
    n, m = map(int, input().split())
    edges = []

    # Read edges
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Check base cases
    if m < n - 1 or n <= 1:
        print(0)
        return

    # Check if graph is connected using Union-Find
    if is_connected(n, edges):
        print(n - 1)  # Minimum number of edges needed for a connected graph
    else:
        print(0)  # Cannot make it connected using subset of existing edges


solve()