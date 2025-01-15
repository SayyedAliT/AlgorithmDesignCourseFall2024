class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_with_mandatory_edges(n, edges, mandatory_edges):
    uf = UnionFind(n)
    mst_cost = 0
    added_edges = 0

    # Add mandatory edges first
    for u, v, w in mandatory_edges:
        if uf.union(u, v):
            mst_cost += w
            added_edges += 1
        else:
            return float('inf')  # Cycle detected, invalid MST

    # Add remaining edges to complete MST
    for u, v, w in edges:
        if added_edges == n - 1:
            break
        if uf.union(u, v):
            mst_cost += w
            added_edges += 1

    return mst_cost if added_edges == n - 1 else float('inf')

def can_include_bridges(n, m, edges, queries):
    edges = sorted(edges, key=lambda x: x[2])  # Sort edges by weight
    results = []

    for query in queries:
        k_i = query[0]
        requested_bridges_indices = query[1:k_i + 1]

        # Prepare mandatory edges and remaining edges
        mandatory_edges = [edges[idx - 1] for idx in requested_bridges_indices]
        remaining_edges = [edges[i] for i in range(m) if (i + 1) not in requested_bridges_indices]

        # Calculate MST cost with mandatory edges
        new_mst_cost = kruskal_with_mandatory_edges(n, remaining_edges, mandatory_edges)

        # Check if MST is valid and matches the initial MST
        if new_mst_cost != float('inf'):
            results.append("YES")
        else:
            results.append("NO")

    return results

# Input Handling
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0

    # Read number of islands and bridges
    n, m = int(data[index]), int(data[index + 1])
    index += 2

    edges = []

    # Read the bridges information
    for _ in range(m):
        u, v, w = int(data[index]), int(data[index + 1]), int(data[index + 2])
        edges.append((u - 1, v - 1, w))  # Convert to zero-indexed
        index += 3

    # Read number of queries
    q = int(data[index])
    index += 1

    queries = []

    # Read each query
    for _ in range(q):
        query_data = list(map(int, data[index:index + 1 + int(data[index])]))
        queries.append(query_data)
        index += 1 + int(data[index])

    # Function Call to get results
    results = can_include_bridges(n, m, edges, queries)

    # Print results for each query
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
